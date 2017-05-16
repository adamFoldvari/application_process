

def pprint_table(table):
    for rows in table:
        for item in rows:
            print(item, end=' ')
        print('\n')