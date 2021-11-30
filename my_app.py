import mysql.connector
import requests
import csv


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



def get_access_rights(username):
    # query = {'lat': '45', 'lon': '180'}
    param = {'username': username}
    response = requests.get('http://localhost:80/v1/accesslevels', params=param)
    access_right = response.json()
    return access_right['access']


def find_valid_users_and_get_access_rights(sql_result, users):
    user_with_access_rights = []
    for sql_row in sql_result:
        sql_name = sql_row[1]  # TODO: More beautiful solution at mysql query
        birthday = sql_row[2].strftime("%Y-%m-%d %H:%M:%S")
        # Finding in the user list
        username = 'N/A'
        for user_item in users:
            if sql_name == user_item['name']:
                rest_api_username = user_item['username']
                access_right = get_access_rights(rest_api_username)
                # Check right
                if 'WRITE' in access_right:
                    username = rest_api_username
                else:
                    username = 'N/A'  # Does not needed, but more beautiful
                # else: Incorrect access right
        user_with_access_rights.append({'Name': sql_name, 'Birthday': birthday, 'Username': username})
        # If it is not find in users: maybe he has not registered to rest-api server
    return user_with_access_rights


def export_to_csv(user_list_with_info):
    with open('exported_users.csv', 'w', newline='') as f:
        # create the csv writer
        fieldnames = 'Name', 'Birthday', 'Username'
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(user_list_with_info)

    # Only debug print
    for row in user_list_with_info:
        print(row)


def my_app():
    mydb = connect_to_db()
    print('Exec MySQL')
    sql_result = queries_the_mysql_database_for_employees_working_in_the_Production_deparment_earning_more_than_100(mydb)
    #print(result)
    print('Exec Rest-api users')
    users = get_rest_api_users()
    user_list_with_info = find_valid_users_and_get_access_rights(sql_result, users)
    export_to_csv(user_list_with_info)


if __name__ == '__main__':
    my_app()

