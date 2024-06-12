# URLBuilder - Builder Design Patterns

The **``URLBuilder``** is a Python class that allows you to construct URLs with various components such as ``scheme``, ``username``, ``password``, ``host``, ``port``, ``path``, and ``query`` parameters.

## Builder Design Pattern

The Builder pattern is a creational design pattern that separates the construction of a complex object from its representation. It allows the same construction process to create different representations.

In the provided code:

- ``URLBuilder`` Class: _This class serves as the builder. It encapsulates the construction logic for creating instances of the ``URL`` class._

- ``URL`` Class: _This class represents the complex object that the builder constructs._

### Advantages of Using the Builder Pattern

- **Encapsulates Construction Logic**: The construction logic for creating ``URL`` objects is encapsulated within the ``URLBuilder`` class. This makes the construction process more modular and easier to manage.

- **Flexible Object Construction**: The builder allows for flexible construction of ``URL`` objects by providing methods to set different components such as ``scheme``, ``username``, ``password``, ``host``, ``port``, ``path``, and ``query`` parameters independently.

- **Improves Readability**: Using a builder improves code readability by clearly separating the construction steps from the rest of the code.

- **Avoids Telescoping Constructors**: With the builder pattern, there's no need for constructors with numerous parameters (telescoping constructors), which can be difficult to maintain and use.

## Example

**Code :**
```python
from urlbuilder.url_builder import URLBuilder

def print_url_details(url):
    print("================================[ URL Info ]================================")
    print(f"URL : {url.to_string()}")
    print(f"Host : {url.get_host()}")
    print(f"Port : {url.get_port()}")
    print(f"Scheme : {url.get_scheme()}")
    print(f"Username : {url.get_username()}")
    print(f"Password : {url.get_password()}")
    print(f"Path : {url.get_path()}")
    print("----------------------------------------------------------------------------")
    print("Parameters:")
    print("----------------------------------------------------------------------------")
    for key, value in url.get_params().items():
        print(f"{key} : {value}")
    print("============================================================================")

if __name__ == "__main__":
    # Example usage:
    builder = URLBuilder("www.example.com")
    url = builder.set_scheme("http")\
                .set_username("user")\
                .set_password("pass")\
                .set_port(8080)\
                .set_path("post/details")\
                .add_param("pagesize",10)\
                .add_param("page",3)\
                .build()
    print_url_details(url)
```
**Output :**
```
================================[ URL Info ]================================
URL : http://user:pass@www.example.com:8080/post/details?pagesize=10&page=3
Host : www.example.com
Port : 8080
Scheme : http
Username : user
Password : pass
Path : post/details
----------------------------------------------------------------------------
Parameters:
----------------------------------------------------------------------------
pagesize : 10
page : 3
============================================================================
```

