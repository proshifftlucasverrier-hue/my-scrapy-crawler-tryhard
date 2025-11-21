import re
from bs4 import BeautifulSoup

class EncodingDetectorMiddleware:
    """
    Middleware non bloquant qui détecte charset déclaré et signes de mojibake.
    Résultats stockés dans response.request.meta['encoding_check'] ou response.meta['encoding_check'].
    """
    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        try:
            raw = response.body  # bytes

            # header charset
            ct = response.headers.get(b'Content-Type', b'').decode('latin1', errors='ignore')
            header_cs = None
            m = re.search(r'charset=([-\w]+)', ct, re.I)
            if m:
                header_cs = m.group(1).lower()

            meta_val = None
            equiv_val = None
            try:
                soup = BeautifulSoup(raw, "lxml")
                meta_cs = soup.find("meta", charset=True)
                if meta_cs and meta_cs.get("charset"):
                    meta_val = meta_cs["charset"].lower()
                equiv = soup.find("meta", attrs={"http-equiv": re.compile("content-type", re.I)})
                if equiv and equiv.get("content"):
                    m2 = re.search(r'charset=([-\w]+)', equiv["content"], re.I)
                    if m2:
                        equiv_val = m2.group(1).lower()
            except Exception:
                pass

            # détection mojibake
            try:
                text_latin1 = raw.decode('iso-8859-1', errors='replace')
            except Exception:
                text_latin1 = ''
            try:
                text_utf8 = raw.decode('utf-8', errors='replace')
            except Exception:
                text_utf8 = ''

            p = {
                "Ã© Ã´ Ã§ Ã¨ etc.": len(re.findall(r'Ã[a-zà-ÿ]', text_latin1)),
                "â€™ â€œ â€\u009d": len(re.findall(r'â[\u20ac\u201c\u201d\u201e\u2018\u2019]', text_latin1)),
                "�": text_utf8.count('�') + text_latin1.count('�'),
                "???": len(re.findall(r'\?{3,}', text_latin1 + text_utf8))
            }
            total = sum(p.values())

            result = {
                "header_charset": header_cs,
                "meta_charset": meta_val,
                "http_equiv_charset": equiv_val,
                "problems": {k: v for k, v in p.items() if v},
                "total_errors": total
            }

            if (not any([header_cs, meta_val, equiv_val])) or total > 0:
                spider.logger.warning("EncodingDetector: problèmes détectés pour %s : %s", request.url, result)

            # attacher aux meta de la requête / réponse
            try:
                if getattr(response, 'request', None) and response.request.meta is not None:
                    response.request.meta['encoding_check'] = result
                else:
                    response.meta = dict(response.meta) if response.meta is not None else {}
                    response.meta['encoding_check'] = result
            except Exception:
                pass

        except Exception as e:
            spider.logger.debug("EncodingDetector failed: %s", e)

        return response

    def process_exception(self, request, exception, spider):
        return None