import flask
from flask import request, jsonify
import requests
from datetime import date
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = False

def ask_apiwl(nip):
	today = date.today()
	today_date = today.strftime("%Y-%m-%d")
	address = "https://wl-api.mf.gov.pl/api/search/nip/" + nip + "?date=" + str(today_date)
	response_raw = requests.get(address)
	response = response_raw.json()
	company_info = {}
	company_info['regon'] = response['result']['subject']['regon']
	company_info['krs'] = response['result']['subject']['krs']
	company_info['name'] = response['result']['subject']['name']
	company_info_json = json.dumps(company_info)
	return company_info_json


@app.route('/check/<string:key>/', methods = ['GET'])
def check_company_info(key):
    response = ask_apiwl(key)
    return jsonify(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=33303, debug=True)
