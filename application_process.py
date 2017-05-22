import consol_functions
import querys


def main():
    menu_switcher = True
    while menu_switcher:
        consol_functions.menu()
        menu_number = consol_functions.menu_input()
        if menu_number == 1:
            querys.query_handler(0)
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 2:
            querys.query_handler(1)
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 3:
            querys.query_handler(2)
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 4:
            querys.query_handler(3)
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 5:
            querys.query_handler(4)
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 6:
            querys.query_handler(5)
            menu_switcher = consol_functions.back_or_exit()
        elif menu_number == 7:
            querys.query_handler(6)
            menu_switcher = consol_functions.back_or_exit()


if __name__ == '__main__':
    main()