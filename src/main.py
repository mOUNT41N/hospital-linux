# coding=utf8
# import ast
import csv
import datetime
# import json
import os
import time
from urllib import parse

import flask
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import request
from flask import send_file
from flask import session
# from pyecharts import options as opt
# from pyecharts.charts import Bar
# from pyecharts.charts import Line
from pyecharts import Line
from PIL import Image

import logging
# import sys
import api
import db
import questions
import sms
import zipfile
# import codecs
from utility import require_login, md5_hash
from urllib.parse import quote
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

# reload(sys)
# sys.setdefaultencoding('utf8')

app = Flask(__name__)
# app = flask.Flask(__name__)
app.config.from_object("settings")
app.register_blueprint(sms.bp)
app.register_blueprint(api.bp)
# app.secret_key = "2017140836"
app.secret_key = "2018211620"
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = (['pdf'])


# 主页,显示需要通知下一次的随访记录
@app.route('/')
@require_login
def index():
    with db.cur() as cursor:
        cursor.execute("set sql_mode='';")
        # sql = "select * from suifang"
        # sql = '''select * from (select suifang.* from suifang join
        # (select id_number, max(sequence) as sequence from suifang group by id_number) as last
        # on suifang.id_number = last.id_number and suifang.sequence = last.sequence) as rst
        # where (sequence = 1 and datediff(now(), time_stamp) > 1) or
        # (sequence = 2 and datediff(now(), time_stamp) > 2) or (sequence = 3 and datediff(now(), time_stamp) > 3);'''

        # sql = '''select * from (select suifang.* from suifang natural join
        #         (select id_number, max(sequence) as sequence from suifang group by id_number) as last ) as rst
        #         where (sequence = 1 and datediff(now(), time_stamp) > 1) or
        #         (sequence = 2 and datediff(now(), time_stamp) > 2) or (sequence = 3 and datediff(now(), time_stamp) > 3);'''

        sql = '''select * from (select suifang.* from suifang natural join 
                        (select id_number, max(sequence) as sequence from suifang group by id_number) as last ) as rst;'''
        cursor.execute(sql)
        data = cursor.fetchall()
    # #print(data)
    send_data = []
    for i in range(len(data)):
        if data[i]['time_stamp2'] is not None:
            if (data[i]['time_stamp2'] - datetime.datetime.now()).days < 30:
                #                #print(data[i]['name'], " ", data[i]['time_stamp2'])
                send_data.append(data[i])
        # else:
        #     now = datetime.datetime.now()
        #     delta = datetime.timedelta(days=3)
        #     n_days = now + delta
        #     data[i]['time_stamp2'] = n_days.strftime('%Y-%m-%d %H:%M:%S')
        #     send_data.append(data[i])

    sd = sorted(send_data, key=lambda e: e.__getitem__('time_stamp2'), reverse=False)
    chapter_name = questions.chapter_name
    survey_info = questions.survey_info
    return render_template("index.html", data=sd, survey_info=survey_info, chapter_name=chapter_name)
    # return render_template("uploadimg.html", data=sd, survey_info=survey_info, chapter_name=chapter_name)


# 模糊查询
@app.route('/add_survey/fuzzysearch/', methods=["get", "post"])
# @require_login
def fuzzysearch():
    if request.method == "POST":
        cusname = request.form.get("cusname")
        # #print(type(cusname))
        # cusname.join('%')
        sql = "select name, id_number, phone from suifang where name like '%%%s%%' " % cusname

        with db.cur() as cursor:
            cursor.execute(sql)
            name = cursor.fetchall()
        # 方案1: name 是[{}]的形式，我们将其中字典的每个值取出放入一个集合中
        # #print(name)
        templist = []
        for i in range(len(name)):
            temp = list(name[i].values())
            # #print(temp)
            # #print(temp.values())
            for j in range(len(temp)):
                templist.append(temp[j])
        # #print(templist)
        name = list(set(templist))
        # #print("name", name)
        # #print("res:", res)

        # # 方案2： 把字典传过去，然后让前端取出对应的值 用datalist展示选择
        # #print(name)
        return jsonify(name)
    if request.method == "GET":
        return "fuzzysearch!!"


