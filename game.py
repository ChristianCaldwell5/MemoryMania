# import error handling
from errorHandling import *
# import menu prints
from menus import *
# import gameplay
from gameplay import *


def main():
    # determines if player is still playing
    playing = True
    while(playing):
        main_menu()
        bad_choice = True
        while(bad_choice):
            choice = input('\nSelect an Option: ')
            if(choice == '1'):
                bad_choice = False
                new_game()
            elif(choice == '2'):
                bad_choice = False
                saved_game()
            elif(choice == '3'):
                bad_choice = False
                playing = False
                print('\nThank you for playing Memory Mania!')
            else:
                handle_invalid_option(choice)

main()
