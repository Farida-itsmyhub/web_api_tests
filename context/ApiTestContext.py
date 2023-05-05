from .BaseContext import BaseContext


class ApiTestContext(BaseContext):
    base_url: str = "https://reqres.in"
    users_url: str = "/api/users"
    unknown_url: str = "/api/unknown"
    register_url: str = "/api/register"
    login_url: str = "/api/login"
