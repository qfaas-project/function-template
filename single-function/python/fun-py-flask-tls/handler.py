import time

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    # print(str(type(req)))
    # print(req)
    return f'Response from fun-py-flask-tls: {time.asctime()}, echo: {req}'   
