from random import randint
from datetime import datetime
from time import strftime
from exceptions import EnemyDown, GameOver
import settings


class Enemy:
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        attack = randint(1,3)
        return attack

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown
        else:
            pass


class Player:
    score = 0
    def __init__(self, name):
        self.name = name
        self.lives = settings.LIVES

    @staticmethod
    def fight(attack, defense):
        winner = ((1, 2), (2, 3), (3, 1))
        for item in winner:
            if item[0] == attack:
                if item[1] == defense:
                    result = 1
                elif item[0] == defense:
                    result = 0
                else:
                    result = -1
            else:
                pass
        return result

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver
        else:
            pass

    @classmethod
    def print_scores(cls):
        print("You are scored {} points.".format(cls.score))
        return cls.score

    def attack(self, enemy_obj):
        your_hero = input('Select ATTACK to Use: 1 - WIZARD, 2 - WARRIOR, 3 - ROGUE:')
        your_hero = int(your_hero)
        opponent = enemy_obj.select_attack()
        print("{} vs {}".format(your_hero, opponent))
        fight_result = self.fight(your_hero, opponent)
        if fight_result == 0:
            print("It's a draw!The enemy has been repelled your attack")
        elif fight_result == 1:
            print("You attacked successfully!")
            enemy_obj.decrease_lives()
            Player.score += 1
            print(Player.score)

        elif fight_result == -1:
            print("You missed!")
        return fight_result

    def defence(self, enemy_obj):
        your_hero = input('Select hero for defence: 1 - WIZARD, 2 - WARRIOR, 3 - ROGUE:')
        your_hero = int(your_hero)
        opponent = enemy_obj.select_attack()
        print("{} vs {}".format(your_hero, opponent))
        fight_result = self.fight(opponent, your_hero)
        if fight_result == 0:
            print("It's a draw! Your hero is repelled the attack.")
        elif fight_result == 1:
            print("Your hero has been defeated.")
        elif fight_result == -1:
            print("He is missed")
        return fight_result

    def write_result(self):
        with open(r'scores.txt', 'a') as output:
            a = datetime.now()
            a = strftime('%Y-%m-%d %H:%M:%S', datetime.timetuple(a))
            string = '{},\t{}\t{}\n'.format(a, self.name, self.print_scores())
            print(string)
            output.write(string)
            output.close()






