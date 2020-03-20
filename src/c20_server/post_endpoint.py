from flask import Flask, request


APP = Flask(__name__)


@APP.route('/return_result', methods=['POST'])
def return_result():
    json_data = request.json
    if json_data is None:
        return{}, 400

    return {}, 200
