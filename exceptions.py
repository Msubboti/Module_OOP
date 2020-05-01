"""
Module includes exceptions for control process of game
"""
class EnemyDown(Exception):
    """
    Class EnemyDown, exceptions will be raised when enemy is defeated.
    """


class GameOver(Exception):
    """
    Exceptions will be raised when Player has lost all of his lives.
    """
    @staticmethod
    def you_lose(player_object, current_score):
        """
        Static method is used for get current result and
        TEN best scores will be written to score table.
        :param player_object: Instance of class Player
        :param current_score: Instance of class Score, it contains current result
        :return: Nothing.
        """
        print("You are scored {} points.".format(player_object.score))
        records = current_score.records('scores.txt')
        records.append(current_score)
        records.sort(key=lambda record: record.score, reverse=True)
        for item in range(0, 10):
            records[item].write_result()
