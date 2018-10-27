import requests

URL = "http://localhost:7000/api/shorturl/new"

def validJsonRequest():
    req = {"original_url":"http://google.com"}
    r = requests.post(URL, json = req)
    if r.status_code != 200:
        raise Exception("Invalid response status code")
    if r.json()['original_url'] != req['original_url']:
        raise Exception("Invalid original url")
    return r.json()

def checkIfShortened():
    res = validJsonRequest()
    r = requests.get(res['short_url'])
    if r.status_code != 200:
        raise Exception("Invalid response status code")
    print r.text

def invalidURL():
    req = {"original_url":"4535353535"}
    r = requests.post(URL, json = req)
    if not r.json()['error']:
        raise Exception("Expected error")
    return r.json()

if __name__ == '__main__':
    validJsonRequest()
    checkIfShortened()
    invalidURL()