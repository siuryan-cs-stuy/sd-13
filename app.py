from flask import Flask, render_template, request
import urllib2
import urllib
import json

app = Flask(__name__)

NASA_API_KEY = 'IO2j5bRnvBBOA915Appc2wSsM0fZt59vHoQ5gCug'
WA_API_KEY = '2VHUGQ-LJRRRP3AAU'

@app.route('/')
def index():
    u = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + NASA_API_KEY)
    json_string = u.read()
    potd = json.loads(json_string)

    query = None
    if request.args:
        params = {'i': request.args['q'], 'appid': WA_API_KEY}
        query_args = urllib.urlencode(params)
        print query_args
        u = urllib2.urlopen('http://api.wolframalpha.com/v1/result?' + query_args)
        query = u.read()

    return render_template('index.html', potd = potd, query = query)

if __name__ == '__main__':
    app.debug = True
    app.run()
