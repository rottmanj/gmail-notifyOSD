Dependencies needed:
python-feedparser
python-notify
python-media (pymedia)
gtk2-engines-pixbuf
python-keyring-gnome (gnome) or python-keyring-kwallet (kde) depending on which one you use

To add your account info to the keyring:
user@domain:~$ python
 Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41) 
 [GCC 4.4.3] on linux2
 Type "help", "copyright", "credits" or "license" for more information.
 >>> import keyring
 >>> keyring.set_password("gmail", "username@gmail.com", "secret")
