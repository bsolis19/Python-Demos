import httplib

conn = httplib.HTTPSConnection("www.google.com")
conn.request("GET", "/")
response = conn.getresponse()
print response.status