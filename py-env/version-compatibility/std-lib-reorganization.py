from future import standard_library
standard_library.install_aliases()

# Then these Py3-style imports work on both Python 2 and Python 3:
import socketserver
import queue
from collections import UserDict, UserList, UserString
from collections import Counter, OrderedDict, ChainMap   # even on Py2.6
from itertools import filterfalse, zip_longest

import html
import html.entities
import html.parser

import http
import http.client
import http.server
import http.cookies
import http.cookiejar

import urllib.request
import urllib.parse
import urllib.response
import urllib.error
import urllib.robotparser

import xmlrpc.client
import xmlrpc.server