# 登录页
@app.route('/login/', methods=["get", "post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        if request.form["username"] == app.config["SU_USER"] and request.form["passwd"] == md5_hash(
                app.config["SU_PASSWD"]):
            session["username"] = request.form["username"]
            return redirect("/")
        else:
            return redirect("/login/")


# 添加一条随访记录 姓名,身份证号,电话,第几次随访,时间戳(自动插入)
# 需求添加2021 10 11 录入界面，添加随访方面简化，以姓名作为首要条件，重名患者身份证号，电话辅助识别，随访次数系统自动生成
@app.route('/add_survey/', methods=["get", "post"])
@require_login
def add_survey():
    if request.method == "GET":
        return render_template("add_survey.html")
    else:
        # 提交的时间
        temptime = request.form['time']
        temptime = temptime.replace("T", ' ')
        # 将提交的时间转换为可计算的时间
        time_stamp = datetime.datetime.strptime(temptime, '%Y-%m-%d %H:%M')

        temptime2 = request.form['time2']
        temptime2 = temptime2.replace("T", ' ')
        time_stamp2 = datetime.datetime.strptime(temptime2, '%Y-%m-%d %H:%M')
        number = request.form['id_number']
        birthday = number  # 出生年月日
        birthday = birthday.replace("-", '')
        birth_year = birthday[0:4]  # 前四位
        age = datetime.datetime.now().year - int(birth_year)  # int换算

        # age = int(age)
        # #print(time_stamp)
        with db.cur() as cursor:
            # sql = "select name, id_number, phone from suifang"
            # cursor.execute(sql)
            # data = cursor.fetchall()
            # #print(data)
            # for i in range(len(data)):
            #     if data[i]['name'] == request.form["name"]:
            #         if data[i]['id_number'] == request.form["id_number"]:
            #             #print("name:", request.form["name"])
            #             break
            # else:
            #     #print("There is new man:", request.form["name"])
            sql = "select id,name, id_number, phone, sequence from suifang"
            cursor.execute(sql)
            data = cursor.fetchall()
            # #print(data)
            # maxsequence = 0
            # flag = 0
            # 从后向前遍历可以直接获得 最近一次的随访记录
            for i in range(len(data) - 1, -1, -1):
                if data[i]['name'] == request.form["name"]:
                    if data[i]['id_number'] == request.form["id_number"]:  # 原来就有这个人
                        # #print("name:", request.form["name"])
                        sql = "insert into suifang (name, id_number, phone, sequence, time_stamp, docter_name, time_stamp2, nianling) values ( '%s', '%s', '%s', '%d', '%s', '%s', '%s', '%d')"
                        cursor.execute(
                            sql % (
                                request.form["name"], request.form["id_number"],
                                request.form["phone"],
                                data[i]['sequence'] + 1, time_stamp,
                                request.form["docter_name"], time_stamp2, age))
                        sql = "select * from chapter1 where id = %s" % data[i]['id']
                        cursor.execute(sql)
                        info = cursor.fetchone()
                        print("info:", info)
                        cursor.execute("select MAX(id) from suifang")
                        maxid = cursor.fetchone()
                        print("maxid", maxid)
                        tempdata = []
                        fields = ""
                        format_ = ""
                        if info is not None:
                            for k in info:
                                if info[k] is not None and info[k] != '':
                                    if type(info[k]) == type(1):
                                        format_ += "'%d',"
                                    else:
                                        format_ += "'%s',"
                                    fields += k
                                    fields += ","
                                    if k == 'id':
                                        tempdata.append(maxid['MAX(id)'])
                                    else:
                                        tempdata.append(info[k])

                            print("info:", info)
                            print("fields", fields[:-1])
                            print("temdata:", tempdata)

                            sql = "replace into chapter1 "
                            #                            tempdata[0] = maxid['MAX(id)']
                            print(len(tempdata))
                            fields = fields[:-1]
                            format_ = format_[:-1]
                            print("format:", format_)
                            sql = (sql + "(" + fields + ")" + "values(" + format_ + ")") % tuple(tempdata)
                            print(sql)
                            cursor.execute(sql)
                        break
            else:  # 原来没有这个人
                # #print("There is new man:", request.form["name"])
                id_number = number + " "
                id_number = id_number + str(time_stamp).replace(" ", "")[0:10]
                # print(id_number)
                sql = "insert into suifang (name, id_number, phone,sequence, time_stamp, docter_name, time_stamp2, nianling) values ( '%s', '%s', '%s', '%d', '%s', '%s', '%s', '%d')"
                cursor.execute(
                    sql % (request.form["name"], id_number, request.form["phone"],
                           int(1), time_stamp,
                           request.form["docter_name"], time_stamp2, age))
        # #print("time:", request.form['time'])

        return redirect('/surveys/')


# 显示所有随访条目概览
@app.route('/surveys/')
@require_login
def surveys():
    N = 2
    with db.cur() as cursor:
        sql = "select * from suifang order by time_stamp desc"
        arg_dict = {}
        for k in request.args:
            arg_dict[k] = request.args[k]
        if "p" not in arg_dict:
            arg_dict["p"] = "1"
        if "name" in request.args:
            sql = "select * from suifang where name='%s' order by time_stamp desc" % arg_dict["name"]
        if "p" in request.args:
            sql += " limit %s, %s" % (N * (int(request.args["p"]) - 1), N)
        page_info = []
        start_page = int(arg_dict["p"])
        for i in range(max(1, start_page - 2), start_page):
            arg_dict["p"] = str(i)
            page_info.append({"link": parse.urlencode(arg_dict), "num": arg_dict["p"], "class": ""})
        arg_dict["p"] = start_page
        page_info.append({"link": parse.urlencode(arg_dict), "num": arg_dict["p"], "class": "active"})
        while len(page_info) < 5:
            arg_dict["p"] = str(int(page_info[-1]["num"]) + 1)
            page_info.append({"link": parse.urlencode(arg_dict), "num": arg_dict["p"], "class": ""})
        cursor.execute(sql)
        data = cursor.fetchall()
    chapter_name = questions.chapter_name
    survey_info = questions.survey_info
    return render_template("surveys.html", data=data, survey_info=survey_info, chapter_name=chapter_name,
                           page_info=page_info)


# 查看某一次随访的某一章的详情
@app.route('/survey/<survey_id>/<chapter_id>/', methods=["get", "post"])
@require_login
def survey_edit(survey_id, chapter_id):
    with db.cur() as cursor:
        if request.method == "GET":
            cursor.execute("select * from chapter" + chapter_id + " where id=" + survey_id)
            rst = cursor.fetchall()
            q = questions.chapters["chapter" + chapter_id]
            chapter_name = questions.chapter_name[int(chapter_id) - 1]
            if len(rst) == 0:
                return render_template("chapter_blank.html", q=q, chapter_name=chapter_name,
                                       id=survey_id, chapter_id=chapter_id)
                # return render_temp
            else:
                # #print("nice!")
                # TODO: number of checkbox items > 10 don't work
                return render_template("chapter.html", q=q, q_value=rst[0],
                                       chapter_name=chapter_name, id=survey_id, chapter_id=chapter_id)
        else:
            table_name = "chapter" + chapter_id
            q = [item for item in questions.chapters[table_name] if item["field"] in request.form]
            sql = "replace into %s " % table_name
            fields = "id, " + ", ".join([item["field"] for item in q])
            format_ = "'%d', "
            tmp = []
            for item in q:
                if item["type"] == 1:
                    tmp.append("'%s'")
                elif item["type"] == 0 or item["type"] == 2 or item["type"] == 3 or item["type"] == 5:
                    tmp.append("'%s'")
                elif item["type"] == 4 or item["type"] == 6 or item["type"] == 7 or item["type"] == 8 or item[
                    "type"] == 9:
                    tmp.append("'%s'")
                else:
                    continue
            format_ += ", ".join(tmp)
            data = [int(survey_id)]
            for item in q:
                if item["type"] == 2 or item["type"] == 5:
                    checked = request.form.getlist(item["field"])
                    data.append(' '.join([str(i) for i in checked]))
                elif item["type"] == 3:
                    data.append(request.form[item["field"]] or "1975-01-01")
                else:
                    data.append(request.form[item["field"]])

            if table_name == "chapter7":
                # data[46]存储的是路径 更改反斜杠
                # #print(data[46])
                # data[46].replace("\\\\", "/")
                # #print(data[46])
                temp_list = list(data[46])
                rep_list = ['\\\\' if x == '\\' else x for x in temp_list]
                # rep_list[0].replace('\u202a', '')
                # rep_list = ['' if x == '\\u202a' else x for x in rep_list]
                # rep_list.strip('\u202a')
                # if rep_list[0] == '\u202a':
                #     del rep_list[0]
                # #print("you 202a")
                # else:
                #      #print("meiyou")
                # #print(rep_list)
                data[46] = ''.join(rep_list)
                # data[46] = data[46].replace('\\u202a', '')
                data[46] = data[46].strip('\u202a')  # 去除不可见符号
                # #print(data[46])
            sql = (sql + "(" + fields + ")" + "values(" + format_ + ")") % tuple(data)
            cursor.execute(sql)
            #            #print("sql:", sql)
            # #print("fields:", fields)
            # #print("data:", data)
            if int(chapter_id) == 1:
                #                #print("chapterid==1",1)
                cursor.execute(
                    "select id from suifang where id_number = (select id_number from suifang where id = %s)" % survey_id)
                info = cursor.fetchall()
                # print("info:", info)
                idlist = []
                for i in range(len(info)):
                    idlist.append(info[i]["id"])
                #                #print("idlist", idlist)
                for i in range(len(idlist)):
                    # fields[0] = idlist[i]
                    sql = "replace into chapter1 "
                    data[0] = idlist[i]
                    # #print("fields:", fields)
                    # #print("data:", data, "datalen:", len(data))
                    sql = (sql + "(" + fields + ")" + "values(" + format_ + ")") % tuple(data)
                    #                    #print("sql:", sql)
                    cursor.execute(sql)

            # 疾病分组计算
            sql = "select niaobaidanbaijihang, xiaoshiniaodanbaidingliang,eGFR from chapter7 where id = %s" % survey_id
            cursor.execute(sql)
            info = cursor.fetchall()
            logging.warning(cursor)
            if not info:
                return redirect("/surveys/")
            #            logging.warning('infolen{}'.format((info)))
            niaobaidanbaijihang = info[0]["niaobaidanbaijihang"]
            xiaoshiniaodanbaidingliang = info[0]["xiaoshiniaodanbaidingliang"]
            eGFR = info[0]["eGFR"]
            print("eGFR:", eGFR)
            flag = 0
            # 早期
            if niaobaidanbaijihang and niaobaidanbaijihang != '' and xiaoshiniaodanbaidingliang and xiaoshiniaodanbaidingliang != '':
                if float(niaobaidanbaijihang) >= 30 and int(xiaoshiniaodanbaidingliang) <= 500:
                    print("tag is early")
                    flag = 1
                    # with db.cur() as cursor:
                    #     cursor.execute("select name,id_number from suifang where id = %s" % survey_id)
                    #     #print(cursor.fetchall())
                    with db.cur() as cursor:
                        cursor.execute("update suifang set tag = '早期' where id = %s " % survey_id)
            if xiaoshiniaodanbaidingliang and xiaoshiniaodanbaidingliang != '' and eGFR and eGFR != '':  # 中期
                if int(xiaoshiniaodanbaidingliang) >= 500 and float(eGFR) >= 30:
                    flag = 1
                    print("tag is mid")
                    with db.cur() as cursor:
                        cursor.execute("update suifang set tag = '中期' where id = %s " % survey_id)
            if eGFR and eGFR != '':  # 晚期
                if float(eGFR) < 30:
                    print("tag is late")
                    flag = 1
                    with db.cur() as cursor:
                        cursor.execute("update suifang set tag = '晚期' where id = %s " % survey_id)
            if flag == 0:
                print("tag is none")
                with db.cur() as cursor:
                    cursor.execute("update suifang set tag = '正常' where id = %s " % survey_id)
            # #print(tmp)
            # #print(tmp)
            # #print(data)

            # 判断 疾病分组标准
            return redirect("/surveys/")


# 上传图片路径
# @app.route('/survey/<survey_id>/<chapter_id>/uploadPicture', methods=["get", "post"])
# @require_login
# def upload_picture(survey_id, chapter_id):
#     with db.cur() as cursor:
#         if request.method == "POST":
#             table_name = "chapoter" + chapter_id
#             q = [item for item in questions.chapters[table_name] if item["field"] in request.form]
#             sql = "replace into %s" % table_name
#             fields =

# 自动生成eGFR的值
@app.route('/computer/survey/<survey_id>/', methods=["get", "post"])
@require_login
def auto_BMI(survey_id):
    with db.cur() as cursor:
        if request.method == "GET":
            # 取得性别
            cursor.execute("select xingbie from chapter1 where id='%s'" % survey_id)
            info = cursor.fetchone()
            # nianling = float(info["nianling"])
            if info is not None and info["xingbie"] is not None:
                xingbie = info["xingbie"]
            else:
                return "请填写性别"
                xingbie = None
            cursor.execute("select nianling from suifang where id = '%s'" % survey_id)
            # 取得年龄
            info = cursor.fetchone()
            nianling = info["nianling"]

            cursor.execute("select Scr from chapter7 where id='%s'" % survey_id)
            info = cursor.fetchone()
            if info is not None and info["Scr"] is not None:
                Scr = info["Scr"]
            else:
                return "请填写Scr"
                Scr = None

            #            #print("survey_id", survey_id)
            #            #print("xingbie:", xingbie)
            #            #print("nianling", nianling)
            #            #print("Scr", Scr)

            if xingbie is not None and nianling is not None and Scr is not None and xingbie != '' and nianling != '' and Scr != '':
                xingbie = int(xingbie)
                nianling = float(nianling)
                print("xingbie", xingbie)
                print("nianling", nianling)
                print("Scr", Scr)
                Scr = float(Scr) / 88.4
                b = -1.209
                c = 0.993
                if xingbie == 0:
                    k = 0.9
                    a = -0.411
                    eGFR = 141 * pow(min(Scr / k, 1), a) * pow(max(Scr / k, 1), b) * pow(c, nianling)
                else:
                    k = 0.7
                    a = -0.329
                    eGFR = 141 * pow(min(Scr / k, 1), a) * pow(max(Scr / k, 1), b) * pow(c, nianling) * 1.018
                eGFR = round(eGFR)
            else:
                return "请检查是否填写性别与Scr"
                eGFR = 0
            with db.cur() as cursor:
                # print("eGFR type:", type(eGFR))
                cursor.execute("update chapter7 set eGFR=%s where id=%s" % (eGFR, survey_id))
            return redirect("/surveys/")


# 个人历史信息曲线
@app.route('/charts/<name_id>/<survey_id>', methods=["get", "post"])
@require_login
def history_charts(name_id, survey_id):
    with db.cur() as cursor:
        if request.method == "GET":
            cursor.execute("select id_number from suifang where id=%s" % name_id)
            id_number = cursor.fetchone()
            ##print(id_number)
            # with db.cur() as cursor:
            #     cursor.execute("select * from suifang")
            #     info = cursor.fetchall()
            #     count_id = []
            #     data = []
            # for info_id in info:
            #     if name_yuan["name"] == info_id["name"]:
            #         count_id.append(info_id["id"])

            # 更新：解决重名问题
            with db.cur() as cursor:
                cursor.execute("select * from suifang where id_number = '%s'" % id_number["id_number"])
                info = cursor.fetchall()
                ##print("info", info)
                count_id = []
                data = []
                sequence = []
                i = 1
            for info_id in info:
                count_id.append(info_id["id"])
                sequence.append(str(i))
                i += 1
            #               sequence.append(str(info_id["sequence"]))
            for count in count_id:
                with db.cur() as cursor:
                    cursor.execute("select %s from chapter7 where id='%s'" % (survey_id, count))
                    zanshi = cursor.fetchone()[survey_id]
                    data.append(zanshi)
            #
            # #柱状图
            # bar = Bar()
            # # 添加柱状图的数据及配置项
            # bar.add_xaxis(count_id)
            # for a in questions.chapters["chapter7"]:
            #     if survey_id == a["field"]:
            #         b = a["zh-cn"]
            #         break
            # bar.add_yaxis(b, data)
            # bar.set_series_opts(markpoint_opts=opt.MarkPointOpts(data=[opt.MarkPointItem(type_="max", name="最大值"),
            #                                                            opt.MarkPointItem(type_="min", name="最小值")]),
            #                     markline_opts=opt.MarkLineOpts(data=[opt.MarkLineItem(type_="average", name="平均值")]))

            # 折线图
            line = Line()
            # 添加柱状图的数据及配置项

            #            line.add_xaxis(xaxis_data=sequence)
            for a in questions.chapters["chapter7"]:
                if survey_id == a["field"]:
                    b = a["zh-cn"]
                    break
            ##print(data)
            line.add(b, sequence, data, mark_point_symbol="diamond", mark_line=["max", "average", "min"],
                     is_label_show=True)
            #            line.add_yaxis(b, data)
            #            line.set_series_opts(markpoint_opts=opt.MarkPointOpts(data=[opt.MarkPointItem(type_="max", name="最大值"),
            #                                                                        opt.MarkPointItem(type_="min", name="最小值")]),
            #                                 markline_opts=opt.MarkLineOpts(data=[opt.MarkLineItem(type_="average", name="平均值")]))

            # 生成本地文件（默认为.html文件）
            line.render("./templates/mycharts.html")
            return render_template("mycharts.html")


# 导出勾选随访
@app.route('/download/partsurveys/', methods=['GET', 'POST'])
@require_login
def partsurveys_download():
    # with db.cur() as cursor:
    #     sql = "select id, name, sequence from suifang"
    #     cursor.execute(sql)

    # for chapter_index in questions.survey_info[0]:
    #     if chapter_index == 4 or chapter_index == 9:
    #         continue
    if request.method == 'GET':
        return redirect("/surveys/")
    if request.method == 'POST':
        ##print("DOWNLOAD POST!!!!!!!!\n\n\n\n")

        # #print("post:", end='')
        # data = request.form.get("2")
        # #print("data:", data, end="")

        # 获得最大随访id
        with db.cur() as cursor:
            cursor.execute("select MAX(id) from suifang")
            max_id = cursor.fetchone()
        max_num = max_id['MAX(id)']
        # #print(max_num)
        # 建立随访id表
        id_list = []
        out_list = []
        for i in range(max_num):
            id_list.append(i + 1)
        # 找到勾选项目 id 存放到out_list中
        for i in range(max_num):
            if request.form.get(str(i + 1)) != None:
                if id_list[i] == int(request.form.get(str(i + 1))):
                    out_list.append(i + 1)
            # data = request.form.get("3")
            # #print("data", i + 1, data)
        # #print("outlist:", out_list)
        # 初始化header
        header = ["患者姓名", "年龄", "身份证号", "电话", "随访次序", "疾病分组", "上次随访时间"]
        for chapter_index in questions.survey_info[0]:
            for q in questions.chapters["chapter" + str(chapter_index)]:
                if q["field"] == "id":
                    continue
                header.append(q["zh-cn"])
        # #print("header", header)

        data_list = []
        # 获取信息放入data
        for index in range(len(out_list)):
            tempData = []
            with db.cur() as cursor:
                cursor.execute(
                    "select name,nianling, id_number,phone,sequence,tag,time_stamp from suifang where id=%s" % out_list[
                        index])
                info = cursor.fetchone()
                tempData.append(info["name"])
                tempData.append(info["nianling"])
                tempData.append(info["id_number"])
                tempData.append(info["phone"])
                tempData.append(info["sequence"])
                tempData.append(info["tag"])
                tempData.append(info["time_stamp"])

            for chapter_index in questions.survey_info[0]:
                if chapter_index == 4 or chapter_index == 9:  # chapter4,9 的内容未定义 跳过
                    continue
                with db.cur() as cursor:
                    # cursor.execute("select * from chapter%s where id=%s" % (chapter_index, survey_id))
                    # index为所需要导出的随访的id
                    cursor.execute("select * from chapter%s where id=%s" % (chapter_index, out_list[index]))
                    chapter_dict = cursor.fetchone()
                for q in questions.chapters["chapter" + str(chapter_index)]:
                    if q["field"] == "id":
                        continue
                    # header.append(q["zh-cn"])
                    if chapter_dict is None or chapter_dict[q["field"]] is None:
                        tempData.append("")
                        continue
                    if q["type"] == 0 or q["type"] == 4 or q["type"] == 6 or q["type"] == 7 or q["type"] == 8 or q[
                        "type"] == 9:
                        tempData.append(chapter_dict[q["field"]])
                    elif q["type"] == 3:
                        tempData.append(str(chapter_dict[q["field"]]))
                    elif q["type"] == 1:
                        if chapter_index == 5:
                            tempData.append(chapter_dict[q["field"]] * 2)
                        else:
                            tempData.append(q["items"][chapter_dict[q["field"]]])
                    elif q["type"] == 2:
                        # #print(q["type"])
                        # #print(chapter_dict[q["field"]].split(" "))
                        checkbox_list = [int(i) for i in chapter_dict[q["field"]].split(" ")]
                        tempData.append("\n".join([q["items"][i] for i in checkbox_list]))
                    elif q["type"] == 5:
                        checkbox_list = [int(i) for i in chapter_dict[q["field"]].split(" ")[:-1]]
                        tempData.append("\n".join([q["items"][i] for i in checkbox_list]))
                        # #print(chapter_dict[q["field"]].split(" ")[-1])
                        # data.append(chapter_dict[q["field"]].split(" ")[-1])
                    else:
                        print("error")
            data_list.append(tempData)

        file_dir = os.path.join(basedir, app.config["DOWNLOAD_FOLDER"])
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file_name = os.path.join(file_dir, "部分选择" + ".csv")
        # csvfile = open(file_name, "w", encoding="utf-8")
        csvfile = open(file_name, "w", encoding="utf-8_sig")
        #        csvfile.write(codecs.BOM_UTF8)
        writer = csv.writer(csvfile)
        # writer.writerow(['\uFEFF'])
        writer.writerow(header)
        #        #print(header)
        for i in range(len(data_list)):
            writer.writerow(data_list[i])
        #            #print(data_list[i])
        # writer.writerow(data)
        csvfile.close()
        temp_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        temp_time = temp_time.replace(" ", "_")
        latinfilename = ("部分选择：" + str(temp_time) + ".csv").encode("utf-8").decode("latin1")
        #        file_name = quote(file_name)
        #        gunicornfilename = quote(str(temp_time) + ".csv")
        #        #print(gunicornfilename)
        #        return send_file(file_name, as_attachment=True, attachment_filename=gunicornfilename)
        return send_file(file_name, as_attachment=True, attachment_filename=latinfilename)
        return send_file(file_name, as_attachment=True, attachment_filename="部分选择：" + str(temp_time) + ".csv")
        # return redirect("/surveys/")


## 导出某一次随访
# @app.route('/download/survey/<survey_id>/')
# @require_login
# def survey_download(survey_id):
#    header = []
#    data = []
#    with db.cur() as cursor:
#        cursor.execute("select name, sequence from suifang where id=%s" % survey_id)
#        info = cursor.fetchone()
#        sequence = info["sequence"]
#
#    # 不根据随访次数显示部分信息，显示所有信息
#    sequence = 1
#    # 从数据库获取该次随访chapter1-7 的信息
#    for chapter_index in questions.survey_info[sequence - 1]:
#        if chapter_index == 4 or chapter_index == 9:  # chapter4,9 的内容未定义 跳过
#            continue
#        with db.cur() as cursor:
#            cursor.execute("select * from chapter%s where id=%s" % (chapter_index, survey_id))
#            chapter_dict = cursor.fetchone()
#        for q in questions.chapters["chapter" + str(chapter_index)]:
#            if q["field"] == "id":
#                continue
#            header.append(q["zh-cn"])
#            if chapter_dict is None or chapter_dict[q["field"]] is None:
#                data.append("")
#                continue
#            if q["type"] == 0 or q["type"] == 4 or q["type"] == 6 or q["type"] == 7 or q["type"] == 8 or q["type"] == 9:
#                data.append(chapter_dict[q["field"]])
#            elif q["type"] == 3:
#                data.append(str(chapter_dict[q["field"]]))
#            elif q["type"] == 1:
#                if chapter_index == 5:
#                    data.append(chapter_dict[q["field"]] * 2)
#                else:
#                    data.append(q["items"][chapter_dict[q["field"]]])
#            elif q["type"] == 2:
#                # #print(q["type"])
#                # #print(chapter_dict[q["field"]].split(" "))
#                checkbox_list = [int(i) for i in chapter_dict[q["field"]].split(" ")]
#                data.append("\n".join([q["items"][i] for i in checkbox_list]))
#            elif q["type"] == 5:
#                checkbox_list = [int(i) for i in chapter_dict[q["field"]].split(" ")[:-1]]
#                data.append("\n".join([q["items"][i] for i in checkbox_list]))
#                # #print(chapter_dict[q["field"]].split(" ")[-1])
#                # data.append(chapter_dict[q["field"]].split(" ")[-1])
#            else:
#                #print("error")
#
#    file_dir = os.path.join(basedir, app.config["DOWNLOAD_FOLDER"])
#    if not os.path.exists(file_dir):
#        os.makedirs(file_dir)
#    file_name = os.path.join(file_dir, str(survey_id) + ".csv")
##    csvfile = open(file_name, "w", encoding="utf-8")
#    #print("导出某一次随访")
#    #print(header)
#    #print(data)
#    csvfile = open(file_name, "w",encoding="utf-8_sig")
#    writer = csv.writer(csvfile)
##    writer.writerow(['\uFEFF'])
##    header.decode('GB2312').encode('utf-8')
##    header.decode('utf-8')
#    writer.writerow(header)
#
##    latindata = []
##    for i in range(len(data)):
##        latindata.append(data[i].decode("utf-8"))
##    writer.writerow(latindata)	
#    writer.writerow(data)
#    csvfile.close()
#    latinfilename = (info["name"] + str(sequence) + ".csv").encode("utf-8").decode("latin1")
#    return send_file(file_name, as_attachment=True, attachment_filename=latinfilename)
#    return send_file(file_name, as_attachment=True, attachment_filename=info["name"] + str(sequence) + ".csv")


# 导出全部随访
@app.route('/download/surveys/')
@require_login
def surveys_download():
    with db.cur() as cursor:
        sql = "select id, name, sequence from suifang"
        cursor.execute(sql)
        survey_ids = {item["id"]: [item["name"], item["sequence"]] for item in cursor.fetchall()}
    file_dir = os.path.join(basedir, app.config["DOWNLOAD_FOLDER"])
    os.system("rm -if %s/*" % file_dir)
    for survey_id in survey_ids:
        header = []
        data = []
        with db.cur() as cursor:
            cursor.execute("select name, sequence from suifang where id=%s" % survey_id)
            info = cursor.fetchone()
            sequence = info["sequence"]

        # 不根据随访次数显示部分信息，显示所有信息
        sequence = 1
        for chapter_index in questions.survey_info[sequence - 1]:
            if chapter_index == 4 or chapter_index == 9:
                continue
            with db.cur() as cursor:
                cursor.execute("select * from chapter%s where id=%s" % (chapter_index, survey_id))
                chapter_dict = cursor.fetchone()
            for q in questions.chapters["chapter" + str(chapter_index)]:
                if q["field"] == "id":
                    continue
                header.append(q["zh-cn"])
                if chapter_dict is None or chapter_dict[q["field"]] is None:
                    data.append("")
                    continue
                if q["type"] == 0 or q["type"] == 4 or q["type"] == 6 or q["type"] == 7 or q["type"] == 8:
                    data.append(chapter_dict[q["field"]])
                elif q["type"] == 3:
                    data.append(str(chapter_dict[q["field"]]))
                elif q["type"] == 1:
                    if chapter_index == 5:
                        data.append(chapter_dict[q["field"]] * 2)
                    else:
                        data.append(q["items"][chapter_dict[q["field"]]])
                elif q["type"] == 2:
                    checkbox_list = [int(i) for i in chapter_dict[q["field"]].split(" ")]
                    data.append("\n".join([q["items"][i] for i in checkbox_list]))
                elif q["type"] == 5:
                    checkbox_list = [int(i) for i in chapter_dict[q["field"]].split(" ")[:-1]]
                    data.append("\n".join([q["items"][i] for i in checkbox_list]))
                else:
                    print("error")
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        file_name = os.path.join(file_dir,
                                 "_".join([str(survey_id), survey_ids[survey_id][0], str(survey_ids[survey_id][1])])
                                 + ".csv")
        csvfile = open(file_name, "w")
        writer = csv.writer(csvfile)
        # writer.writerow(['\uFEFF'])
        writer.writerow(header)
        writer.writerow(data)
        csvfile.close()
    file_name = os.path.join(file_dir, "全部记录.zip")
    os.system("zip -j %s %s/*" % (file_name, file_dir))
    return send_file(file_name, as_attachment=True)


def header_data(survey_id):
    header = []
    data = []
    with db.cur() as cursor:
        cursor.execute("select name, sequence from suifang where id=%s" % survey_id)
        info = cursor.fetchone()
        sequence = info["sequence"]
    # 不根据随访次数显示部分信息，显示所有信息
    sequence = 1
    for chapter_index in questions.survey_info[sequence - 1]:
        if chapter_index == 4 or chapter_index == 9:
            continue
        with db.cur() as cursor:
            cursor.execute("select * from chapter%s where id=%s" % (chapter_index, survey_id))
            chapter_dict = cursor.fetchone()
        for q in questions.chapters["chapter" + str(chapter_index)]:
            if q["field"] == "id":
                continue
            header.append(q["zh-cn"])
            if chapter_dict is None or chapter_dict[q["field"]] is None:
                data.append("")
                continue
            if q["type"] == 0 or q["type"] == 4 or q["type"] == 6 or q["type"] == 7 or q["type"] == 8:
                data.append(chapter_dict[q["field"]])
            elif q["type"] == 3:
                data.append(str(chapter_dict[q["field"]]))
            elif q["type"] == 1:
                if chapter_index == 5:
                    data.append(chapter_dict[q["field"]] * 2)
                else:
                    data.append(q["items"][chapter_dict[q["field"]]])
            elif q["type"] == 2:
                checkbox_list = [int(i) for i in chapter_dict[q["field"]].split(" ")]
                data.append("\n".join([q["items"][i] for i in checkbox_list]))
            elif q["type"] == 5:
                checkbox_list = [int(i) for i in chapter_dict[q["field"]].split(" ")[:-1]]
                data.append("\n".join([q["items"][i] for i in checkbox_list]))
            else:
                print("error")
    return header, data


# 删除某一次随访
@app.route('/delete/survey/<survey_id>/')
@require_login
def survey_delete(survey_id):
    return "nop"


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload_pdf/', methods=["get", "post"])
@require_login
def upload_pdf():
    if request.method == "GET":
        return render_template("upload_pdf.html")
    else:
        file = request.files['pdf_file']
        if file and allowed_file(file.filename):
            t = int(time.time())
            file_dir = os.path.join(basedir, app.config["PDF_UPLOADER_FOLDER"])
            file_name = os.path.join(file_dir, str(t) + ".pdf")
            file.save(file_name)
            os.system("pdftohtml -c -s %s" % file_name)
            with db.cur() as cursor:
                sql = "insert into feed(feed_title, feed_description, feed_file_timestamp) values('%s', '%s', %s)"
                cursor.execute(sql % (request.form["title"], request.form["description"], t))
            return "ok"


@app.route('/statistic/', methods=["get"])
@require_login
def statistic():
    if request.method == "GET":
        return render_template("statistic.html")


# @app.route("/upload_row/", endpoint="upload_row", methods=["GET", "POST"])
# def upload_row():
#     # 文件对象保存在request.files上，并且通过前端的input标签的name属性来获取
#     fp = request.files.get("f1")
#     # 保存文件到服务器本地
#     fp.save("a.jpg")
#     return redirect(url_for("cms.index"))

@app.route('/docter/')
@require_login
def docter():
    sql = "select * from docter"
    with db.cur() as cursor:
        cursor.execute(sql)
        data = cursor.fetchall()
    return render_template("docter.html", data=data)


@app.route('/docter/add/', methods=['post', 'get'])
@require_login
def docter_add():
    if request.method == "GET":
        return render_template("docter_add.html")
    if request.method == "POST":
        # #print(request.form)
        # return redirect("/docter/")
        with db.cur() as cursor:
            sql = "insert into docter (docter_name, docter_phone) values ('%s', '%s')"
            cursor.execute(sql % (request.form['docter_name'], request.form['docter_phone']))
        return redirect("/docter/")


# 获取医生医生名字接口
@app.route('/get_docter/', methods=['post', 'geet'])
@require_login
def get_docter():
    if request.method == "GET":
        return "getdocter!!"
    if request.method == "POST":
        with db.cur() as cursor:
            sql = "select docter_name from docter"
            cursor.execute(sql)
            data = cursor.fetchall()
        return jsonify(list(data))


# 获取病人名字接口
@app.route('/get_customer/', methods=['post', 'geet'])
@require_login
def get_customer():
    if request.method == "GET":
        return "getcustomer!!"
    if request.method == "POST":
        with db.cur() as cursor:
            sql = "select name from suifang"
            cursor.execute(sql)
            data = cursor.fetchall()
        # #print(data)
        templist = []
        for i in range(len(data)):
            templist.append(data[i]['name'])
        # templist.sort()
        templist = list(set(templist))
        templist.sort()
        # #print(templist)
        return jsonify(templist)


# 获取病人电话接口
@app.route('/get_phone/', methods=['post', 'geet'])
@require_login
def get_phone():
    if request.method == "GET":
        return "getphone!!"
    if request.method == "POST":
        cusname = request.form.get("cusname")
        with db.cur() as cursor:
            sql = "select phone from suifang where name = '%s'" % cusname
            cursor.execute(sql)
            data = cursor.fetchall()
        templist = []
        for i in range(len(data)):
            templist.append(data[i]['phone'])
        templist = list(set(templist))
        templist.sort()
        return jsonify(templist)


# 获取病人身份证号
@app.route('/get_idnumbers/', methods=['post', 'geet'])
@require_login
def get_idnumbers():
    if request.method == "GET":
        return "getidnumbers!!"
    if request.method == "POST":
        cusname = request.form.get("cusname")
        with db.cur() as cursor:
            sql = "select id_number from suifang where name = '%s'" % cusname
            cursor.execute(sql)
            data = cursor.fetchall()
        templist = []
        for i in range(len(data)):
            templist.append(data[i]['id_number'])
        templist = list(set(templist))
        templist.sort()
        return jsonify(templist)


@app.route('/upload_img/', methods=['POST'])
@require_login
def upload_img():
    indexid = request.form['indexid']
    chapterid = request.form['chapterid']
    # #print(request.form['indexid'])
    # #print(request.form['chapterid'])
    imgfilename = str(indexid) + '_' + str(chapterid) + '.jpg'
    img = request.files.get('img')
    # #print('_img:', img)
    Basepath = os.path.abspath(os.path.dirname(__file__))
    # print("Basepath:", Basepath)
    path = Basepath + '/static/upload/'
    img_path = path + imgfilename
    # print("img_path", img_path)
    test_path = '../static/upload/' + imgfilename
    # #print("_img:", img)
    img.save(img_path)

    return jsonify({'signal': 1, 'img_path': test_path})


@app.route('/show_img/', methods=['POST'])
@require_login
def show_img():
    indexid = request.form['indexid']
    chapterid = request.form['chapterid']
    tempname = str(indexid) + '_' + str(chapterid) + '.jpg'
    # #print(request.form['indexid'])
    # #print(request.form['chapterid'])
    imgfilename = "/static/img/up2.png"
    Basepath = os.path.abspath(os.path.dirname(__file__))
    tempimgfilename = Basepath + '/static/upload/' + tempname
    # print(tempimgfilename)
    if os.path.exists(tempimgfilename):
        # print("Success!!!!!")
        return jsonify("/static/upload/" + tempname)
    else:
        print("Failure!!!")
    return jsonify(imgfilename)


@app.route('/uploadimg/<survey_id>/', methods=["get", "post"])
@require_login
def uploadimg(survey_id):
    if request.method == "GET":
        # #print("imghtml")
        return render_template("uploadimg.html", survey_id=survey_id)
    if request.method == "POST":
        # #print("uploadimg")
        imgfiles = list(request.files)
        with db.cur() as cursor:
            cursor.execute("select name, sequence, pic_num from suifang where id = '%s'" % survey_id)
            temp_dt = cursor.fetchone()
            pic_num = temp_dt["pic_num"]
            # 原来没有添加图片
            if pic_num is None:
                cursor.execute("update suifang set pic_num = %s where id = '%s'" % (len(imgfiles), survey_id))
                pic_num = len(imgfiles)
            else:
                cursor.execute(
                    "update suifang set pic_num = %s where id = '%s'" % ((len(imgfiles) + pic_num), survey_id))
                pic_num = len(imgfiles) + pic_num
            # #print(temp_name)
        basepath = os.path.abspath(os.path.dirname(__file__))
        # #print("Basepath", basepath)
        path = basepath + '/static/upload/'
        tempname = temp_dt["name"] + "第" + str(temp_dt["sequence"]) + "次随访"
        testpath = path + tempname + "/"
        # #print("testpath:", testpath)
        # #print(os.path.exists(testpath))
        if not os.path.exists(testpath):
            os.makedirs(testpath)
        # 图片存入服务器并压缩图片大小
        j = 0
        for i in range(pic_num - len(imgfiles), pic_num):
            img = request.files.get(imgfiles[j])
            j += 1
            imgfilename = str(i) + ".jpg"
            img_path = testpath + imgfilename
            # #print("img_path:", img_path)
            img.save(img_path)
            foo = Image.open(img_path)
            # foo = foo.resize((160, 300), Image.ANTIALIAS)
            foo = foo.convert("RGB")
            foo.save(img_path, optimize=True, quality=50)
            # #print(len(name))
    # return send_file(path + tempname + ".zip", as_attachment=True)
    return render_template("uploadimg.html")


@app.route('/downloadimg/<survey_id>/', methods=["get", "post"])
@require_login
def downloadimg(survey_id):
    if request.method == "GET":
        print("get download img")
    if request.method == "POST":
        # print("POST DOWNLOAD IMG")
        with db.cur() as cursor:
            cursor.execute("select name, sequence, pic_num from suifang where id = '%s'" % survey_id)
            temp_dt = cursor.fetchone()
            pic_num = temp_dt["pic_num"]
        basepath = os.path.abspath(os.path.dirname(__file__))
        # #print("Basepath", basepath)
        path = basepath + '/static/upload/'
        tempname = temp_dt["name"] + "第" + str(temp_dt["sequence"]) + "次随访"
        testpath = path + tempname + "/"
        # 测试压缩文件夹
        zip_file = zipfile.ZipFile(path + tempname + ".zip", 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(testpath):
            # #print(root)  # 当前目录路径
            # #print(dirs)  # 当前路径下所有子目录
            # #print(files)  # 当前路径下所有非目录子文件
            for tempfile in files:
                zip_file.write(root + tempfile, tempname + "/" + tempfile)
                # #print("tempfile:", tempfile)
        zipname = path + tempname + ".zip"
        # print("zipname:", zipname)
        zip_file.close()
        latinfilename = (tempname + '.zip').encode("utf-8").decode("latin1")
        return send_file(zipname, as_attachment=True, attachment_filename=latinfilename)


#        return send_file(zipname, as_attachment=True, attachment_filename=tempname + ".zip")
# return redirect("/uploadimg/%s" % survey_id)


@app.route('/medicalhistory/<survey_id>/', methods=["get", "post"])
@require_login
def medicalhistory(survey_id):
    sql = "select id from suifang where id = '%s'" % survey_id
    with db.cur() as cursor:
        cursor.execute(sql)
        data = cursor.fetchone()
    sql = "select * from medicalhistory where survey_id = '%s'" % survey_id
    with db.cur() as cursor:
        cursor.execute(sql)
        temp = cursor.fetchall()
        if len(temp) != 0:
            # data = {'id': temp["survey_id"]}
            data = temp
            data.sort(key=lambda x: x["starttime"], reverse=True)
            # print("hello")
    # return render_template("medicalhistory.html")
    return render_template("medicalhistory.html", data=data, survey_id=survey_id)


@app.route('/medicalhistory/<survey_id>/add/', methods=["get", "post"])
@require_login
def medicalhistoryadd(survey_id):
    # sql = "select * from suifang where id = %s" % survey_id
    # with db.cur() as cursor:
    #     cursor.execute(sql)
    #     data = cursor.fetchall()
    if request.method == "GET":
        sql = "select id from suifang where id = '%s'" % survey_id
        with db.cur() as cursor:
            cursor.execute(sql)
            data = cursor.fetchone()
        # print(data)
        return render_template("medical_add.html", data=data)
    if request.method == "POST":
        sql = "insert into medicalhistory(survey_id,medicinename,medicinesize,medicinecount,starttime,diseasename) values('%d','%s','%s','%s','%s','%s')"
        with db.cur() as cursor:
            cursor.execute(
                sql % (int(survey_id), request.form["medicinename"], request.form["medicinesize"],
                       request.form["medicinecount"], request.form["starttime"], request.form["diseasename"]))
        return redirect("/medicalhistory/%s" % survey_id)
        # return "hello" + survey_id
    return survey_id + "add"


@app.route('/medicalhistory/<survey_id>/delete/<medical_id>/', methods=["post"])
@require_login
def medicalhistorydelete(survey_id, medical_id):
    if request.method == "POST":
        sql = "delete from medicalhistory where id = '%s'" % medical_id
        with db.cur() as cursor:
            cursor.execute(sql)
        return redirect("/medicalhistory/%s" % survey_id)
    return "delete bro"
    # return render_template("medicalhistory.html", data=data, survey_id=survey_id)


@app.route('/test', methods=["get", "post"])
def testfunc():
    print("hello")
    if request.method == "POST":
        temp = ""
        temp = request.form["id_number"]
        temp = temp.replace('-', '')
        print(temp)

    return render_template("test.html")


if __name__ == "__main__":
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=True)
#    app.run(host='0.0.0.0', port=5000)
