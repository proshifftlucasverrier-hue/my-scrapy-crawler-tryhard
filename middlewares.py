class CustomMiddleware:
    def process_request(self, request, spider):
        # Modify the request before it is sent
        return None

    def process_response(self, request, response, spider):
        # Modify the response before it is processed
        return response

    def process_exception(self, request, exception, spider):
        # Handle exceptions that occur during the request
        return None