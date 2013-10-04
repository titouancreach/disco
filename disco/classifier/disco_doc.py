#!/usr/bin/env python3

import os
import re

path = './disco_modules/'

os.system('cd ' + path)

file_list = [f for f in os.listdir(path) if re.match(r'.*\.py(.?)$', f)]
file_list = [f.split('.')[0] for f in file_list ]

for i in file_list:
    os.system('pydoc -w ' + i)

os.system('cd ..')
