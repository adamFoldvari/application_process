
def pprint_table(table):
    print("\033c")
    for rows in table:
        for item in rows:
            print(item, end=' ')
        print('\n')


def menu():
    print("\033c")
    query_list = ['Mentors full name',
                  'Nicknames of mentors from Miskolc',
                  'Carols phone number',
                  'Adipiscingenimmi University students phone number',
                  'Add the new applicant',
                  'Update Jemimas phone number',
                  'Delete mauriseu kids']
    for number, title in enumerate(query_list):
        print('{0}. {1}'.format(number + 1, title))
    print('\n')


def menu_input():
    menu_number = 0
    while not (0 < menu_number and menu_number < 8):
        try:
            menu_number = int(input('Please enter the number of the query you would like to execute: '))
            print('\n')
        except ValueError:
            print('Please enter an integer between 1 and 7!')
        if not (0 < menu_number and menu_number < 8):
            print('There is no such option!')
    return menu_number


def back_or_exit():
    user_input = input('Type q for quit or anything to go back: ')
    if user_input == 'q':
        return False
    else:
        return True
