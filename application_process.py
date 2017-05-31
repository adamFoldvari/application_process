import consol_functions
import querys
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route('/')
def menu():
    links = ['/mentor']
    query_names = ['Mentors']
    return render_template('menu.html', links=links, query_names=query_names)


def main():
    menu_switcher = True
    while menu_switcher:
        consol_functions.menu()
        menu_number = consol_functions.menu_input()
        if menu_number == 1:
            querys.query_handler('query_1')
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 2:
            querys.query_handler('query_2')
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 3:
            querys.query_handler('query_3')
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 4:
            querys.query_handler('query_4')
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 5:
            querys.query_handler('query_5')
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 6:
            querys.query_handler('query_6')
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 7:
            querys.query_handler('query_7')
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 8:
            menu_switcher = False


if __name__ == '__main__':
    app.run(debug=True)