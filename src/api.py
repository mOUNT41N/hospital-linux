from flask import Blueprint, request, jsonify, send_from_directory
import db
from utility import md5_hash, require_login
import random

bp = Blueprint('app', __name__, url_prefix='/api')
SALT = "qazwsx"
@bp.route('/user_info/<user_phone>/', methods=["get", "post"])
def user_info(user_phone):
    with db.cur() as cursor:
        if request.method == "GET":
            sql = "select * from patient where user_phone=%s"
            data = (user_phone, )
            cursor.execute(sql % data)
            rst = cursor.fetchone()
            return jsonify({"status": 0, "data": {k: rst[k] for k in rst}})
        else:
            key_words = [key for key in request.form]
            place_holder = [key+"='%s'" for key in key_words]
            sql = "update patient set " + ", ".join(place_holder) + " where user_phone=%s"
            # data = [request.form[key] for key in request.form]
            data = [request.form[key] for key in request.form]
            data.append(user_phone)
            data = tuple(data)
            cursor.execute(sql % data)
            return jsonify({"status": 0})


@bp.route('/diagnosis/<phone_number>/')
def diagnosis(phone_number):
    pass


@bp.route('/blood_sugar/<phone_number>/', methods=["get", "post"])
def blood_sugar(phone_number):
    with db.cur() as cursor:
        if request.method == "GET":
            sql = "select blood_sugar_time, blood_sugar_number from blood_sugar where blood_sugar_phone=%s"
            cursor.execute(sql % phone_number)
            data = cursor.fetchall()
            return jsonify({"status": 0, "data": {"blood_sugar_time": [str(item["blood_sugar_time"]) for item in data],
                            "blood_sugar_number": [item["blood_sugar_number"] for item in data]}})
        else:
            sql = "insert into blood_sugar (blood_sugar_phone, blood_sugar_time, blood_sugar_number) values('%s', '%s', %s)"
            cursor.execute(sql % (phone_number, request.form["blood_sugar_time"], request.form["blood_sugar_number"]))
            return jsonify({"status": 0})


@bp.route('/register/<user_phone>/', methods=["post"])
def register(user_phone):
    with db.cur() as cursor:
        sql = "select count(user_phone) from patient where user_phone='%s'"
        cursor.execute(sql % user_phone)
        if cursor.fetchone()['count(user_phone)'] != 0:
            return jsonify({"status": 1, "reason": "user already exists"})
        sql = "insert into patient(user_phone, user_passwd) values('%s', '%s')"
        cursor.execute(sql % (user_phone, md5_hash(SALT+request.form["passwd"])))
        return jsonify({"status": 0})


@bp.route('/login/<user_phone>/', methods=["post"])
def login(user_phone):
    with db.cur() as cursor:
        sql = "select count(user_phone) from patient where user_phone='%s'"
        cursor.execute(sql % user_phone)
        if cursor.fetchone() == 0:
            return jsonify({"status": 1, "reason": "user didn't register"})
        sql = "select user_passwd from patient where user_phone='%s'"
        cursor.execute(sql % user_phone)
        if cursor.fetchone()["user_passwd"] != md5_hash(SALT+request.form["passwd"]):
            return jsonify({"status": 1, "reason": "wrong passwd"})
        sql = "insert into login(user_phone) values('%s')"
        cursor.execute(sql % user_phone)
        return jsonify({"status": 0})


@bp.route('/ages/')
@require_login
def ages():
    with db.cur() as cursor:
        sql = "select nianling from chapter1 where id in (select id from suifang where sequence=1)"
        cursor.execute(sql)
        data = {"ages": []}
        for i in range(1000):
            data["ages"].append(str(random.randint(0, 100)))
        # return jsonify(data)
        return jsonify({"ages": [item["nianling"] for item in cursor.fetchall()]})


@bp.route('/tags/')
@require_login
def tags():
    with db.cur() as cursor:
        sql = "select tag from suifang where sequence=1"
        cursor.execute(sql)
        return jsonify({"tags": [item["tag"] for item in cursor.fetchall()]})

@bp.route('/pdf_html/<id>/')
def get_html(id):
    id = int(id)
    with db.cur() as cursor:
        cursor.execute("select * from feed where feed_file_timestamp > %s order by feed_file_timestamp desc" % id)
        data = cursor.fetchall()
        return jsonify({"feed_title": [item["feed_title"] for item in data],
                        "feed_description": [item["feed_description"] for item in data],
                        "feed_file_timestamp": [item["feed_file_timestamp"] for item in data]})