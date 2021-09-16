def download(filePath,symbol):
    from crumbSource import download

    data = download(symbol)
    with open(filePath,"wb") as output:
        output.write(bytearray(data))
    print data