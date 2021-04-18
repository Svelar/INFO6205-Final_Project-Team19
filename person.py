import turtle

from config import *


class Person(object):
    infected_num = 0
    total_num = 0
    dead_num = 0

    def __init__(self, status, mask, vaccine):
        Person.total_num += 1
        self.turt = turtle.Turtle()

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

        self.turt.shape(shape)

        # 健康状态，2 为确诊 红色/1 为潜伏 黄色/0 为健康 绿色
        #
        self.status = status
        if self.status == 2:
            self.infected_day = 0
            Person.infected_num += 1
            self.turt.color("red")
        elif self.status == 1:
            self.infected_day = 0
            Person.infected_num += 1
            self.turt.color("yellow")
        else:
            self.turt.color("green")

        # 随机定义该点的位置
        self.x = random.randint(-TOTAL_W * 0.9, TOTAL_W * 0.9)
        self.y = random.randint(-TOTAL_H * 0.9, TOTAL_H * 0.9)

        self.turt.penup()
        self.turt.goto(self.x, self.y)

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
        # 如果他们超出了边界就会往回走
        self.turt.penup()
        self.turt.goto(self.x, self.y)

    def infect(self, rate):
        x = random.randrange(0, 100)
        if x / 100 < rate:
            self.status = 1  # 此人的状态进入潜伏期
            self.infected_day = 0  # 有了感染天数，且变为0
            self.turt.color('yellow')
            Person.infected_num += 1

    def day(self):
        if self.status > 0:
            if self.infected_day >= 7:
                x = random.randrange(0, 100)
                if x / 100 < DEATH_Rate:  # 死亡率为5%
                    # 确定死亡时返回某个值
                    return -1
        if self.status == 1:
            self.infected_day += 1
            if self.infected_day >= 4:
                x = random.randrange(0, 100)
                if x / 100 < Diagnose_Rate:
                    self.status = 2
                    self.turt.color('red')
        return 0

    def dead(self):
        # 死亡以后颜色变为灰色
        self.turt.color('gray')
        Person.total_num -= 1
        Person.dead_num += 1
        if self.status > 0:
            Person.infected_num -= 1

    def __del__(self):
        Person.total_num -= 1
        if self.status > 0:
            Person.infected_num -= 1
