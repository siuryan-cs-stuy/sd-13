from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

API_KEY = 'IO2j5bRnvBBOA915Appc2wSsM0fZt59vHoQ5gCug'

@app.route('/')
def index():
    u = urllib2.urlopen('https://api.nasa.gov/planetary/apod?api_key=' + API_KEY)
    json_string = u.read()
    potd = json.loads(json_string)
    return render_template('index.html', potd = potd)

if __name__ == '__main__':
    app.debug = True
    app.run()
