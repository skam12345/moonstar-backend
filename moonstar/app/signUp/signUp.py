from moonstar.sql.serverSqlQuery import sqlList as query
import pymysql as mysql
import json
class SignUp:
    def __init__():
        super.__init__()
        
    def check_id(user):
        result = 0
        file = open('/workspace/moonstar-mysql/moonstar/dbinfo.json', encoding = 'utf-8')
        data = json.load(file)
        conn = mysql.connect(host=data['host'], user=data['user'], password=data['passwd'], db=data['db'], charset=data['charset'], port=int(data['port']))
        cur = conn.cursor()
        sql = query['check_id']
        cur.execute(sql, user['id'])
        check = cur.fetchone()
        if(check[0] == 0):
            result = {"result": True}
        else:
            result = {"result": False}

        return result
    
    def check_nick(user):
        result = 0
        file = open('/workspace/moonstar-mysql/moonstar/dbinfo.json', encoding = 'utf-8')
        data = json.load(file)
        conn = mysql.connect(host=data['host'], user=data['user'], password=data['passwd'], db=data['db'], charset=data['charset'], port=int(data['port']))
        cur = conn.cursor()
        sql = query['check_nick']
        cur.execute(sql, user['nickname'])
        check = cur.fetchone()
        if(check[0] == 0):
            result = {"result": True}
        else:
            result = {"result": False}

        return result
    
    def check_email(user):
        result = 0
        file = open('/workspace/moonstar-mysql/moonstar/dbinfo.json', encoding = 'utf-8')
        data = json.load(file)
        conn = mysql.connect(host=data['host'], user=data['user'], password=data['passwd'], db=data['db'], charset=data['charset'], port=int(data['port']))
        cur = conn.cursor()
        sql = query['check_email']
        cur.execute(sql, user['email'])
        check = cur.fetchone()
        if(check[0] == 0):
            result = {"result": True}
        else:
            result = {"result": False}

        return result
    
    def sign_up(user):
        result = 0
        file = open('/workspace/moonstar-mysql/moonstar/dbinfo.json', encoding = 'utf-8')
        data = json.load(file)
        conn = mysql.connect(host=data['host'], user=data['user'], password=data['passwd'], db=data['db'], charset=data['charset'], port=int(data['port']))
        cur = conn.cursor()
        sql = query['sign_up']
        cur.execute(sql, [user['id'], user['pwd'], user['nickname'], user['email'], user['question'], user['answer']])
        conn.commit()
        result = {"result": "가입 완료"}
        return result 