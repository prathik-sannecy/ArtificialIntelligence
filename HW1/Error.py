class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class BadPartyTableMatrix(Error):
    """Invalid Table matrix format"""
    def __init__(self, message):
       self.message = message

    def __str__(self):
        return(repr(self.message))