import pickle
# print main menu
def main_menu():
    print('\n**** MEMORY MANIA ****')
    print('\n1. New Game\n2. Load Game\n3. Quit Application')

# print game options
def game_mode_options():
    print('\n**** MODE SELECT ****')
    print('1. Levels')
    print('2. Endless')
    print('3. View Highscores')
    print('4. View Player Stats')
    print('5. Game Mode Descriptions')
    print('6. Save & Return to Main Menu')

# print instructions
def instructions():
    print('\n--------------------')
    print('Game Modes:')
    print('--------------------')
    print('Levels:')
    print('Progress through levels by correctly memorizing a flash of characters. Levels get harder as you get higher! Progress is saved.\n')
    print('\nEndless:')
    print('Correctly memorize a flash of different characters to advance rounds. Climb as many rounds as you can without being incorrect to\nset a highscore! Rounds flash more characters after every two rounds. Progress resets when you lose!')
    print('---------------------')

def level_options(player):
    print('\n**** LEVEL ' + str(player.get_level()) + ' ****')
    print('1. Play level.')
    print('2. Quit and exit to mode select.')

# endless difficulties
def endless_difficulty_select():
    print('\n**** SELECT DIFFICULTY ****')
    print('1. Easy      -lowercase letters with slow timer')
    print('2. Medium    -lowercase & uppercase letters with slow timer')
    print('3. Hard      -lowercase letters with fast timer')
    print('4. HARDCORE  -lowercase & uppercase letters with an even faster timer. Good Luck >:)')

def endless_success():
    print('\nNew round available!')
    print('1. Play next round')
    print('2. Quit and exit to game modes')

def endless_game_over(round_num, pb, difficulty):
    print('\n**** GAME OVER ****')
    if(pb):
        print('You broke you personal best on ' + difficulty + '! New personal best: ' + str(round_num) + '.')
    else:
        print('You lasted ' + str(round_num) + ' round(s) on ' + difficulty + '.')
    print('1. Play again.')
    print('2. Quit and exit to game modes.')

def player_stats(player):
    print('\n**** PLAYER STATS ****')
    print('Endless (easy) personal best: ' + str(player.get_endless_highscore_from_easy()))
    print('Endless (medium) personal best: ' + str(player.get_endless_highscore_from_medium()))
    print('Endless (hard) personal best: ' + str(player.get_endless_highscore_from_hard()))
    print('Endless (HARDCORE) personal best: ' + str(player.get_endless_highscore_from_hardcore()))
    print('Current level: ' + str(player.get_level()))

def print_highscores(ee, em, eh, ehc, l):
    print('\n**** HIGHSCORES ****')
    print('Endless (Easy):')
    print('1. ' + ee.get_fp_name() + ' | Round: ' + str(ee.get_fp_round()))
    print('2. ' + ee.get_sp_name() + ' | Round: ' + str(ee.get_sp_round()))
    print('3. ' + ee.get_tp_name() + ' | Round: ' + str(ee.get_tp_round()))
    print('\nEndless (Medium):')
    print('1. ' + em.get_fp_name() + ' | Round: ' + str(em.get_fp_round()))
    print('2. ' + em.get_sp_name() + ' | Round: ' + str(em.get_sp_round()))
    print('3. ' + em.get_tp_name() + ' | Round: ' + str(em.get_tp_round()))
    print('\nEndless (Hard):')
    print('1. ' + eh.get_fp_name() + ' | Round: ' + str(eh.get_fp_round()))
    print('2. ' + eh.get_sp_name() + ' | Round: ' + str(eh.get_sp_round()))
    print('3. ' + eh.get_tp_name() + ' | Round: ' + str(eh.get_tp_round()))
    print('\nEndless (HARDCORE):')
    print('1. ' + ehc.get_fp_name() + ' | Round: ' + str(ehc.get_fp_round()))
    print('2. ' + ehc.get_sp_name() + ' | Round: ' + str(ehc.get_sp_round()))
    print('3. ' + ehc.get_tp_name() + ' | Round: ' + str(ehc.get_tp_round()))
    print('\nLevels:')
    print('1. ' + l.get_fp_name() + ' | Level: ' + str(l.get_fp_round()))
    print('2. ' + l.get_sp_name() + ' | Level: ' + str(l.get_sp_round()))
    print('3. ' + l.get_tp_name() + ' | Level: ' + str(l.get_tp_round()))
