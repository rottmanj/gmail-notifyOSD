import os
import sys
import urllib2            # For BasicHTTPAuthentication
import feedparser         # For parsing the feed
import base64
import pynotify
from textwrap import wrap

CONFIG_FILE = os.path.expanduser("~/.conky/.conkysettings")



