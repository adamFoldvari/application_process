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


def query_executor(query):
    try:
        cursor, connection = make_connection()
        cursor.execute(query)
        table = cursor.fetchall()
        # header = [description for description in cursor.description]
        header = []
        # print(table)
        return table, header
    except Exception as e:
        print(e)
    finally:
        if connection:
            connection.close()


def mentors_query():
    query = ("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                FROM mentors
                JOIN schools USING (city);""")
    table, header = query_executor(query)
    return table, header


def all_school_query():
    query = ("""SELECT mentors.first_name, mentors.last_name, schools.name, schools.country
                FROM mentors
                RIGHT JOIN schools USING (city)
                ORDER BY mentors.id;""")
    table, header = query_executor(query)
    return table, header


def mentor_by_country_query():
    query = ("""SELECT country, COUNT(mentors.id) AS count
                FROM schools
                JOIN mentors USING (city)
                GROUP BY country;""")
    table, header = query_executor(query)
    return table, header


def contacts_query():
    query = ("""SELECT schools.name, mentors.first_name, mentors.last_name
                FROM schools
                JOIN mentors ON mentors.id = schools.contact_person;""")
    table, header = query_executor(query)
    return table, header


def applicant_query():
    query = ("""SELECT applicants.first_name, applicants.application_code, applicants_mentors.creation_date
                FROM applicants
                JOIN applicants_mentors ON applicants.id = applicants_mentors.applicant_id
                WHERE applicants_mentors.creation_date > '2016/1/1'
                ORDER BY creation_date DESC;""")
    table, header = query_executor(query)
    return table, header
