import psycopg2


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
    rows = cursor.fetchall()
    for names in rows:
        for name in names:
            print(name, end=' ')
        print('\n')


def main():
    query_1()

if __name__ == '__main__':
    main()