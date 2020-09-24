import mysql.connector
import sys
import datetime
sys.path.append("..")
from config import sshistory_set

def getRequest(ssRequest, ssType='baike'):
    mydb = mysql.connector.connect(
        host=sshistory_set.host,
        user=sshistory_set.user,
        passwd=sshistory_set.passwd,
        database=sshistory_set.database
    )
    mycursor = mydb.cursor()

    dd = datetime.datetime.now()+datetime.timedelta(days=-1)
    ddd = dd.strftime("%Y-%m-%d %H:%M:%S")

    sqlcount = "SELECT COUNT(*) FROM ssHistory WHERE  ssType = %s AND ssRequest = %s  AND ssTime > %s "
    sql = "SELECT ssResponse FROM ssHistory WHERE ssType = %s AND ssRequest = %s AND ssTime > %s ORDER BY ssTime DESC"
    val = (ssType, ssRequest, ddd)
    try:
        mycursor.execute(sqlcount, val)
        resultcount = mycursor.fetchone()
        if resultcount[0] > 0:
            mycursor.execute(sql, val)
            resultreturn = mycursor.fetchone()
            result = resultreturn[0]
        else:
            result = 'None'
    except:
        mydb.rollback()

    mydb.close()
    return result


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('缺少必要参数.')
        exit(2)
    result = getRequest(sys.argv[1], 'baike')
    print("查询结果：%s" % result)
