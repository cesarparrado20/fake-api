from functools import wraps
from flask import request, Response


def api_logger(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(f"Request contains: {request.data.decode('utf-8')}")
        response: Response | str = f(*args, **kwargs)
        if isinstance(response, Response):
            print(
                f"Response [{response.status}] is: {response.data.decode('utf-8')}"
            )
        else:
            print(f"Response is: {response}")
        return response

    return decorated_function
