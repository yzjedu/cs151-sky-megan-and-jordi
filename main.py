# Programmers: Megan, Jordi
# Course: Cs151, Professor Zee
# Due Date: 10/3/2024
# Lab Assignment: 3
# Problem statement: Make a program to calculate the distance traveled based on speed and /
# determine how many points the skier would receive if they went that distance.

# Data In: Code needs input the distance the skier wants to jump  in meter, the height of the jump in meter, the points per meter, /
# the par in meter, the skiers speed at the end of the jump,
# Data Out: How many points the skier will receive based on their distance traveled

# User should be prompted to enter five inputs: the height of the jump in meters, the skiers speed,
import math

print('What is the type of hill jump')
hill_type = input()
print('What is the speed at the end of the jump in km/h?')
skiers_speed_kmh = float(input())
if hill_type == "Normal" :
    height = 46
    points_per_meter = 2
    par = 90
elif hill_type == "Large":
    height = 70
    points_per_meter = 1.8
    par = 120

time_in_air = math.sqrt((2 * height) / 9.8)
distance = skiers_speed_kmh * time_in_air

total_points = 60 + (distance - par) * points_per_meter

print("Distance:", distance, "meters")
print("Total Points", total_points)

if total_points >= 61:
    print("Congrats on doing better than par!")
elif total_points < 10:
    print("What happened??")
else:
    print("Wow, you didn't go so far, I'm sorry ")
