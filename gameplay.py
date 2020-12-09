import random
import time
import math
import pickle
import string
import sys
from Player import *
from Highscore import *
from errorHandling import *
from pathlib import Path
from menus import *

# initialize highscores
endless_easy_hs = pickle.load(open('Highscores/endless_easy.mem', 'rb'))
endless_medium_hs = pickle.load(open('Highscores/endless_medium.mem', 'rb'))
endless_hard_hs = pickle.load(open('Highscores/endless_hard.mem', 'rb'))
endless_hardcore_hs = pickle.load(open('Highscores/endless_hardcore.mem', 'rb'))
level_hs = pickle.load(open('Highscores/levels.mem', 'rb'))

# new game started
def new_game():
    print('\nNew game selected...')
    username = input('\nCreate a username: ')
    player = Player(username)
    print('\nWelcome to Memory Mania, ' + player.get_username() + '!')
    instructions()
    game(player)

# saved game resumed
def saved_game():
    print('\nSaved game selected...')
    username = input('\nWhat is your username? ')
    player_file = Path('Users/' + username + '.mem')
    # if so, deserialize data into player object
    if player_file.is_file():
        player = pickle.load(open('Users/' + username + '.mem', 'rb'))
        print('\nWelcome back to Memory Mania ' + player.get_username() + '.') 
        # start the game with a saved player
        game(player)
    # else, let the user know the game couldn't be found.
    else:
        print('\nSorry ' + username + ', your game couldn\'t be found.')

def level_round(player):
    # generate sequence based on level
    # number of characters depending on round. 4 is base. +1 every five rounds
    number_of_char = 3 + math.floor(player.get_level() / 5)
    if(player.get_level() < 20):
        sequence = ''
        timer = 1.5
        for x in range (0, number_of_char):
            sequence += random.choice(string.ascii_lowercase)
    elif(player.get_level() < 45 and player.get_level() > 19):
        sequence = ''
        timer = 1.5
        for x in range (1, number_of_char):
            sequence += random.choice(string.ascii_letters)
    else:
        number_of_char = 12
        sequence = ''
        timer = 1
        for x in range (1, number_of_char):
            sequence += random.choice(string.ascii_letters)
    for x in range (0,4):  
        b = 3 - x
        if(b == 0):
            print('START!')
        else:
            print(str(b), end="\r")
        time.sleep(1)
    # display sequence
    for x in range (0, len(sequence)):
        print(sequence[x], end='\r')
        time.sleep(timer)
    print('Sequence Finished')
    guess = input('\nWhat was the sequence? ')
    if(guess == sequence):
        print('\nThat is correct! You have advanced one level.')
        player.increment_level()
        # check if highscore was beatin
        if(player.get_level() > level_hs.get_fp_round()):
            level_hs.new_fp(player.get_username(), player.get_level())
            print('\nCongrats! You just beat the number 1 player for Levels mode!')
            pickle.dump(level_hs, open('Highscores/levels.mem', 'wb'))
        elif(player.get_level() > level_hs.get_sp_round()):
            level_hs.new_sp(player.get_username(), player.get_level())
            print('\nCongrats! You just beat the number 2 player for Levels mode!')
            pickle.dump(level_hs, open('Highscores/levels.mem', 'wb'))
        elif(player.get_level() > level_hs.get_tp_round()):
            level_hs.new_tp(player.get_username(), player.get_level())
            print('\nCongrats! You just beat the number 3 player for Levels mode!')
            pickle.dump(level_hs, open('Highscores/levels.mem', 'wb'))
    else:
        print('\nThat is incorrect! Your guess: ' + guess + '. Correct sequence: ' + sequence + '.')
        print('You will have to try the level again to move on!')

def level_mode(player):
    if(player.get_level() == 1):
        print('\nWelcome to Levels!\nProgress is saved and levels get harder every five rounds!\nLowercase & Uppercase begin at level 20.\nA faster timer and character cap start at level 45! Can you reach this level??')
    levels = True
    while(levels):
        level_options(player)
        level_bad_choice = True
        while(level_bad_choice):
            choice = input('\nWhat would you like to do? ')
            if(choice == '1'):
                level_bad_choice = False
                level_round(player)
            elif(choice == '2'):
                level_bad_choice = False
                levels = False
            else:
                handle_invalid_option(choice)

