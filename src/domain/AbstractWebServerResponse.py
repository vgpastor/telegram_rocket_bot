from requests import Response

class AbstractWebServerResponse:
    def parse(self, data) -> Response:
        raise NotImplementedError("You must implement this method")
