# +--------------------------------------------------+
# |                       URL                        |
# |                =================                 |
# |           Author : Prashant Bhandari             |
# +--------------------------------------------------+
# | The URL is a Python class that represents URL.   |
# +--------------------------------------------------+ 

from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class URL:
    """A data class representing a URL."""
    scheme: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    path: Optional[str] = ""
    params: Optional[Dict[str, str]] = None

    def __post_init__(self):
        if self.params is None:
            self.params = {}

    def to_string(self) -> str:
        """Constructs the URL string."""
        
        # List of components that must always be provided
        unignorable_components = ['scheme', 'host'] 

        # Check if any unignorable component is missing
        missing_components = [comp for comp in unignorable_components if getattr(self, comp) is None]
        if missing_components:
            errmsg = f"Missing required components: {', '.join(missing_components)}"
            raise ValueError(errmsg)
        
        url = f"{self.scheme}://"
        if self.username is not None:
            url += f"{self.username}"
            if self.password is not None:
                url += f":{self.password}"
            url += "@"
        if self.host is not None:
            url += self.host
        if self.port is not None:
            url += f":{self.port}"
        if self.path is not None:
            url += f"/{self.path}"
        if self.params:
            param_string = "&".join([f"{key}={value}" for key, value in self.params.items()])
            url += f"?{param_string}"
        return url
    
    # Getter methods for other components

    def get_scheme(self) -> Optional[str]:
        """Returns the scheme of the URL."""
        return self.scheme

    def get_username(self) -> Optional[str]:
        """Returns the username of the URL."""
        return self.username

    def get_password(self) -> Optional[str]:
        """Returns the password of the URL."""
        return self.password

    def get_host(self) -> Optional[str]:
        """Returns the host of the URL."""
        return self.host

    def get_port(self) -> Optional[int]:
        """Returns the port of the URL."""
        return self.port

    def get_path(self) -> Optional[str]:
        """Returns the path of the URL."""
        return self.path

    def get_params(self) -> Optional[Dict[str, str]]:
        """Returns the parameters of the URL."""
        return self.params

    # Setter methods for URL components

    def set_scheme(self, scheme: Optional[str]) -> None:
        """Sets the scheme of the URL."""
        self.scheme = scheme

    def set_username(self, username: Optional[str]) -> None:
        """Sets the username of the URL."""
        self.username = username

    def set_password(self, password: Optional[str]) -> None:
        """Sets the password of the URL."""
        self.password = password

    def set_host(self, host: Optional[str]) -> None:
        """Sets the host of the URL."""
        self.host = host

    def set_port(self, port: Optional[int]) -> None:
        """Sets the port of the URL."""
        self.port = port

    def set_path(self, path: Optional[str]) -> None:
        """Sets the path of the URL."""
        self.path = path

    def set_params(self, params: Optional[Dict[str, str]]) -> None:
        """Sets the parameters of the URL."""
        self.params = params

    # Methods to manage param
        
    def get_param_value(self, key: str) -> Optional[str]:
        """Returns the value of a parameter by key."""
        if self.params is not None:
            return self.params.get(key)
        return None
        
    def add_param(self, key: str, value: str) -> None:
        """Adds a parameter to the URL if it doesn't already exist."""
        if self.params is None:
            self.params = {}
        if key not in self.params:
            self.params[key] = value
        else:
            raise ValueError(f"Parameter '{key}' already exists in the URL.")

    def update_param(self, key: str, value: str) -> None:
        """Updates a parameter in the URL if it exists."""
        if self.params is None:
            self.params = {}
        if key in self.params:
            self.params[key] = value
        else:
            raise ValueError(f"Parameter '{key}' does not exist in the URL.")

    def delete_param(self, key: str) -> None:
        """Deletes a parameter from the URL if it exists."""
        if self.params is not None and key in self.params:
            del self.params[key]
        else:
            raise ValueError(f"Parameter '{key}' does not exist in the URL.")