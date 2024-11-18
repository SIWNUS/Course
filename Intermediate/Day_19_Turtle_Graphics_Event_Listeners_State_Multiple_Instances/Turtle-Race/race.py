from random import randint
from turtle import Turtle

class TurtleRace():
    '''This class takes your list and number of turtles you want appended to this list
        before calling the methods of this list. You can pass in an empty list or any 
        list with turtles(t_list) and number of turtles(t_num) you would like to add. 
        You should also pass the list of colors(c_list) in here to give your turtle any 
        random color from the list. No empty color_list.'''
    def __init__(self, t_list, c_list, t_num):
        self.list = t_list
        self.colors = c_list
        self.num = int(t_num)
        for _ in range(0, self.num):
            tim = Turtle()
            self.list.append(tim)

    def turtle_race(self):
        '''This method conducts the race and returns the color of the winning turtle in title case.
            starting from x-cor = -250 and ending in x-cor = 250. every turtle has 30 spacings between
            them. The lowest turtle is at y-cor = -60 and others are arranged 30 spaces above each other.'''
        size = len(self.list)
        race = True
        while race:
            for t in self.list:
                t.penup()
                if t.pos()[0] >= 250.0:
                    race = False
                else:
                    t.fd(randint(5, 15))

        winner_pos = 0
        for index in range(0, size):
            if self.list[index].pos()[0] > winner_pos:
                winner_pos = self.list[index].pos()[0]

        for t in self.list:
            if t.pos()[0] == winner_pos:
                return t.pencolor().lower()
            
    def race_arrange(self):
        '''This method helps give your turtle unique colors from your color_list
            and helps settle them in their starting position.'''
        increase = -60
        index = 0

        for every_turtle in self.list:
            every_turtle.shape('turtle')
            every_turtle.color(self.colors[index])
            current_pos = every_turtle.pos()
            every_turtle.teleport(current_pos[0] - 250, current_pos[1] + increase)
            increase += 30
            index += 1