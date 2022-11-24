from flask import Flask, request
from dataManager import DataManager
import json

app = Flask(__name__)


dm = DataManager()

@app.route("/filterDataBy", methods=['POST'])
def parse_data():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = dm.parse_arguments(request.get_json())
        return data
    else:
        return 'Content-Type not supported!'

@app.route("/getTop", methods=['GET','POST'])
def get_all_data():
    if request.method == 'POST':
        if (request.headers.get('Content-Type') == 'application/json'):
            return dm.get_top_total_comments(request.get_json()["data"])
        else:
            return 'Content-Type not supported!'
    else:
        __init_data = dm.get_top_total_comments()
        if __init_data is not None:
            response = app.response_class(
                response=json.dumps(__init_data),
                status=200,
                mimetype='application/json'
            )
            return response
        else:
            response = app.response_class(
                response=json.dumps({"code":"3", "message":"Internal error."}),
                status=405,
                mimetype='application/json'
            )
            return response

if __name__ == "__main__":
    app.run()