def array_sort(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    content_type = request.headers['content-type']
    if content_type == 'application/json':
        request_json = request.get_json(silent=True)
        if request_json and 'a' in request_json:
            a = request_json['a']
        else:
            raise ValueError("JSON is invalid, or missing 'a' property array")

        if request_json and 'b' in request_json:
            b = request_json['b']
        else:
            raise ValueError("JSON is invalid, or missing 'b' property array")            
    else:
        raise ValueError("Expecting a json format")
        
    new=a+b
    new1 = sorted(new)
    return str(new1)



