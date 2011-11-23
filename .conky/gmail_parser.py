import os
import sys
import urllib2            
import feedparser
import base64
import pynotify
from keyring import get_password
from ConfigParser import ConfigParser
from textwrap import wrap

CONFIG_FILE = os.path.expanduser("~/.conky/.conkysettings")


def _get_config():
    config = ConfigParser()
    config.read([CONFIG_FILE])
	
    if not config.has_section("settings"):
        config.add_section("settings")
    
    if not config.has_option("settings","username"):
        config.set("settings","username","rottmanj")
    
    if not config.has_option("settings","show_notify"):
        config.set("settings","show_notify","False")
    
    if not config.has_option("settings","url"):
       config.set("settings","url","https://mail.google.com/mail/feed/atom/")
    
    if not config.has_section("messages"):
       config.add_section("messages")
    
    return config
	
def get_messages():
    config = _get_config()
    username = config.get("settings","username")
    
    if not config.has_option("settings", "password"):
        password = get_password("gmail", username)
    else:
        password = config.get("settings", "password")
        
    request = urllib2.Request(config.get("settings","url"))
    request.add_header("Authorization", "Basic %s" % (base64.encodestring("%s:%s" % (username, password))[:-1]))
    f = urllib2.urlopen(request)
    feed = f.read()
    return feed
    
def readmail(feed):
    messages = feedparser.parse(feed)
    total = int(len(messages.entries))
    
    pynotify.init("Basics")
    n = pynotify.Notification(messages.entries[0].title, messages.entries[0].author)
    n.show()
    
    return feed
	
if __name__ == "__main__":
    return readmail(get_messages())