from flask import Flask, request, redirect
from flask_restful import Resource, Api
from handlers.shortener import Shortener
from handlers.store import RedisWrapper
import urlparse

app = Flask(__name__)
api = Api(app)

shorten = Shortener()
shorten.genPermutations()
store = RedisWrapper()
store.initRedis()

@app.route("/<short>")
def redirectShortURL(short):
    value = store.get(short)
    print value
    return """
    <html><head><meta http-equiv="refresh" content="0; url={0}" /></head></html>
    """.format(value)

class URLShortner(Resource):
    #API that will return the shortened URL
    def post(self):
        json_data = request.get_json(force=True)
        original_url = json_data['original_url']
        #TODO: parse url to remove slash so that including that
        #won't change the token
        
        shortURL = store.get(original_url)

        if shortURL:
            return {"original_url": original_url, "short_url":"http://localhost:7000/{0}".format(shortURL)}
        else:
            shortToken = shorten.getURLToken()
        
        if shorten.checkIfValid(original_url):
            store.insert(original_url, shortToken)
            store.insert(shortToken, original_url)
        else:
            return {"error":"invalid url"}
        
        response = {"original_url": original_url, "short_url":"http://localhost:7000/{0}".format(shortToken)}
        return response

class CustomURL(Resource):
    #API that will return the shortened URL
    def post(self):
        json_data = request.get_json(force=True)
        original_url = json_data['original_url']
        customToken = json_data['customToken']
        #TODO: parse url to remove slash so that including that
        #won't change the token
        
        shortURL = store.get(original_url)

        if shortURL:
            return {"original_url": original_url, "short_url":"http://localhost:7000/{0}".format(shortURL)}
        
        if shorten.customShortURL(original_url, customToken) and shorten.checkIfValid(original_url):
            store.insert(original_url, customToken)
            store.insert(customToken, original_url)
        else:
            return {"error":"invalid url"}
        
        response = {"original_url": original_url, "short_url":"http://localhost:7000/{0}".format(customToken)}
        return response

api.add_resource(URLShortner, '/api/shorturl/new')
api.add_resource(CustomURL, '/api/shorturl/custom')

if __name__ == '__main__':
    app.run(debug=True, port = 7000, host='0.0.0.0')