#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 13:06:52 2021

@author: ked
"""

import sys
from enum import Enum, auto
import pygame as pg
from TTTBoard import TTTBoard
from TTTMenu import TTTMenu
import basic_ops
from expected_outcom import expected_outcome

class TiqTaqToe:

    class State(Enum):
        CHOOSE_GATE = auto()
        CHOOSE_2Q_CONTROL = auto()
        CHOOSE_2Q_TARGET = auto()
        CHOOSE_1Q_TARGET = auto()

    def __init__(self, tiles=3, w=1000, h=800):
        self.tiles = tiles
        self.w = w
        self.h = h

        pg.init()
        pg.display.set_caption('Tiq-Taq-Toe')
        self.screen = pg.display.set_mode((self.w, self.h))
        self.clock = pg.time.Clock()

        self.board = TTTBoard(self.screen, self.tiles, w/2, (3/8*w, h/4), 10, (200,200,200), 0)
        self.board.draw_board()

        self.menu = TTTMenu(self.screen, 100, (1/16*w, h/4), 10, (200,200,255))

        self.font = pg.font.SysFont('Corbel', 80)
        self.font_small = pg.font.SysFont('Corbel', 40)
        self.p1_text = self.font.render('Player 1', True, (0,0,0))
        self.p2_text = self.font.render('Player 2', True, (0,0,0))
        self.gate_text = self.font_small.render('choose a gate', True, (0,0,0))
        self.target_text = self.font_small.render('choose a target qubit', True, (0,0,0))
        self.control_text = self.font_small.render('choose a control qubit', True, (0,0,0))

        self.circ = basic_ops.initialize(self.tiles)
        self.update_probabilities()

    def update_probabilities(self):
        prob_zero_list = expected_outcome(self.circ)
        print(prob_zero_list)

        self.board.set_qubits(prob_zero_list)

    def run(self):
        playing = True
        state = self.State.CHOOSE_GATE
        control_qubit = None
        gate = None
        player1 = True

        while True:
            self.screen.fill((255, 255, 255))
            self.board.draw_board()
            self.menu.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    qubit = self.board.find_qubit(event.pos)
                    if qubit is not None:
                        if state == self.State.CHOOSE_2Q_CONTROL:
                            control_qubit = qubit
                            self.board.highlight(qubit.row, qubit.col)
                            state = self.State.CHOOSE_2Q_TARGET

                        elif state is self.State.CHOOSE_2Q_TARGET:
                            # TODO: Act on both qubits with gate
                            if qubit != control_qubit:
                                basic_ops.add_cnot(self.circ, control_qubit.qid, qubit.qid)
                                self.update_probabilities()

                                self.board.reset()
                                self.menu.reset()
                                state = self.State.CHOOSE_GATE
                                player1 = not player1

                        elif state is not self.State.CHOOSE_GATE:
                            # TODO: Act on qubit with gate

                            if gate == 'rot_plus_y':
                                basic_ops.add_ry(self.circ, 1, qubit.qid)
                            elif gate == 'rot_minus_y':
                                basic_ops.add_ry(self.circ, -1, qubit.qid)
                            self.update_probabilities()
                            state = self.State.CHOOSE_GATE
                            self.menu.reset()
                            player1 = not player1

                    menu_item = self.menu.find_item(event.pos)
                    if menu_item is not None:
                        if menu_item == 'measure':
                            # TODO: Measure
                            basic_ops.add_measurement(self.circ, self.tiles)
                        else:
                            if state is not self.State.CHOOSE_2Q_TARGET:
                                self.menu.reset()
                                gate = menu_item
                                self.menu.highlight(menu_item)
                                if gate == 'cnot':
                                    state = self.State.CHOOSE_2Q_CONTROL
                                else:
                                    state = self.State.CHOOSE_1Q_TARGET

            mouse_pos = pg.mouse.get_pos()
            mouse_qubit = self.board.find_qubit(mouse_pos)
            mouse_menu_item = self.menu.find_item(mouse_pos)

            if state is not self.State.CHOOSE_2Q_TARGET:
                self.menu.mouseover(mouse_menu_item)

            if state is self.State.CHOOSE_2Q_TARGET:
                if mouse_qubit is not None and mouse_qubit != control_qubit:
                    # self.board.draw_cnot(control_qubit, mouse_qubit)
                    self.board.mouseover(mouse_qubit)
            elif state is not self.State.CHOOSE_GATE:
                self.board.mouseover(mouse_qubit)

            if player1:
                self.screen.blit(self.p1_text, (400, 20))
            else:
                self.screen.blit(self.p2_text, (400, 20))

            if state is self.State.CHOOSE_GATE:
                self.screen.blit(self.gate_text, (400, 80))
            elif state is self.State.CHOOSE_2Q_CONTROL:
                self.screen.blit(self.control_text, (400, 80))
            else:
                self.screen.blit(self.target_text, (400, 80))

            pg.display.update()
            self.clock.tick(30)

game = TiqTaqToe()
game.run()
