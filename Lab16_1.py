#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
html = urlopen("http://www.codeabbey.com/index/user_ranking")
print(html.read())