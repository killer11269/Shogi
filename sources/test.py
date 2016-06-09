#!/bin/python3.5

import sys
sys.path.append('../class')
import Class


stone = Class.stone("pedone", 0xFF, "file.grafic", "withe", "front")
print (stone.name, stone.move, stone.grafic, stone.team, stone.direction)
