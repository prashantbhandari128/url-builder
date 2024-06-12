# +-------------------------------------------------+
# |                    URLBuider                    |
# |                =================                |
# |           Author : Prashant Bhandari            |
# +-------------------------------------------------+
# | The URL Builder is a Python class that allows   |
# | you to construct URLs with various components   |
# | such as scheme, username, password, host, port, |
# | path, and query parameters.                     |
# +-------------------------------------------------+

from urlbuilder.url import URL

class URLBuilder:
    """A builder class for constructing URLs."""

    def __init__(self, host: str = None):
        self.scheme = None
        self.username = None
        self.password = None
        self.host = host
        self.port = None
        self.path = None
        self.params = None

    def set_scheme(self, scheme: str) -> 'URLBuilder':
        """Sets the scheme of the URL."""
        self.scheme = scheme
        return self

    def set_username(self, username: str) -> 'URLBuilder':
        """Sets the username of the URL."""
        self.username = username
        return self

    def set_password(self, password: str) -> 'URLBuilder':
        """Sets the password of the URL."""
        self.password = password
        return self
    
    def set_host(self, host: str) -> 'URLBuilder':
        """Sets the host of the URL."""
        self.host = host
        return self

    def set_port(self, port: int) -> 'URLBuilder':
        """Sets the port of the URL."""
        self.port = port
        return self

    def set_path(self, path: str) -> 'URLBuilder':
        """Sets the path of the URL."""
        self.path = path
        return self

    def add_param(self, key: str, value: str) -> 'URLBuilder':
        """Adds a parameter to the URL."""
        if self.params is None:
            self.params = {}
        self.params[key] = value
        return self

    def build(self) -> URL:
        """Constructs the URL object."""
        return URL(self.scheme, self.username, self.password, self.host, self.port, self.path, self.params)