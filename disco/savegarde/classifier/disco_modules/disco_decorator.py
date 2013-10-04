#
# CNET - Content Solution
#
# Disco classifier
#
# Module name : disco_decorator
#
# Titouan CREACH
#
# titouan.creach@gmail.com
# titouan.creach@cbsi.com
#

#from disco_globals import *
from functools import wraps

def disco_assert(ev, debug, msg):
    """
    This decorator is used for execute function ONLY if "condition" is true.
    When Debug is true, some information are printed on stdout
    """
    global g_state
    def decorator(func):
        @wraps(func)
        def wrapper(*args):
            if not ev:
                if debug:
                    print('assert failed : ' + msg)
                    print('from : ' + func.__name__)
                return ''
            return func(*args)
        return wrapper
    return decorator
