import mysql.connector


def connect_to_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="secret",
        database="employee-db"
    )
    return mydb


def queries_the_mysql_database_for_employees_working_in_the_Production_deparment_earning_more_than_100(mydb):
    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM employees")

    result = cursor.fetchall()

    for x in result:
        print(x)

    return result



def my_app():
    mydb = connect_to_db()
    result = queries_the_mysql_database_for_employees_working_in_the_Production_deparment_earning_more_than_100(mydb)
    print(result)


if __name__ == '__main__':
    my_app()

