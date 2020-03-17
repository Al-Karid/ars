import flask
from collections import defaultdict
from flask import request, jsonify
from ars.api.recomsys import recommendations
from ars.api.recomsys import get_8_random_movies

app = flask.Flask(__name__)
app.config["DEBUG"] = True

print("Starting server...")

req = defaultdict(list)

# Create some test data for our catalog in the form of a list of dictionaries.
@app.route('/', methods=['GET'])
def home():
    if 'm' in request.args:
        m = request.args['m']
        r = recommendations(m.lower())
        if (r!=0):
            req["status"] = 1
            req["data"] = r
            return jsonify(req)
        else:
            req["status"] = 0
            return jsonify(req)
    else:
        return "Error: No id field provided. Please specify an m param."


# A route to return all of the available entries in our catalog.
@app.route('/random', methods=['GET'])
def random():
    return get_8_random_movies()

def run():
    app.run()