import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/companyinfocorectness', methods = ['POST'])
def company_info_corectness():
    content_json = request.json
    content = json.loads(content_json)
    
    nip1 = content['nip1']
    regon1 = content['regon1']
    krs1 = content['krs1']
    name1 = content['name1']
    nip2 = content['nip2']
    regon2 = content['regon2']
    krs2 = content['krs2']
    name2 = content['name2']
    response = {}
    if(name1 == name2 and nip1 == nip2 and regon1 == regon2 and krs1 == krs2):
    	response['response'] = 'True' 
    else:
    	response['response'] = 'False'
    response_json = json.dumps(response)
    return jsonify(response_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=33301, debug=True)
