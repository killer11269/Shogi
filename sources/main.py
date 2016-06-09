#!/bin/python3.5

import sys
sys.path.append('../class')
import Class


stone = Class.stone("pedone", 0x01, "file.grafic", "withe", "front", 0x02)
stone.display()

print (stone.move_stone())
