## check-gmail.py -- A command line util to check GMail -*- Python -*-
## modified to display mailbox summary for conky

# ======================================================================
# Copyright (C) 2006 Baishampayan Ghose <b.ghose@ubuntu.com>
# Modified 2008 Hunter Loftis <hbloftis@uncc.edu>
# Time-stamp: Mon Jul 31, 2006 20:45+0530
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
# ======================================================================

import os
import sys
import urllib2            # For BasicHTTPAuthentication
import feedparser         # For parsing the feed
import base64
from textwrap import wrap

_URL = "https://mail.google.com/gmail/feed/atom"

uname = sys.argv[1]
password = sys.argv[2]
maxlen = sys.argv[3]

	
def auth():
    '''The method to do HTTPBasicAuthentication'''
    req = urllib2.Request(_URL)
    req.add_header("Authorization", "Basic %s" % (base64.encodestring("%s:%s" % (uname, password))[:-1]))
    f = urllib2.urlopen(req)
    feed = f.read()
    return feed


def readmail(feed, maxlen):
	'''Parse the Atom feed and print a summary'''
	atom = feedparser.parse(feed)
	total = int(len(atom.entries))
	'''Check count for pass to notify'''
	if total >cnt:
		notifier = "notify-send '" + atom.entries[0].title  + "'   '" + atom.entries[0].author + "' -i ~/.conky/mail.png"
		os.popen("play ~/.conky/clock-cuckoo2.wav")
		os.popen(notifier)
	'''Formatting for autocentering inside mail block'''	
	if total >=3:
		posit = '-8'
	elif total ==2:
		posit = '-1'
	elif total ==1:
		posit = '6'
	else:
		posit = '13'
	'''Print out with conky formatting'''
	print '${voffset '+posit+'}${goto 92}'+uname+'@gmail.com:'+'${font Ubuntu:style=Bold:size=9}${color1} %s new email(s)${font}${color}' % (len(atom.entries))
	for i in range(min(len(atom.entries), maxlen)):
		print '${goto 105}${font Ubuntu:style=Bold:size=9}${color1}%s${font}${color}' % atom.entries[i].title
#uncomment the following line if you want to show the name of the sender
#		print '          ${color2}%s' % atom.entries[i].author
	if len(atom.entries) > maxlen:
		print '${goto 105}more...'
	'''Update the count'''	
	count=open('gmail_count', "w")
	data = (len(atom.entries))
	data = count.write (str(data))
	count.close ()

if __name__ == "__main__":
	file = open('gmail_count')
	cnt = int(file.read())
	file.close()
	f = auth()  # Do auth and then get the feed
	readmail(f, int(maxlen)) # Let the feed be chewed by feedparser


