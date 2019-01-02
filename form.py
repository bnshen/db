from flask_wtf import Form
from wtforms import StringField,SubmitField,DateField,SelectField
from wtforms.validators import DataRequired
keys = {
    'c':['课号','课名','学分','学时','院系号'],
    's':['学号','姓名','性别','出生日期','籍贯','手机号码','院系号'],
    'd':['院系号', '名称', '地址', '联系电话'],
    't':['工号', '姓名', '性别', '出生日期', '学历', '基本工资', '院系编号'],
    'o':['学期', '课号', '工号', '上课时间'],
    'e':['学号', '学期', '课号', '工号', '平时成绩', '考试成绩', '总评成绩']
}



class switchdb(Form):
    data = SelectField('选择你要查询的数据库',choices=[(None,None)]+[(i,i) for i in keys.keys()])
    submit = SubmitField('转到')
