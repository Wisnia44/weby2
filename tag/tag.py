import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/tags', methods = ['POST'])
def tag():
    source_json = request.json
    source = json.loads(source_json)
    tag=[]
    tag.append(source['created'])
    tag.append(source['invoice_number'])
    tag.append(source['total'])
    tag.append(source['bill_to_name'])
    return jsonify(tag_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=33307, debug=True)
