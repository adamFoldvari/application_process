import psycopg2
import consol_functions
from database_connection_data import db_con_data


def make_connection():
    try:
        connection = None
        connect_str = "dbname={} user={} host='localhost'".format(
            db_con_data()['dbname'], db_con_data()['user'])
        connection = psycopg2.connect(connect_str)
        connection.autocommit = True
        cursor = connection.cursor()
        return cursor, connection
    except psycopg2.OperationalError as exception:
        consol_functions.exception_handler('OperationalError')
    except psycopg2.ProgrammingError as exception:
        consol_functions.exception_handler('ProgrammingError')
    except psycopg2.IntegrityError as exception:
        consol_functions.exception_handler('IntegrityError')


def close_connection(connection):
    if connection:
        connection.close()


def first_test_query():
    cursor, connection = make_connection()
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    table = cursor.fetchall()
    close_connection(connection)
    return table
