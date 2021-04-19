#!/usr/bin/env python
# -*- coding: utf-8 -*-
import turtle

from config import *


class Person(object):
    infected_num = 0
    total_num = 0
    dead_num = 0

    def __init__(self, status, mask, vaccine):
        Person.total_num += 1
        self.turtle = turtle.Turtle()
        # self.turtle.hideturtle()
        #         mask  vaccine
        # circle   0     0
        # square   0     1
        # triangle 1     0
        # turtle   1     1
        self.mask = mask
        self.vaccine = vaccine
        # default
        shape = 'circle'
        if self.mask:
            if not self.vaccine:
                shape = 'square'
        else:
            if self.vaccine:
                shape = 'classic'
            else:
                shape = 'triangle'

        self.turtle.shape(shape)

        # health status:
        # 2: confirmed-red
        # 1: be in incubation-yellow
        # 0: healthy-green
        #
        self.status = status
        if self.status == 2:
            self.infected_day = 0
            Person.infected_num += 1
            self.turtle.color("red")
        elif self.status == 1:
            self.infected_day = 0
            Person.infected_num += 1
            self.turtle.color("yellow")
        else:
            self.turtle.color("green")

        # people randomly appear
        self.x = random.randint(-TOTAL_W * 0.9, TOTAL_W * 0.9)
        self.y = random.randint(-TOTAL_H * 0.9, TOTAL_H * 0.9)

        self.turtle.penup()
        self.turtle.goto(self.x, self.y)

    def move(self):
        dx = random.randint(-2, 2)
        dy = random.randint(-2, 2)
        if - TOTAL_W * 0.9 < self.x + dx < TOTAL_W * 0.9:
            self.x += dx
        else:
            self.x -= dx
        if - TOTAL_H * 0.9 < self.y + dy < TOTAL_H * 0.9:
            self.y += dy
        else:
            self.y -= dy
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        # If they go beyond the margin, they will go back


    def infect(self, rate):
        x = random.randrange(0, 100)
        if x / 100 < rate:
            self.status = 1  # be in period of incubation
            self.infected_day = 0  #infected day
            self.turtle.color('yellow')
            Person.infected_num += 1

    def day(self):
        if self.status > 0:
            if self.infected_day >= VIRUS_LATENCY: #more than a week
                x = random.randrange(0, 100)
                if x / 100 < DEATH_Rate:
                    # return -1 when died
                    return -1
        if self.status == 1:
            self.infected_day += 1
            if self.infected_day >= 4: #period of incubation is 4 days
                x = random.randrange(0, 100)
                if x / 100 < Diagnose_Rate:
                    self.status = 2
                    self.turtle.color('red')
        return 0

    def dead(self):
        # turn grey when died
        self.turtle.color('grey')
        Person.total_num -= 1
        Person.dead_num += 1
        if self.status > 0:
            Person.infected_num -= 1

    def __del__(self):
        Person.total_num -= 1
        if self.status > 0:
            Person.infected_num -= 1
