#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 14:07:03 2021

@author: ked
"""

import pygame as pg
from TTTQubit import TTTQubit

HIGHLIGHT = (255, 255, 100)
MOUSEOVER = (160, 160, 160)

class TTTBoard:
    
    def __init__(self, screen, tiles, size, pos, pad, color, qid_start):
        self.screen = screen
        self.tiles = tiles
        self.size = size
        self.loc_x = pos[0]
        self.loc_y = pos[1]
        self.pad = pad
        self.color = color
        
        self.highlighted = []
        self.mouseover_item = None

        self.tile_size = self.size / self.tiles
        self.qubits = []
        qid = qid_start
        
        qubit_size = self.tile_size - 8 * self.pad
        
        for row in range(self.tiles):
            self.qubits.append([])
            for col in range(self.tiles):
                x = int(self.loc_x + (col + 0.5) * self.tile_size)
                y = int(self.loc_y + (row + 0.5) * self.tile_size)
                self.qubits[row].append(TTTQubit(qid, row, col, self.screen, (x, y), qubit_size))
                qid += 1
    
    def draw_board(self):
        
        sq_size = int(self.tile_size - 2 * self.pad)
        
        for row in range(self.tiles):
            for col in range(self.tiles):
                x = int(self.loc_x + col * self.tile_size + self.pad)
                y = int(self.loc_y + row * self.tile_size + self.pad)
                if (row, col) in self.highlighted:
                    color = HIGHLIGHT
                elif self.mouseover_item == self.qubits[row][col]:
                    color = MOUSEOVER
                else:
                    color = self.color
                pg.draw.rect(self.screen, color, (x, y, sq_size, sq_size))
                self.qubits[row][col].draw()
        self.mouseover_item = None
        
    def find_qubit(self, pos):
        if self.loc_x < pos[0] < self.loc_x + self.size:
            col = int((pos[0] - self.loc_x) // self.tile_size)
            col = min(col, self.tiles)
        else:
            return None
        if self.loc_y < pos[1] < self.loc_y + self.size:
            row = int((pos[1] - self.loc_y) // self.tile_size)
            row = min(row, self.tiles)
        else:
            return None
        
        return self.qubits[row][col]
    
    def highlight(self, row, col):
        if (row, col) not in self.highlighted:
            self.highlighted.append((row, col))
    
    def mouseover(self, item):
        if item is not None:
            self.mouseover_item = item
    
    def draw_cnot(self, control, target):
        pass
    
    def reset(self):
        self.highlighted = []