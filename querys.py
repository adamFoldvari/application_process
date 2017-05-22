import psycopg2
import consol_functions


def query_handler(query_index):
    all_query = [query_1(),
                 query_2(),
                 query_3(),
                 query_4(),
                 query_5(),
                 query_6(),
                 query_7()
                 ]
    try:
        connection = None
        connect_str = "dbname='foldadam' user='adamfoldvari' host='localhost' password='9947ADam'"
        connection = psycopg2.connect(connect_str)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(all_query[query_index])
        table = cursor.fetchall()
        consol_functions.pprint_table(table)
    except psycopg2.OperationalError as exception:
        print('Wrong username or password!')
    except psycopg2.ProgrammingError as exception:
        print("\033c")
        print(exception)
        print('We did the requested query, but nothing to print')
    except psycopg2.IntegrityError as exception:
        print("\033c")
        print('We already added this row before!')
    finally:
        if connection:
            connection.close()


def query_1():
    return """SELECT first_name, last_name FROM mentors;"""


def query_2():
    return """SELECT nick_name FROM mentors WHERE city = 'Miskolc';"""


def query_3():
    return """SELECT first_name ||' '|| last_name, phone_number
                      FROM applicants WHERE first_name = 'Carol';"""


def query_4():
    return """SELECT first_name ||' '|| last_name, phone_number
                      FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';"""


def query_5():
    return """INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                      VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);

              SELECT * FROM applicants WHERE application_code = 54823 ;"""


def query_6():
    return """UPDATE applicants
              SET phone_number = '003670/223-7459'
              WHERE first_name = 'Jemima' AND last_name = 'Foreman';

              SELECT first_name, last_name, phone_number FROM applicants
              WHERE first_name = 'Jemima' AND last_name = 'Foreman';"""


def query_7():
    return """DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';"""
