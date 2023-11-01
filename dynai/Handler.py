class WrongURLProvided(Exception):
    """Raised when a wrong URL is provided."""

    def __init__(self, url: str, msg: str):
        """Constructor for"""
        if msg is not None:
            _custom_message = "Additional information: " + msg
        else:
            _custom_message = ""
        self.url = url
        self.message = "FATAL ERROR: WRONG URL PROVIDED\n\n YOUR INPUT" + url + " \n You have provided a wrong URL. Possibly because you forgot https:// or http:// or provided an invalid pattern. \n \n URL Pattern: https://example.com/path\n\n\n" + _custom_message

