from urllib import request


def handle(index, frame, size):
    percent=100*index*frame//size
    print(str(percent)+"%")

url="https://codeload.github.com/Sommerregen/grav-theme-zsimplex/legacy.zip/v2.2.1"
path="abc.zip"
request.urlretrieve(url, path, handle)
