"""
Console game "Warriors"
"""
from datetime import datetime
from time import strftime
from exceptions import EnemyDown, GameOver
from models import Enemy, Player, Score



def play(main_hero):
    """
    The instruction of game is described in file README.md
    :param main_hero: account which is created for game and
    writing result to score table (input is instance of Player class )
    :return: Nothing. Game will have continued till exception will called.
    """
    start = input('Are you ready to start?Type start if YES\t')
    while start.lower() != "start":
        start = input('Type START for start the game, please')
    print("\n\n************************************************************\n")
    level = 1
    opponent = Enemy(level)
    round_of_battle = 1
    while True:
        print("LEVEL:\t{}\tRound:\t{}. FIGHT".format(level, round_of_battle))
        try:
            main_hero.attack(opponent)
        except EnemyDown:
            print("Your enemy is dead.")
            level += 1
            main_hero.score += 5
            round_of_battle = 1
            opponent = Enemy(level)
            print("You are scored {} points.".format(main_hero.score))
        else:
            print("You need to get ready for defence.")
            print("Your lives:\t{} || Enemy lives:\t{}".format(main_hero.lives, opponent.lives))
            round_of_battle = main_hero.defence(opponent, round_of_battle)



if __name__ == '__main__':
    NAME = input("Enter your name/account please:\t")
    print('Hi, {}'.format(NAME))
    subject = Player(NAME)
    try:
        play(subject)
    except GameOver:
        CURRENT_TIME = datetime.now()
        CURRENT_TIME = strftime('%Y-%m-%d %H:%M:%S', datetime.timetuple(CURRENT_TIME))
        current = Score(CURRENT_TIME, subject.name, subject.score)
        GameOver.you_lose(subject, current)
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")
