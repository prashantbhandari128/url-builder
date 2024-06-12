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