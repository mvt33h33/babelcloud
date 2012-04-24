# Copyright (C) 2011 by Alex Brandt <alunduil@alunduil.com>

def servererrorhandler(func):
    """This handles all the HTTP errors that libcloud might propogate.
    
    Turns those propogated errors into categorized exceptions that can be
    handled generically.

    """

    def new_func(*args, **kargs):
        try:
            return func(*args, **kargs)
        except Exception as error:
            if error.message.startswith("413"):
                raise APILimitError(error.message)
            elif error.message.startswith("500"):
                raise ServerError(error.message)
            else:
                raise error

    return new_func

class APILimitError(RuntimeError):
    pass

