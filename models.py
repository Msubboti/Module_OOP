"""
Module contains classes Player, Enemy and Score.
Class "Player" is storage of Name of player,
score and all events of game are written to property of class.
"""
from random import randint
from exceptions import EnemyDown, GameOver
import settings


class Enemy:
    """
    Class Enemy is used for choose hero for attack and defence.
    Method for decrease lives is included to this class also.
    """
    def __init__(self, level):
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        """
        Choose hero for attack or defence does by random method
        :return: Random integer from 1 till 3
        """
        return randint(1, 3)

    def decrease_lives(self):
        """
        Method for decrease of one lives,
        if number of lives equal to zero then exception will be called.
        :return: Nothing
        """
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown
        else:
            pass


class Player:
    """
    Class "Player" includes name of player,
    number of lives and current score
    """
    def __init__(self, name):
        self.name = name
        self.lives = settings.LIVES
        self.score = 0

    @staticmethod
    def fight(attack, defense):
        """
        Method is used for choose winner in current fight
        :param attack: First participant of fight (Number of hero)
        :param defense: Second participant of fight (Number of hero)
        :return: Result of fight
        """
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
        """
        Method for decreasing lives of Player
        :return: Raise the exception
        """
        self.lives -= 1
        if self.lives == 0:
            raise GameOver
        else:
            pass

    def attack(self, enemy_obj):
        """
        Method defines instance of Enemy
        and send two candidates (Player's hero and Enemy's hero) for fight
        :param enemy_obj: Instance of class Enemy
        :return: Nothing
        """
        your_hero = input('Select ATTACK to Use: 1 - WIZARD, 2 - WARRIOR, 3 - ROGUE:')
        your_hero = int(your_hero)
        opponent = enemy_obj.select_attack()
        print("{} vs {}".format(your_hero, opponent))
        fight_result = self.fight(your_hero, opponent)
        if fight_result == 0:
            print("It's a draw!The enemy has been repelled your attack")
        elif fight_result == 1:
            print("You attacked successfully!\nYou have got one extra point")
            self.score += 1
            enemy_obj.decrease_lives()

        elif fight_result == -1:
            print("You missed!")

    def defence(self, enemy_obj, round_of_battle):
        """
        Method defines instance of Enemy
        and send two candidates (Player's hero and Enemy's hero) for fight.
        Player hero are defencing
        :param enemy_obj: Instance of class Enemy
        :param round_of_battle: Number of current round
        :return: Number of current round
        """
        your_hero = input('Select hero for defence: 1 - WIZARD, 2 - WARRIOR, 3 - ROGUE:')
        your_hero = int(your_hero)
        opponent = enemy_obj.select_attack()
        print("{} vs {}".format(your_hero, opponent))
        fight_result = self.fight(opponent, your_hero)
        if fight_result == 0:
            print("It's a draw! Your hero is repelled the attack.")
            print("Welcome to next round")
            round_of_battle += 1
        elif fight_result == 1:
            print("Your hero has been defeated.")
            print("You have lost one lives")
            self.decrease_lives()
            print("Your lives:\t{} || Enemy lives:\t{}".format(self.lives, enemy_obj.lives))

        elif fight_result == -1:
            print("He is missed")
            print("Welcome to next round")
            round_of_battle += 1
        return round_of_battle


class Score:
    """
    Class "Score" is used for get current result,
    choose the ten best result and write these results to score table.
    """
    def __init__(self, time, name, score):
        self.time = time
        self.name = name
        self.score = score

    def __str__(self):
        return "{}: {}".format(self.name, self.score)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def records(fp):
        """
        Getting all scores from score table
        :param fp: Name of file with score
        :return: List instances of class Score
        """
        with open(fp, 'r') as records:
            objects = list()
            for line in records:
                listing = line[:-1].split('\t')
                record = Score(listing[0][:-1], listing[1], int(listing[2]))
                objects.append(record)
            f = open('scores.txt', 'w')
            f.close()
        return objects

    def write_result(self):
        """
        Write the best ten results
        :return: Nothing
        """
        with open(r'scores.txt', 'a') as output:
            string = "{},\t{}\t{}\n".format(self.time, self.name, self.score)
            output.write(string)
            output.close()
