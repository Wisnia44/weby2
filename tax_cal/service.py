import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/tags', methods = ['POST'])
def tax():
    source_json = request.json
    source = json.loads(source_json)
    tax_list={}
    for i in source['line_items']:
        tax_list[i['description']]=round(1-i['price']/i['total'],2)
    return jsonify(tax_list_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=33308, debug=True)
