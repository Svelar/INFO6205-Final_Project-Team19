import math
import datetime

# 距离计算函数，计算两个人之间的距离
import turtle

from person import Person
from config import *


def dis(point1, point2):
    d = math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)
    return d


# turtle的相关设定
turtle.setup(TOTAL_W * 2 + 200, TOTAL_H * 2, 0, 0)
turtle.screensize(TOTAL_W, TOTAL_H)
turtle.clearscreen()
turtle.hideturtle()
turtle.tracer(False)

# 所有人的数组
people = []

# 类属性的设置（其实可以用类方法）
Person.infected_num = 0
Person.total_num = 0

# 健康人
for i in range(healthy_num):
    masked = random.random()
    vaccine = random.random()
    t1 = Person(0, masked < masked_rate, vaccine < vaccine_rate)
    people.append(t1)

# 患者
for i in range(infected_num):
    masked = random.random()
    vaccine = random.random()
    t1 = Person(1, masked < masked_rate, vaccine < vaccine_rate)
    people.append(t1)

# 记录程序开始运行的时间
start = datetime.datetime.now()
# 开始
day = 0
count = 0
while Person.infected_num < Person.total_num:
    for a in people:
        for b in people:
            if id(a) == id(b):
                continue
            if a.status == 0 and b.status > 0 and dis(a, b) < DANGER_DIS:
                if a.vaccine:
                    a.infect(INFECTED_RATE[a.mask][b.mask])
                else:
                    a.infect(INFECTED_RATE_WITH_VACCINE[a.mask][b.mask])
    for a in people:
        a.move()
    turtle.update()
    #      time.sleep(1 / 300)
    count += 1
    # 每次更新100帧率，为一天
    if count > 100:
        day += 1
        count = 0
        for p in people[:]:
            if p.day() == -1:
                p.dead()
                people.remove(p)

        title = "第 %d 天 现有病例：%d 死亡病例：%d 总人数：%d" % (day, Person.infected_num, Person.dead_num, Person.total_num)
        print(title)
        turtle.title(title)

turtle.down()
end = datetime.datetime.now()
print("全部感染计算机用时", end - start, "模拟天数:", day, "天")
