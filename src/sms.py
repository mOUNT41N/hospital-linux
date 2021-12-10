import json
import random
import re
import requests
import time

from flask import Blueprint, jsonify

sms_dict = {}
app_key = "7ef401198a3414cd5542679c2e2b09a7"
sms_url = "http://v.juhe.cn/sms/send"

bp = Blueprint('sms', __name__, url_prefix='/sms')
@bp.route('/<phone_number>/')
def sms(phone_number):
    if not (len(phone_number) == 11 and re.match(r"\d{11}", phone_number)):
        return jsonify({"error_code": 1, "reason": "invalid phone number"})
    if phone_number in sms_dict and time.time() - sms_dict[phone_number]["time"] < 60:
        return jsonify({"error_code": 2, "reason": "interval less than one minute"})
    captcha = rand_num(6)
    payload = {"mobile": phone_number,
               "tpl_id": 148966,
               "tpl_value": "#code#=" + captcha,
               "key": app_key}
    res = requests.get(sms_url, payload)
    info = json.loads(res.text)
    if info["error_code"] != 0:
        return info
    else:
        sms_dict[phone_number] = {"time": time.time(), "captcha": captcha}
        return jsonify({"error_code": 0, "captcha": captcha})


def rand_num(digit_num):
    rst = ""
    for i in range(digit_num):
        rst += chr(48 + random.randint(0, 9))
    return rst
