#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: September 23 2019
# This program makes a background for pybadge

import ugame
import stage

bank = stage.Bank.from_bmp16("ball.bmp")
background = stage.Grid(bank, 10, 8)
game = stage.Stage(ugame.display, 12)
game.layers = [background]
game.render_block()

while True:
    pass
