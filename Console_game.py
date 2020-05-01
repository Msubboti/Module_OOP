from datetime import datetime
from time import strftime
from models import Enemy, Player, Score
from exceptions import EnemyDown, GameOver



def play(main_hero):
    """

    :param main_hero:
    :return:
    """
    start = input('Are you ready to start?Type start if YES\t')
    while start.lower() != "start":
        start = input('Type START for start the game, please')
    print("\n\n************************************************************\n")
    level = 1
    opponent = Enemy(level)
    round = 1
    while True:
        print("LEVEL:\t{}\tRound:\t{}. FIGHT".format(level, round))
        try:
            main_hero.attack(opponent)
        except EnemyDown:
            print("Your enemy is dead.")
            level += 1
            main_hero.score += 5
            round = 1
            opponent = Enemy(level)
            print("You are scored {} points.".format(main_hero.print_scores()))
        else:
            print("You need to get ready for defence.")
            print("Your lives:\t{} || Enemy lives:\t{}".format(main_hero.lives, opponent.lives))
            round = main_hero.defence(opponent, round)



if __name__ == '__main__':
    name = input("Enter your name/account please:\t")
    print('Hi, {}'.format(name))
    subject = Player(name)
    try:
        play(subject)
    except GameOver:
        a = datetime.now()
        a = strftime('%Y-%m-%d %H:%M:%S', datetime.timetuple(a))
        current = Score(a, subject.name, subject.score)
        GameOver.You_Lose(subject, current)
    except KeyboardInterrupt:
        pass
    finally:
        print("Good bye!")
