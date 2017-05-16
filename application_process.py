import psycopg2
import consol_functions


try:
    # setup connection string
    connect_str = "dbname='foldadam' user='adamfoldvari' host='localhost' password='9947ADam'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)


def query_1():
    # run a SELECT statement
    cursor.execute("""SELECT first_name, last_name FROM mentors;""")
    # Fetch and print the result of the last execution
    table = cursor.fetchall()
    consol_functions.pprint_table(table)


def query_2():
    cursor.execute("""SELECT nick_name FROM mentors WHERE city = 'Miskolc';""")
    table = cursor.fetchall()
    consol_functions.pprint_table(table)


def query_3():
    cursor.execute("""SELECT first_name ||' '|| last_name, phone_number FROM applicants WHERE first_name = 'Carol';""")
    table = cursor.fetchall()
    consol_functions.pprint_table(table)


def main():
    # print('query1 :-----------------------------------------------------------------')
    # query_1()
    # print('query2:------------------------------------------------------------------')
    # query_2()
    # print'query3:--------------------------------------------------------------------')
    query_3()

if __name__ == '__main__':
    main()