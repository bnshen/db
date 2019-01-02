from flask import Flask,render_template,redirect, url_for
import db
from form import *
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY']='nothing'
keys = ['日期/时间','编号','接待人','内容','建议']

@app.route('/hello')
def hello_world():
    content = []
    for i in range(10):
        content.append('第 %d 次，顾斌为什么能'% i)
    return render_template('hello.html',title = '顾斌为什么这么能',content =content)

@app.route('/date/<string:query>')
def find_date(query):
    return render_template('law_help.html',title = query,content = db.find_date(query),keys=keys)

@app.route('/content/<string:query>')
def find_content(query):
    return render_template('law_help.html',title = query,content = db.find_content(query),keys=keys)

@app.route('/')
def main():
    return render_template('mainpage.html')

@app.route('/law_dict/<string:query>')
def find_law_dict(query):
    return render_template('law_dict.html',title = query,content = db.find_fatiao(query))

@app.route('/search/<string:type>',methods=['GET','POST'])
def search(type):
    if type == 'lh_key':
        myform =  law_help_key_form()
        if myform.validate_on_submit():
            data = keys.keys()[myform.data.data]
            return redirect('/content/'+data)
    elif type == 'lh_date':
        myform = law_help_date_form()
        if myform.validate_on_submit():
            data = myform.data.data
            return redirect('/date/'+data)
    elif type == 'ld_key':
        myform = law_dict_key_form()
        if myform.validate_on_submit():
            data = myform.data.data
            return redirect('/law_dict/'+data)
    else:
        return render_template('mainpage.html')
    return render_template('search.html',form = myform)
if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 8000)