def endlessRound(case, timer, round_num):
    # generate sequence based on settings
    # number of characters depending on round. 3 is base. +1 every two rounds
    number_of_char = 3 + math.floor(round_num / 2)
    # generate sequence for low cases
    if(case == 'low'):
        sequence = ''
        for x in range (0, number_of_char):
            sequence += random.choice(string.ascii_lowercase)
    # generate sequence for low-up case
    elif(case == 'low-up'):
        sequence = ''
        for x in range (1, number_of_char):
            sequence += random.choice(string.ascii_letters)
    for x in range (0,4):  
        b = 3 - x
        if(b == 0):
            print('START!')
        else:
            print(str(b), end='\r')
        time.sleep(1)
    # display sequence
    for x in range (0, len(sequence)):
        print(sequence[x], end='\r')
        time.sleep(timer)
    print('Sequence Finished')
    guess = input('\nWhat was the sequence? ')
    if(guess == sequence):
        print('\nThat is correct! You have advanced one round.')
        return 1
    else:
        print('\nThat is incorrect! Your guess: ' + guess + '. Correct sequence: ' + sequence + '.')
        return 0

def endless_mode(player):
    # show mode selected
    print('\nEndless mode!')
    # display difficulties to select from
    endless_difficulty_select()
    difficulty_bad_choice = True
    # allow user to make choice
    while(difficulty_bad_choice):
        choice = input('\nWhich difficulty would you like to play? ')
        if(choice == '1'):
            difficulty_bad_choice = False
            print('\nEasy mode selected...')
            letters = 'low'
            timer = 2
        elif(choice == '2'):
            difficulty_bad_choice = False
            print('\nMedium mode selected...')
            letters = 'low-up'
            timer = 2
        elif(choice == '3'):
            difficulty_bad_choice = False
            print('\nHard mode selected...')
            letters = 'low'
            timer = 1
        elif(choice == '4'):
            difficulty_bad_choice = False
            print('\nHARDCORE mode selected...')
            letters = 'low-up'
            timer = 0.5
        else:
            handle_invalid_option(choice)
    # choice made, show short instructions.
    print('Once ready, a timer will count down to zero, and then you will attempt to remeber the\nsequence of letters that flash up in order!')
    endless = True
    endless_round = 1
    while(endless):
        print('\n**** ROUND ' + str(endless_round) + ' ****')
        response = ''
        # await player ready up
        while(response != 'y'):
            response = input('Ready to play? (press \'y\') ')
        # start endless
        result = endlessRound(letters, timer, endless_round)
        # the user was correct
        if(result == 1):
            endless_round += 1
            endless_success()
            continue_bad_choice = True
            while(continue_bad_choice):
                con_choice = input('What would you like to do? ')
                if(con_choice == '1'):
                    continue_bad_choice = False
                    # will loop back to endless
                elif(con_choice == '2'):
                    continue_bad_choice = False
                    endless = False
                else:
                    handle_invalid_option(con_choice)
        # the user was incorrect. Check for personal best and highscore
        else:
            # check is the user has beat their personal best/highscore on easy
            if(choice == '1'):
                # highscore
                if(endless_round > endless_easy_hs.get_fp_round()):
                    endless_easy_hs.new_fp(player.get_username(), endless_round)
                    print('\nCongrats! You just beat the number 1 player for Endless mode on easy!')
                    pickle.dump(endless_easy_hs, open('Highscores/endless_easy.mem', 'wb'))
                elif(endless_round > endless_easy_hs.get_sp_round()):
                    endless_easy_hs.new_sp(player.get_username(), endless_round)
                    print('\nCongrats! You just beat the number 2 player for Endless mode on easy!')
                    pickle.dump(endless_easy_hs, open('Highscores/endless_easy.mem', 'wb'))
                elif(endless_round > endless_easy_hs.get_tp_round()):
                    endless_easy_hs.new_tp(player.get_username(), endless_round)
                    print('\nCongrats! You just beat the number 3 player for Endless mode on easy!')
                    pickle.dump(endless_easy_hs, open('Highscores/endless_easy.mem', 'wb'))
                # personal best
                if(endless_round > player.get_endless_highscore_from_easy()):
                    # if so, set it and let them know when GAME OVER is displayed
                    player.new_endless_highscore_on_easy(endless_round)
                    endless_game_over(endless_round, True, 'easy')
                else:
                    endless_game_over(endless_round, False, 'easy')
            # check is the user has beat their personal best if on medium
            elif(choice == '2'):
                # highscore
                if(endless_round > endless_medium_hs.get_fp_round()):
                    endless_medium_hs.new_fp(player.get_username(), endless_round)
                    print('\nCongrats! You just beat the number 1 player for Endless mode on medium!')
                    pickle.dump(endless_medium_hs, open('Highscores/endless_medium.mem', 'wb'))
                elif(endless_round > endless_medium_hs.get_sp_round()):
                    endless_medium_hs.new_sp(player.get_username(), endless_round)
                    print('\nCongrats! You just beat the number 2 player for Endless mode on medium!')
                    pickle.dump(endless_medium_hs, open('Highscores/endless_medium.mem', 'wb'))
                elif(endless_round > endless_medium_hs.get_tp_round()):
                    endless_medium_hs.new_tp(player.get_username(), endless_round)
                    print('\nCongrats! You just beat the number 3 player for Endless mode on medium!')
                    pickle.dump(endless_medium_hs, open('Highscores/endless_medium.mem', 'wb'))
                # personal best
                if(endless_round > player.get_endless_highscore_from_medium()):
                    player.new_endless_highscore_on_medium(endless_round)
                    endless_game_over(endless_round, True, 'medium')
                else:
                    endless_game_over(endless_round, False, 'medium')
            # check is the user has beat their personal best if on hard
            elif(choice == '3'):
                # highscore
                if(endless_round > endless_hard_hs.get_fp_round()):
                    endless_hard_hs.new_fp(player.get_username(), endless_round)
                    print('\nCongrats! You just beat the number 1 player for Endless mode on hard!')
                    pickle.dump(endless_hard_hs, open('Highscores/endless_hard.mem', 'wb'))
                elif(endless_round > endless_hard_hs.get_sp_round()):
                    endless_hard_hs.new_sp(player.get_username(), endless_round)
                    print('\nCongrats! You just beat the number 2 player for Endless mode on hard!')
                    pickle.dump(endless_hard_hs, open('Highscores/endless_hard.mem', 'wb'))
                elif(endless_round > endless_hard_hs.get_tp_round()):
                    endless_hard_hs.new_tp(player.get_username(), endless_round)
                    print('\nCongrats! You just beat the number 3 player for Endless mode on hard!')
                    pickle.dump(endless_hard_hs, open('Highscores/endless_hard.mem', 'wb'))
                # personal best
                if(endless_round > player.get_endless_highscore_from_hard()):
                    player.new_endless_highscore_on_hard(endless_round)
                    endless_game_over(endless_round, True, 'hard')
                else:
                    endless_game_over(endless_round, False, 'hard')
            # check is the user has beat their personal best if on hardcode
            else:
                # highscore
                if(endless_round > endless_hardcore_hs.get_fp_round()):
                    endless_hardcore_hs.new_fp(player.get_username(), endless_round)
                    print('\nCongrats! You just beat the number 1 player for Endless mode on HARDCORE!')
                    pickle.dump(endless_hardcore_hs, open('Highscores/endless_hardcore.mem', 'wb'))
                elif(endless_round > endless_hardcore_hs.get_sp_round()):
                    endless_hardcore_hs.new_sp(player.get_username(), endless_round)
                    print('\nCongrats! You just beat the number 2 player for Endless mode on HARDCORE!')
                    pickle.dump(endless_hardcore_hs, open('Highscores/endless_hardcore.mem', 'wb'))
                elif(endless_round > endless_hardcore_hs.get_tp_round()):
                    endless_hardcore_hs.new_tp(player.get_username(), endless_round)
                    print('\nCongrats! You just beat the number 3 player for Endless mode on HARDCORE!')
                    pickle.dump(endless_hardcore_hs, open('Highscores/endless_hardcore.mem', 'wb'))
                # personal best
                if(endless_round > player.get_endless_highscore_from_hardcore()):
                    player.new_endless_highscore_on_hardcore(endless_round)
                    endless_game_over(endless_round, True, 'HARDCORE')
                else:
                    endless_game_over(endless_round, False, 'HARDCORE')
            game_over_bad_choice = True
            while(game_over_bad_choice):
                game_over_choice = input('What would you like to do? ')
                if(game_over_choice == '1'):
                    game_over_bad_choice = False
                    endless = False
                    # play again
                    endless_mode(player)
                elif(game_over_choice == '2'):
                    game_over_bad_choice = False
                    endless = False
                    print('\nExiting to game modes...')
                    # go back to game mode screen
                else:
                    handle_invalid_option(game_over_choice)

def game(player):
    game = True
    while(game):
        game_mode_options()
        game_bad_choice = True
        while(game_bad_choice):
            game_choice = input('\nWhat would you like to do? ')
            if(game_choice == '1'):
                game_bad_choice = False
                level_mode(player)
            elif(game_choice == '2'):
                game_bad_choice = False
                endless_mode(player)
            elif(game_choice == '3'):
                game_bad_choice = False
                print_highscores(endless_easy_hs, endless_medium_hs, endless_hard_hs, endless_hardcore_hs, level_hs)
            elif(game_choice == '4'):
                game_bad_choice = False
                player_stats(player)
            elif(game_choice == '5'):
                game_bad_choice = False
                instructions()
            elif(game_choice == '6'):
                game_bad_choice = False
                game = False
                print('\nSaving...')
            else:
                handle_invalid_option(game_choice)
    try:
        # serialize data
        pickle.dump(player, open('Users/' + player.get_username() + '.mem', 'wb'))
        # inform user of success
        print('\n' + player.get_username() + ', your game has been saved.')
    except Exception as e:
        # error happened, let user know
        print('\nSorry ' + player.get_username() + ', the game could not be saved.')
        print(e)
