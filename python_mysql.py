import mysql.connector


config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'demoprojet'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()




def add_plan(lib,detail,date):
    sql = ("INSERT INTO planing(libelle,detail,date_plan) VALUES ( %s,%s,%s)")
    cursor.execute(sql, (lib,detail,date))
    db.commit()
 


def get_plans():
    sql = ("SELECT * FROM planing")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row[2])


def get_plan(id):
    sql = ("SELECT * FROM planing WHERE id_plan = %s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()

    for row in result:
        print(row)






add_plan( 'plan 1','details de  plan 4','2020-02-13')
get_plans()


