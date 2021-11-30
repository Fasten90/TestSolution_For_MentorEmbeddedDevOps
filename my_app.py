import mysql.connector
import requests


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

    cursor.execute("""
    SELECT employees.id, employees.name, employees.birth_date, departments.department, salaries.salary
    FROM employees
        INNER JOIN departments ON employees.id = departments.empl_id
        INNER JOIN salaries ON employees.id = salaries.empl_id
    WHERE salaries.salary > 100
    ;
    """)

    result = cursor.fetchall()

    for x in result:
        print(x)

    return result


def get_rest_api_users():
    response = requests.get('http://localhost:80/v1/users')
    users = response.json()
    for x in users:
        print(x)
    return users



def get_access_rights():
    # query = {'lat': '45', 'lon': '180'}
    #response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
    #print(response.json())
    pass


def my_app():
    mydb = connect_to_db()
    print('Exec MySQL')
    result = queries_the_mysql_database_for_employees_working_in_the_Production_deparment_earning_more_than_100(mydb)
    #print(result)
    print('Exec Rest-api users')
    users = get_rest_api_users()



if __name__ == '__main__':
    my_app()

