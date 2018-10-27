# url-shortener
Simple URL shortener using Python and redis

## Requirements
`pip install redis requests flask flask-restful`

Can be modeled with a microservices approach such that the shortener generates tokens which are permutations of characters periodically depending on the number of URLs added to the redis keystore.

Start with `python run.py`

`/api/shorturl/new`

Request: `{"original_url":"http://google.com"}`

Response: `{
  "original_url": "http://google.com",
  "short_url": "http://localhost:7000/EhNkb"
}`

`/api/shorturl/custom`

Request: `{"original_url":"http://google.com", "customToken": "google"}`

Response: `{
  "original_url": "http://google.com",
  "short_url": "http://localhost:7000/google"
}`

Tests are in the `tests` folder
