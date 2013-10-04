#!/usr/bin/env python3

#
# CNET - Content Solution
#
# Disco classifier
#
# Module name : main
#
# Titouan CREACH
#
# titouan.creach@gmail.com
# titouan.creach@cbsi.com
#
import sys

#add path to default interpreter path
sys.path.insert(0, './disco_modules')

import json
from  flask import Flask
from disco_const import *
from disco_net import *

app = Flask(__name__)
disco_net.register(app)

if __name__ == '__main__':
    app.run(debug=DEBUG_MODE)
