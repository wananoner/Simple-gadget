import urllib.request

response = urllib.request.urlopen("http://placekitten.com/g/500/600")
cat = response.read()

with open('E:\car.jpg', 'wb') as f:
    f.write(cat)
