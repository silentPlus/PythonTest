# -*- coding: utf-8 -*-
import os
import subprocess

# os.system("ping 127.0.0.1")

f = open("conf.txt", "r");
content = f.read()
os.system(content)