from flask import Flask

APP = Flask(__name__)


@APP.route('/get_job')
def get_job():
    return {
        "docketId": "CMS-2014-0115"
    }
