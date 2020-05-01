class EnemyDown(Exception):
    pass


class GameOver(Exception):

    @staticmethod
    def You_Lose(object, current_score):
        print("You are scored {} points.".format(object.print_scores()))
        records = current_score.records('scores.txt')
        records.append(current_score)
        records.sort(key=lambda record: record.score, reverse=True)
        for item in range(0, 10):
            records[item].write_result()





