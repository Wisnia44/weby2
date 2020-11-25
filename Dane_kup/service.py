import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/vendorinfo', methods = ['POST'])
def get_data():
    source_json = request.json
    source = json.loads(source_json)
    dane={}
    dane['nip'] =source['vat_number']
    dane['name'] = source['vendor']['name']
    dane['address'] = source['vendor']['address']
    dane['vendorinfo'] = source['vendor']
    dane_json = json.dumps(dane)
    return jsonify(dane_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=33306, debug=True)
