# Functions for baseball project:
# - advance base runners based on hit passed from __main__
# - print score box
# - generate batting order
# - generate pitch result

import random
import time

def advance_runner(hit_f, base1_f, base2_f, base3_f, home_plate_f):
    print("before advance:")
    print(hit_f, base1_f, base2_f, base3_f, home_plate_f)

    batter = 1  # Initialize batter to put batter on base if someone already on first
    print(f"batter: {batter}")

    while hit_f:
        if base3_f == 1:
            base3_f = 0
            home_plate_f += 1
        if base2_f == 1:
            base2_f = 0
            base3_f = 1
        if base1_f == 1:
            if batter:
                base1_f = 1
                batter = 0
            else:
                base1_f = 0
            base2_f = 1
        else:
            base1_f = 1

        hit_f -= 1
        print("after 1 loop:\t", hit_f, base1_f, base2_f, base3_f, home_plate_f)
        print(f"batter: {batter}")
    print("function returns:", hit_f, base1_f, base2_f, base3_f, home_plate_f)
    print(f"batter: {batter}")
    return hit_f, base1_f, base2_f, base3_f, home_plate_f


def print_scorebox(home_list, visitors_list):
    # print("TEST TEST TEST")
    # print("Home Team List Score: {}".format(home_list[0]))
    # print("Home Team List Score: {}".format(home_list[3]))
    # <<<<<<< HEAD
    print(
        "INNING  ",
        "\t 1",
        "\t 2",
        "\t 3",
        "\t 4",
        "\t 5",
        "\t 6",
        "\t 7",
        "\t 8",
        "\t 9",
        "\t R",
        "\t H",
        "\t E",
    )
    print(
        "------  ",
        "\t--",
        "\t--",
        "\t--",
        "\t--",
        "\t--",
        "\t--",
        "\t--",
        "\t--",
        "\t--",
        "\t--",
        "\t--",
        "\t--",
    )
    print(
        "HOME:     \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2}".format(
            home_list[0],
            home_list[1],
            home_list[2],
            home_list[3],
            home_list[4],
            home_list[5],
            home_list[6],
            home_list[7],
            home_list[8],
            sum(home_list),
            88,
            88,
        )
    )

    print(
        "VISITORS: \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2} \t{:>2}".format(
            visitors_list[0],
            visitors_list[1],
            visitors_list[2],
            visitors_list[3],
            visitors_list[4],
            visitors_list[5],
            visitors_list[6],
            visitors_list[7],
            visitors_list[8],
            sum(visitors_list),
            99,
            99,
        )
    )


def batting_order():
    batting_lineup = []

    while len(batting_lineup) < 9:
        next_batter = random.randint(0, 8)
        if next_batter in batting_lineup:
            continue
        else:
            batting_lineup.append(next_batter)

    # print("batting order: {}".format(batting_lineup))
    return batting_lineup


def pitch_result():
    pitch_result_tuple = (
        ("strike", 10),
        ("ball", 11),
        ("foul ball", 12),
        ("foul out", 13),
        ("out - defense", 14),
        ("hit - single", 1),
        ("hit - double", 2),
        ("hit - triple", 3),
        ("hit - homerun", 4),
    )
    pitch_result_return = random.randint(0, 8)
    return pitch_result_tuple[pitch_result_return]


class TeamAtBat:
    def __init__(self, team, inning_num):
        self.runs = 0
        self.outs = 0
        self.walks = 0
        self.team = team
        self.inning_num = inning_num

    def team_at_bat(self):
        while self.outs < 3:
            self.player_at_bat()
        print(f"Runs for this at bat: {self.runs}\n\n\n")
        self.outs = 0  # Reset outs to zero after at bat
        return self.runs

    def player_at_bat(self):
        strikes = 0
        balls = 0

        while strikes < 3 and balls < 4:
            batter_swing = random.randint(0, 10)
            pitcher_throw = random.randint(0, 10)

            if pitcher_throw == batter_swing:
                # Batter hit the ball
                print(f"Throw is {pitcher_throw} - Swing is {batter_swing}")
                print(f"Batter hit the ball!")
                print("Hit result: Home Run! Yahoo!")
                self.runs += 1
                if self.walks > 0:
                    self.runs += self.walks  # Those previously walked will score
                    self.walks = 0  # Reset walks
                print(f"Runs: {self.runs}\n")
                # print("Advance base runners where needed\n")
                break
            elif pitcher_throw > batter_swing:
                # Pitch is a strike

                strikes += 1
                if strikes == 3:
                    self.outs += 1
                    print(f"Throw is {pitcher_throw} - Swing is {batter_swing} : Strike 3!\n")
                    print("You're out!\n")
                    print(f"Outs: {self.outs}\n")
                    break
                else:
                    print(f"Throw is {pitcher_throw} - Swing is {batter_swing} : Strike {strikes}\n")
            else:
                # Pitch is a ball
                balls += 1
                if balls == 4:
                    self.walks += 1
                    print(f"Throw is {pitcher_throw} - Swing is {batter_swing} : Ball 4!\n")
                    print("Walk! Take your base!")
                    print("Advance runners where needed\n")
                    if self.walks == 4:
                        self.runs += 1
                        self.walks = 0  # Reset walks
                        print("Extra run! Yee haw!")
                    break
                else:
                    print(f"Throw is {pitcher_throw} - Swing is {batter_swing}  :  Ball {balls}\n")

        print('=' * 50)
        print('\n\n')
        # time.sleep(2)


class Inning(TeamAtBat):
    def __init__(self):
        self.visiting_team_runs = 0
        self.home_team_runs = 0

    visitors_atbat = TeamAtBat(team='Visitors', inning_num=0)
    home_atbat = TeamAtBat(team='Hometeam', inning_num=0)


# Create a total of nine Inning() instances
inning_list = [Inning() for i in range(9)]

print(inning_list, '\n')


for index, inning in enumerate(inning_list):
    visitor_runs = 0
    hometeam_runs = 0
    print("=" * 100)
    print(f"{index + 1} " * 50)
    print("=" * 100)
    print(f"Visitor runs for inning {inning}: {visitor_runs}")
    print(f"Home Team runs for inning {inning}: {hometeam_runs}")
    print('\n')
    print(f"Inning {index + 1}")
    visitor_runs = inning.visitors_atbat.team_at_bat()
    hometeam_runs = inning.home_atbat.team_at_bat()
    print(f"Visitor runs for inning {index + 1}: {visitor_runs}")
    print(f"Home Team runs for inning {index + 1}: {hometeam_runs}")
    visitor_runs = 0  # Reset runs after at bat
    hometeam_runs = 0  # Reset runs after at bat

