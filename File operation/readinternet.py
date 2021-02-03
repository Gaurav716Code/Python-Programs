def readfrominternet():
    import urllib.request
    response = urllib.request.urlopen('https://www.google.com')
    lines = response.readlines(2000)
    print(lines)

readfrominternet()
