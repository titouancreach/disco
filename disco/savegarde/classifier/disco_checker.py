#!/usr/bin/env python3


"""
Just script who check if dependences needed by disco are there
"""

try:
    import sys
    sys.path.insert(0, './disco_modules')
    if sys.version_info < (3,):
        raise Exception('Disco classifier requier python 3.x')
    from flask import Flask, request, session
    from flask.ext.classy import FlaskView, route
    import json
    from disco_classifiers import *
    from disco_classifier import *
    from disco_init import *
    from disco_const import *
    from disco_decorator import *
    import os.path

except ImportError as e:
    print(e)
else:
    print('Everithing is ok ... ')
