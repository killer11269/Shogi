#!/bin/python3.5

import sys
sys.path.append('../class')
import Class


stone = Class.stone("pedone", "file.grafic", "witeh", "front")
print (stone.name, stone.grafic, stone.team, stone.direction)