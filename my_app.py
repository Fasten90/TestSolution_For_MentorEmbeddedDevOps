import mysql.connector


def connect_to_db():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="secret"
    )
    return mydb


def queries_the_mysql_database_for_employees_working_in_the_Production_deparment_earning_more_than_100(mydb):
    # TODO: mydb
    print(mydb)
    pass


def my_app():
    mydb = connect_to_db()
    result = queries_the_mysql_database_for_employees_working_in_the_Production_deparment_earning_more_than_100(mydb)
    print(result)


if __name__ == '__main__':
    my_app()

