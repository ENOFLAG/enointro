######## HTTP Requests ################################################################
import requests

# simple GET request with timeout, full state saved in response
response = requests.get("https://api.github.com", timeout=1)
# check status
if response.status_code == 200:
    print('Success!')
# check (specific) headers
response.headers['Content-Type']
# retrieve HTML content as string
response.text
# get dictionary from JSON content
deserialized = response.json()
# pass GET parameters or headers as dictionaries
requests.get("https://api.github.com/search/repositories",
    params={'q': "requests+language:python"},
    headers={'Accept': "application/vnd.github.v3.text-match+json"},
)
# login via HTTP Basic Auth
requests.get('http://example.com/member_area', auth=('username', 'password'))
# HTTP POST (e.g. to submit form data when logging in) and supply a cookie
response = requests.post("http://example.com/login", 
    data={'user': 'name', 'password': 'value'},
    cookies={'ENOwiki_session': '17ab96bd8ffbe8ca58a78657a918558'}
)
# check cookies in response
cookie_dict = dict(response.cookies)


######## Socket Communication with TelnetLib ############################################
#
# (these things can also easily be done with our favorite swiss army tool: pwntools.
# Docs: http://docs.pwntools.com/en/stable/tubes.html , http://docs.pwntools.com/en/stable/tubes/sockets.html)

import telnetlib as tl

# open a new connection 
s = tl.Telnet("10.10.10.10", 1337)
# receive at least one byte, if nothing is available, block and wait; returns byte string
r = s.read_some()
# receive until byte string (in this case: newline) is matched
r = s.read_until(b'\n')
# send bytes
s.write(b"Hello, World!\x00")
# get an interactive session
s.interact()
# for good measure, close the connection gracefully
s.close()


######## Basic String/Byte Operations ####################################################

# string concatenation
a = "con" + "cat"
# get length of string
len(a) # 6
# reverse a string
a[::-1] # 'tacnoc'
# replace chars (in this case: delete them)
a.replace("c", "") #  this does not alter the original string (a)
# get a list of words, split on parameter (defaults to whitespaces (e.g. spaces or newlines))
a.split("c") # ['', 'on', 'at']
# make byte string from string (two different types in python3, sockets usually expect bytes)
a.encode()
# many string operations work on byte strings as you would expect
len(a.encode()) # 6
# get string from byte string (only works for correct UTF-8 encoding)
b"hello".decode()   # works
b"he\xc1o".decode() # does not work
# get ASCII hex representation from byte string
x = b"\x40\x00\x1b\xff".hex() # '40001bff'
# convert hex string to integer (if you omit the second param, it defaults to base 10, the usual decimal representation)
int(x, 16)
