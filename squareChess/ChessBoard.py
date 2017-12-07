#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import helper

class ChessBoard:
    pieces = [[0 for i in range(5)] for i in range(5)]
    playCount = 0
    state = "play"
    result = ""

    def __init__(self):
        self.reset()
        self.mainLoop()

    def showBoard(self):
        for line in self.pieces:
            for c in line:
                print(c, end='')
                print(' ', end='')
            print()

    def reset(self):
        self.pieces = [[0 for i in range(5)] for i in range(5)]
        self.pieces[2][2] = '*'
        self.playCount = 0
        self.state = "play"

    def showFrame(self):
        for i in range(10):
            print()
        self.showBoard()
        if self.state == "end":
            print(self.result)
        else:
            print("now player ", self.playCount%2+1, " move")

    def placable(self, x, y):
        if x<0 or x>4 or y<0 or y>4:
            return False
        if self.pieces[x][y] != 0:
            return False
        return True

    def isEnd(self):
        squares = helper.getAllSquares()
        for square in squares:
            dict = {0: 0, 1: 0, 2: 0}
            for p in square:
                dict[self.pieces[p[0]][p[1]]] += 1
            if dict[1] == 4:
                self.result = "player 1 win"
                self.state = "end"
                return True
            if dict[2] == 4:
                self.result = "player 2 win"
                self.state = "end"
                return True
        return False

    def mainLoop(self):
        while 1:
            self.showFrame()
            command = input()
            if command == "restart":
                self.reset()
            if self.state == "end":
                continue

            cmds = command.split()
            if len(cmds) != 2:
                continue
            x = int(cmds[0])
            y = int(cmds[1])
            x -= 1
            y -= 1
            if not self.placable(x, y):
                continue
            self.pieces[x][y] = self.playCount%2+1
            self.playCount += 1

            if self.isEnd():
                pass
