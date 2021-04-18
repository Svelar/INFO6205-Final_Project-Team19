#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import datetime
import turtle

from person import Person
from config import *

#calculate distance between two people
def dis(point1, point2):
    d = math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
    return d


# turtle settings
turtle.setup(TOTAL_W * 2 + 200, TOTAL_H * 2, 0, 0)
turtle.screensize(TOTAL_W, TOTAL_H)
turtle.clearscreen()
turtle.hideturtle()
turtle.tracer(False)

# All people
people = []

# init
Person.infected_num = 0
Person.total_num = 0

# healthy people
for i in range(healthy_num):
    masked = random.random()
    vaccine = random.random()
    t1 = Person(0, masked < masked_rate, vaccine < vaccine_rate)
    people.append(t1)

# infected people
for i in range(infected_num):
    masked = random.random()
    vaccine = random.random()
    t1 = Person(1, masked < masked_rate, vaccine < vaccine_rate)
    people.append(t1)

# record start time
start = datetime.datetime.now()
# start
day = 0
count = 0
while Person.infected_num < Person.total_num:
    for a in people:
        for b in people:
            if id(a) == id(b):
                continue
            if a.status == 0 and b.status > 0 and dis(a, b) < DANGER_DIS:
                if a.vaccine:
                    a.infect(INFECTED_RATE_WITH_VACCINE[a.mask][b.mask])
                else:
                    a.infect(INFECTED_RATE[a.mask][b.mask])
    for a in people:
        a.move()
    turtle.update()
    #      time.sleep(1 / 300)
    count += 1
    # count==100, add one day
    if count > 100:
        day += 1
        count = 0
        for p in people[:]:
            if p.day() == -1:
                p.dead()
                people.remove(p)

        title = "No. %d Day    All cases：%d    Death cases：%d    Total number of people：%d" % (day, Person.infected_num, Person.dead_num, Person.total_num)
        print(title)
        turtle.title(title)

turtle.down()
end = datetime.datetime.now()
print("Time of all infected", end - start, "Days:", day)