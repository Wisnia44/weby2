#serwer
import flask
from flask import request, jsonify
#api ocr
from veryfi import Client
#json
import json
#download
import urllib.request
#pdf to jpg
from pdf2image import convert_from_path
#delete file
import os

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# get your keys here: https://hub.veryfi.com/api/
client_id = 'vrfLoNznIGEpybDY14dAPAtFM2SVramJRJSHJca'
client_secret = 'Rh0jOMOr0UV8B0EOJ18ewEfOhmjwue8FLzzrBieCBdCMy9mtuCbdLUmLmmzyPTMjeDnBDAVAohvicOLgY1FwYolJor27duA1l4fP3KNj6ovrnl5MlukNINnhvTaPmziu'
username = 'danior909'
api_key = '56452bf786b2746e6f9730ac552e733d'
veryfi_client = Client(client_id, client_secret, username, api_key)

def download_file(url):
    urllib.request.urlretrieve(url, './ocr/temp/file.pdf')

def to_jpg():
    #poppler_path =r'.\ocr\poppler-20.11.0\bin'
    pages = convert_from_path('./ocr/temp/file.pdf', 500)
    for page in pages:
        page.save('./ocr/temp/file2.png', 'PNG')

def OCR():
    file_path='./ocr/temp/file2.png'
    categories = ['Grocery', 'Utilities', 'Travel']
    # This submits document for processing (takes 3-5 seconds to get response)
    document_json = veryfi_client.process_document(file_path, categories=categories)
    return (document_json)

def del_temp():
    os.remove("./ocr/temp/file2.png")
    os.remove("./ocr/temp/file.pdf")

@app.route('/ocr', methods = ['POST'])
def run_program():
    url_json = request.json
    url = json.loads(url_json)
    download_file(url['url'])
    to_jpg()
    response={}
    response['response'] = OCR()
    del_temp() 
    response_json = json.dumps(response)
    return jsonify(response_json)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=33305, debug=True)
