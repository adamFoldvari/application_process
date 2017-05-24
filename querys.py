import psycopg2
import consol_functions
from database_connection_data import db_con_data


def query_handler(query_name):
    all_query = {'query_1': """SELECT first_name, last_name FROM mentors;""",

                 'query_2': """SELECT nick_name FROM mentors WHERE city = 'Miskolc';""",

                 'query_3': """SELECT first_name ||' '|| last_name, phone_number
                             FROM applicants WHERE first_name = 'Carol';""",

                 'query_4': """SELECT first_name ||' '|| last_name, phone_number
                              FROM applicants WHERE email LIKE '%@adipiscingenimmi.edu';""",

                 'query_5': """INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                               VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', 54823);
                               SELECT * FROM applicants WHERE application_code = 54823 ;""",

                 'query_6': """UPDATE applicants SET phone_number = '003670/223-7459'
                               WHERE first_name = 'Jemima' AND last_name = 'Foreman';
                               SELECT first_name, last_name, phone_number FROM applicants
                               WHERE first_name = 'Jemima' AND last_name = 'Foreman';""",

                 'query_7': """DELETE FROM applicants WHERE email LIKE '%@mauriseu.net';""",
                 }

    try:
        connection = None
        connect_str = "dbname={} user={} host='localhost'".format(
            db_con_data()['dbname'], db_con_data()['user'])
        connection = psycopg2.connect(connect_str)
        connection.autocommit = True
        cursor = connection.cursor()
        cursor.execute(all_query[query_name])
        table = cursor.fetchall()
        consol_functions.pprint_table(table)
    except psycopg2.OperationalError as exception:
        consol_functions.exception_handler('OperationalError')
    except psycopg2.ProgrammingError as exception:
        consol_functions.exception_handler('ProgrammingError')
    except psycopg2.IntegrityError as exception:
        consol_functions.exception_handler('IntegrityError')
    finally:
        if connection:
            connection.close()