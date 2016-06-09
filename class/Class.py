#!/bin/python3.5


class stone(object):

    def __init__(self, name, move, grafic, team, direction, position):
        self.name = name
        self.move = move
        self.grafic = grafic
        self.team = team
        self.direction = direction
        self.position = position
        
    def display(self):
        print (self.name, self.move, self.grafic, self.team, self.direction, self.position)
        return
    
    def move_stone(self):
        if self.move == 0x01 and self.direction == "front":
            self.position += 0x01
        return self.position
