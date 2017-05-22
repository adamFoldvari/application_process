import psycopg2
import consol_functions


try:
    # setup connection string
    connect_str = "dbname='foldadam' user='adamfoldvari' host='localhost' password='9947ADam'"
    # use our connection values to establish a connection
    connection = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    connection.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = connection.cursor()

except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)


def close_connection():
    if connection:
        connection.close()


def query_1():
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    table = cursor.fetchall()
    consol_functions.pprint_table(table)
    close_connection()


def query_2():
    cursor.execute("""SELECT nick_name FROM mentors WHERE city = 'Miskolc';""")
    table = cursor.fetchall()
    consol_functions.pprint_table(table)


def query_3():
    cursor.execute("""SELECT first_name ||' '|| last_name, phone_number
                      FROM applicants WHERE first_name = 'Carol';""")
    table = cursor.fetchall()
    consol_functions.pprint_table(table)


def query_4():
    cursor.execute("""SELECT first_name ||' '|| last_name, phone_number
                      FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';""")
    table = cursor.fetchall()
    consol_functions.pprint_table(table)


def query_5():
    cursor.execute("""INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                      VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);""")
    cursor.execute("""SELECT * FROM applicants WHERE application_code = 54823 ;""")
    table = cursor.fetchall()
    consol_functions.pprint_table(table)


def query_6():
    cursor.execute("""UPDATE applicants
                      SET phone_number = '003670/223-7459'
                      WHERE first_name = 'Jemima' AND last_name = 'Foreman';""")
    cursor.execute("""SELECT first_name, last_name, phone_number FROM applicants
                      WHERE first_name = 'Jemima' AND last_name = 'Foreman';""")
    table = cursor.fetchall()
    consol_functions.pprint_table(table)


def query_7():
    cursor.execute("""DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';""")
    table = ('We deleted the requested data!')
    consol_functions.pprint_table(table)
