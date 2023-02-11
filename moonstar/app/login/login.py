from moonstar.sql.serverSqlQuery import sqlList as query
import pymysql as mysql
import json

class Login:
    def __init__():
        super.__init__()
        
    
    def check_login(user):
        result = 0
        file = open('/workspace/moonstar-mysql/moonstar/dbinfo.json', encoding = 'utf-8')
        data = json.load(file)
        conn = mysql.connect(host=data['host'], user=data['user'], password=data['passwd'], db=data['db'], charset=data['charset'], port=int(data['port']))
        cur = conn.cursor()
        sql = query['login']
        cur.execute(sql, [user['id'], user['pwd']])
        data = cur.fetchone()
        print(data);
        if data is None:
            result ={
                "result": "로그인 실패"
            }
        else:
            result = {
                "id": data[0],
                "nickname": data[1],
                "profile": data[2],
            }
        return result