from flask import Flask, request

APP = Flask(__name__)


@APP.route('/get_job')
def get_job():
    return {
        "docketId": "CMS-2014-0115"
    }


@APP.route('/return_result', methods=['POST'])
def return_result():
    json_data = request.json
    if json_data is None:
        return{}, 400
    return {}, 200
