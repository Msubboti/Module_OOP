from exceptions import GameOver, EnemyDown
from models import Enemy, Player


def play(main_hero):
    start = input('Are you ready to start?Type start if YES\t')
    while start.lower() != "start":
        start = input('Type START for start the game, please')
    print("\n\n************************************************************\n")
    level = 1
    opponent = Enemy(level)
    Raund = 1
    while True:
        print("LEVEL:\t{}\tRound:\t{}. FIGHT".format(level, Raund))
        try:
            result = main_hero.attack(opponent)
        except EnemyDown:
            print("Your enemy is dead.")
            level += 1
            Player.score += 5
            print(Player.print_scores())
            Raund = 1
            opponent = Enemy(level)
        else:
            print("You need to get ready for defence.")
            print("Your lives:\t{} || Enemy lives:\t{}".format(main_hero.lives, opponent.lives))
            result = main_hero.defence(opponent)
            if result == 0 or result == -1:
                print("Good, lets continue")
                Raund += 1
            elif result == 1:
                print("You have lost one lives")
                print(main_hero.lives)
                main_hero.decrease_lives()
                print(main_hero.lives)
                Raund += 1


if __name__ == '__main__':
    name = input("Enter your name/account please:\t")
    print('Hi, {}'.format(name))
    subject = Player(name)
    try:
        play(subject)
    except GameOver:
        Player.print_scores()
        subject.write_result()
    except KeyboardInterrupt:
        pass
    finally:
        Player.score = 0
        print("Good bye!")
