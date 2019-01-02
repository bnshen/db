
import random
import time,sqlite3

keys = {
    'c':['kh','km','xf','xs','yxh'],
    's':['xh','xm','xb','csrq','jg','sjhm','yxh'],
    'd':['yxh', 'mc', 'dz', 'lxdh'],
    't':['gh', 'xm', 'xb', 'csrq', 'xl', 'jbgz', 'yxh'],
    'o':['xq', 'xh', 'gh', 'sksj'],
    'e':['xh', 'xq', 'kh', 'gh', 'pscj', 'kscj', 'zpcj']
}



def findx(s:str):
    conn = sqlite3.connect('school.sqlite3')
    c = conn.cursor()
    sql = 'select * from '+s+';'
    cursor = c.execute(sql)
    return [i for i in cursor]
    conn.close()

def deletex(table:str,params:dict):
    if table not in keys or len(params) != len(keys[table]):
        raise
    sql = 'delete from %s where ' % table
    index = 0
    for param in params:
        if params[param] != 'None':
            sql += '%s = \'%s\' and ' % (keys[table][index],params[param])
            index += 1
    sql = sql[:-4]
    conn = sqlite3.connect('school.sqlite3')
    c = conn.cursor()
    try:
        cursor = c.execute(sql)
        conn.commit()
        conn.close()
        return 'success'
    except Exception as e:
        conn.close()
        return ['error',sql,e]
        


