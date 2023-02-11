from moonstar.sql.serverSqlQuery import sqlList as query
import pymysql as mysql
import json
import random

class Gachya:
    def __init__():
        super.__init__()
    
    def per_gachya(types):
        result = []
        file = open('/workspace/moonstar-mysql/moonstar/dbinfo.json', encoding = 'utf-8')
        data = json.load(file)
        conn = mysql.connect(host=data['host'], user=data['user'], password=data['passwd'], db=data['db'], charset=data['charset'], port=int(data['port']))
        cur = conn.cursor()
        sql = query['gachya']
        cur.execute(sql, types['a_type'])
        data = cur.fetchall()
        data = list(data)
        perList = []
        for i in range(0, len(data)):
            perList.append(data[i][2])
        for j in range(0, 10):
            luck = random.choices(range(1, len(data) + 1), weights=perList)
            sql = query['extract']
            cur.execute(sql, luck)
            res = cur.fetchall()
            result.append({"name": res[0][0], "star": res[0][1]})
        
        return result
            
            
            
            