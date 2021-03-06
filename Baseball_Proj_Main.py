import baseball_functions as bf

# Variables & Data structures

# Variables for bases & home plate

hit_g = base1_g = base2_g = base3_g = home_plate_g = 0

# Player positions stored in a tuple

players_tuple = (
    "pitcher",
    "catcher",
    "first baseman",
    "second baseman",
    "third baseman",
    "shortstop",
    "left fielder",
    "center fielder",
    "right fielder",
)

# Innings

innings_name = [
    "1st Inning",
    "2nd Inning",
    "3rd Inning",
    "4th Inning",
    "5th Inning",
    "6th Inning",
    "7th Inning",
    "8th Inning",
    "9th Inning",
]

# Pitch Result tuple

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

# Innings tracker list by list comprehension

innings_tracker = [x for x in range(0, 9)]
# print(innings_tracker)

# Home team & Visitors score tracking

home_team_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

visitors_list = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# ***** MAIN SECTION *****
# if __name__ == "__main__":

print()
print("*** MAIN SECTION ***")
print("+" * 80)

print()
print("=" * 70)
print()

# Set up batting order
print("Set up batting order")

visitors_batting_lineup = bf.batting_order()
hometeam_batting_lineup = bf.batting_order()

print(f"Visitors batting order: {visitors_batting_lineup}")
print(f"Home team batting order: {hometeam_batting_lineup}")


print()
print("=" * 70)
print()

print("+" * 80)
print("Check innings:")

for game_inning in innings_tracker:
    print("-" * 50)
    home_team_list[game_inning] = game_inning
    visitors_list[game_inning] = game_inning
    print(innings_name[game_inning])
    bf.print_scorebox(home_team_list, visitors_list)
    print("-" * 50)
    print()

print()
print("+" * 80)
print("*** MAIN SECTION ***")
print()

print()

home_team_list[0] = 1
home_team_list[3] = 3

visitors_list[2] = 10
visitors_list[6] = 2

print("Scorebox test:")
bf.print_scorebox(home_team_list, visitors_list)

print()
# ***** MAIN SECTION *****

#
# # Testing area
#
# home_team_list[2] = 3
# home_team_list[1] = 1
#
# visitors_list[2] = 33
# visitors_list[8] = 5
#
# print("*" * 30)
#
# print()
#
# # Print each inning and the scores for each team
#
# for inning in innings_tracker:
#     print(innings_name[inning])
#     print("home team score: \t{}".format(home_team_list[inning]))
#     print("visitors score: \t{}".format(visitors_list[inning]))
#
#     print("=" * 30)
#
# print("Home Team Score: {}".format(sum(home_team_list)))
# print("Visitors Score: {}".format(sum(visitors_list)))
#
# print("*" * 30)
#
# print(home_team_list)
# print(home_team_list[1])
# home_team_list[1] = 33
# print("Update home_team_list 2nd element to 33:")
# print(home_team_list)
# print(home_team_list[1])
#
# print("*" * 30)
# print()
#
# print("Home Team Score: {}".format(sum(home_team_list)))
# print("Visitors Score: {}".format(sum(visitors_list)))
#
# print("*" * 30)
# print()
#
# print("Test base advance function")
#
# print("Hit: {}\n first base: {}\n second base: {}\n third base: {}\n home plate: {}".format(
#     hit_g, base1_g, base2_g, base3_g, home_plate_g))
#
# hit_g = 2
# base3_g = 5
#
# print("Hit: {}\n first base: {}\n second base: {}\n third base: {}\n home plate: {}".format(
#     hit_g, base1_g, base2_g, base3_g, home_plate_g))
#
# # Try function to advance runners
# print()
# print("No runners on base, single")
#
# hit_g = 1
# base1_g = 0
# base2_g = 0
# base3_g = 0
# home_plate_g = 0
#
# print("Before:")
# print("Hit: {}\n first base: {}\n second base: {}\n third base: {}\n home plate: {}".format(
#     hit_g, base1_g, base2_g, base3_g, home_plate_g))
#
# hit_g, base1_g, base2_g, base3_g, home_plate_g = \
#     baseball_functions.advance_runner(hit_g, base1_g, base2_g, base3_g, home_plate_g)
#
# print("After:")
# print("Hit: {}\n first base: {}\n second base: {}\n third base: {}\n home plate: {}".format(
#     hit_g, base1_g, base2_g, base3_g, home_plate_g))
#
# print(">" * 80)
#
# print()
# print("Runner on first base, single")
#
# hit_g = 1
# base1_g = 1
# base2_g = 0
# base3_g = 0
# home_plate_g = 0
#
# print("Before:")
# print("Hit: {}\n first base: {}\n second base: {}\n third base: {}\n home plate: {}".format(
#     hit_g, base1_g, base2_g, base3_g, home_plate_g))
#
# hit_g, base1_g, base2_g, base3_g, home_plate_g = \
#     baseball_functions.advance_runner(hit_g, base1_g, base2_g, base3_g, home_plate_g)
#
# print("After:")
# print("Hit: {}\n first base: {}\n second base: {}\n third base: {}\n home plate: {}".format(
#     hit_g, base1_g, base2_g, base3_g, home_plate_g))
#
# print(">" * 80)
#
# print()
# print("Runner on first and second base, single")
#
# hit_g = 1
# base1_g = 1
# base2_g = 1
# base3_g = 0
# home_plate_g = 0
#
# print("Before:")
# print("Hit: {}\n first base: {}\n second base: {}\n third base: {}\n home plate: {}".format(
#     hit_g, base1_g, base2_g, base3_g, home_plate_g))
#
# hit_g, base1_g, base2_g, base3_g, home_plate_g = \
#     baseball_functions.advance_runner(hit_g, base1_g, base2_g, base3_g, home_plate_g)
#
# print("After:")
# print("Hit: {}\n first base: {}\n second base: {}\n third base: {}\n home plate: {}".format(
#     hit_g, base1_g, base2_g, base3_g, home_plate_g))
#
#
# print(">" * 80)
#
# print()
# print("Runner on first and second base, double")
#
# hit_g = 2
# base1_g = 1
# base2_g = 1
# base3_g = 0
# home_plate_g = 0
#
# print("Before:")
# print("Hit: {}\n first base: {}\n second base: {}\n third base: {}\n home plate: {}".format(
#     hit_g, base1_g, base2_g, base3_g, home_plate_g))
#
# hit_g, base1_g, base2_g, base3_g, home_plate_g = \
#     baseball_functions.advance_runner(hit_g, base1_g, base2_g, base3_g, home_plate_g)
#
# print("After:")
# print("Hit: {}\n first base: {}\n second base: {}\n third base: {}\n home plate: {}".format(
#     hit_g, base1_g, base2_g, base3_g, home_plate_g))
#

# advance_runner(hit_g, base1_g, base2_g, base3_g, home_plate_g)


#
# hit_g, base1_g, base2_g, base3_g, home_plate_g = 0
# advance_runner(hit_f, base1_f, base2_f, base3_f, home_plate_f):


print("*" * 30)
print()

print("END")
