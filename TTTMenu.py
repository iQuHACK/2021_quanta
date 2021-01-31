#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 16:34:14 2021

@author: ked
"""

import pygame as pg

HIGHLIGHT = (255, 200, 200)
MOUSEOVER = (160, 160, 255)

class TTTMenu:

    def __init__(self, screen, item_size, pos, pad, color):
        self.screen = screen
        self.item_size = item_size
        self.loc_x = pos[0]
        self.loc_y = pos[1]
        self.pad = pad
        self.color = color
        self.w = 2 * (self.item_size + 2 * self.pad)
        self.h = 3 * (self.item_size + 4 * self.pad)

        self.items = [["rot_minus_x", "rot_plus_x"], ["rot_minus_y", "rot_plus_y"], ["cnot", "measure"]]

        self.highlighted = []
        self.mouseover_item = None

    def draw(self):

        sq_size = int(self.item_size + 2 * self.pad)

        for row in range(3):
            for col in range(2):
                x = int(self.loc_x + col * (self.item_size + 4 * self.pad))
                y = int(self.loc_y + row * (self.item_size + 4 * self.pad))
                if self.items[row][col] in self.highlighted:
                    color = HIGHLIGHT
                elif self.mouseover_item == self.items[row][col]:
                    color = MOUSEOVER
                else:
                    color = self.color
                pg.draw.rect(self.screen, color, (x, y, sq_size, sq_size))
                image = pg.image.load(self.items[row][col] + ".png").convert_alpha()
                self.screen.blit(image, (x + self.pad, y + self.pad))
        self.mouseover_item = None


    def find_item(self, pos):
        if self.loc_x < pos[0] < self.loc_x + self.w:
            col = int((pos[0] - self.loc_x) // (self.item_size + 4 * self.pad))
            col = min(col, len(self.items))
        else:
            return None
        if self.loc_y < pos[1] < self.loc_y + self.h:
            row = int((pos[1] - self.loc_y) // (self.item_size + 4 * self.pad))
            row = min(row, len(self.items))
        else:
            return None

        return self.items[row][col]

    def highlight(self, item):
        if item not in self.highlighted:
            self.highlighted.append(item)

    def mouseover(self, item):
        if item is not None:
            self.mouseover_item = item

    def reset(self):
        self.highlighted = []
