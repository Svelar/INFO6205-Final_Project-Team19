import unittest

from config import VIRUS_LATENCY
from person import Person
from util import dis


class PersonTest(unittest.TestCase):

    def test_infect(self):
        p = Person(0, 0, 1)
        p.turtle.hideturtle()
        self.assertTrue(p.vaccine)
        self.assertTrue(not p.mask)

        num1 = Person.infected_num
        p.infect(1)
        self.assertEqual(num1 + 1, Person.infected_num)

    def test_dead(self):
        num1 = Person.total_num
        p = Person(0, 0, 1)
        p.turtle.hideturtle()
        self.assertEqual(num1 + 1, Person.total_num)
        p.dead()
        self.assertEqual(num1, Person.total_num)
        self.assertEqual(1, Person.dead_num)

    def test_math(self):
        p1 = Person(0, 0, 0)
        p2 = Person(0, 0, 0)
        p1.turtle.hideturtle()
        p2.turtle.hideturtle()
        p1.x = 0
        p1.y = 0
        p2.x = 3
        p2.y = 4
        self.assertEqual(5, dis(p1, p2))

    def test_day(self):
        p = Person(1, 0, 0)
        p.turtle.hideturtle()
        p.infected_day = VIRUS_LATENCY
        p.day()
        self.assertEqual(p.status, 1)

    def test_super(self):
        p = Person(0, 0, 0)
        p.super = True
        self.assertTrue(p.isSuper())


if __name__ == '__main__':
    unittest.main()
