#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 14:56:41 2021

@author: ked
"""

import pygame as pg

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
P1 = (255, 0, 0)
P2 = (0, 0, 255)

class TTTQubit:

    def __init__(self, qid, row, col, screen, center, size, color=BLACK):
        self.qid = qid
        self.row = row
        self.col = col
        self.screen = screen
        self.r = size / 2
        self.center = center
        self.color = color

    def set_probability(self, prob):
        color = [max(min(prob * P1[i] + (1 - prob) * P2[i], 255), 0) for i in range(3)]
        self.color = color

    def draw(self):
        try:
            pg.draw.circle(self.screen, self.color, self.center, self.r)
        except ValueError as e:
            print(self.color)
            print(e)
