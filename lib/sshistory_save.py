import mysql.connector
import sys
import time
sys.path.append("..")
from config import sshistory_set


def saveRequest(ssRequest, ssResponse, ssType='baike'):
    mydb = mysql.connector.connect(
        host=sshistory_set.host,
        user=sshistory_set.user,
        passwd=sshistory_set.passwd,
        database=sshistory_set.database
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO ssHistory (`ssType`, `ssRequest`, `ssResponse`, `ssTime`, `ssFromIP`) VALUES (%s, %s, %s, %s, %s)"
    val = (ssType, ssRequest, ssResponse, time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime()), "")

    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except:
        mydb.rollback()

    mydb.close()


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print('缺少必要参数.')
        exit(2)
    saveRequest(sys.argv[1], sys.argv[2], 'baike')
