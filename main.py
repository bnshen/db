from flask import Flask,render_template,redirect, url_for,request,make_response
import db
from form import *
from flask_bootstrap import Bootstrap
import json



app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']='nothing'
keys = {
    'c':['课号','课名','学分','学时','院系号'],
    's':['学号','姓名','性别','出生日期','籍贯','手机号码','院系号'],
    'd':['院系号', '名称', '地址', '联系电话'],
    't':['工号', '姓名', '性别', '出生日期', '学历', '基本工资', '院系编号'],
    'o':['学期', '课号', '工号', '上课时间'],
    'e':['学号', '学期', '课号', '工号', '平时成绩', '考试成绩', '总评成绩']
}






@app.route('/', defaults={'tablename': 'c'},methods=['GET','POST'])
@app.route('/<tablename>',methods=['GET','POST'])
def show(tablename):
    if len(tablename) > 1 or tablename not in keys.keys():
        return render_template('design.html',content =[],keys = [],tablename = 'None')
    form = switchdb()
    content = db.findx(tablename)
    if form.data.data != 'None':
        return redirect('/'+form.data.data)
    return render_template('design.html',content =content,keys = keys[tablename],form = form,tablename = tablename)

@app.route('/query',methods = ['POST'])
def getcourses():
    data = request.form.to_dict()
    result = {}
    result['contents'] = db.findx(data['tablename'])
    result['keys'] = keys[data['tablename']]
    return make_response(json.dumps(result),200)


@app.route('/delete',methods = ['POST'])
def delete():
    data = request.form.to_dict()
    tablename = data['tablename']
    data.pop('tablename')
    #tablename = data[-1]
    result = db.deletex(tablename,data)
    if result == 'success':
        try:
            return make_response('删除成功',200)
        except Exception as e:
            print(e)
            return make_response('unknown error',500)
    else:
        try:
            return make_response('无法删除',500)
        except Exception as e:
            print(e)
            return make_response('unknown error',500)


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 9000)
