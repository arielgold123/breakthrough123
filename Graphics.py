import pygame
import numpy as np
from state import *
















class Graphics:
    def __init__(self, window_size=(400, 400), board_size=8, circle_size=20):
       
        self.LIGHT_BLUE = (173, 216, 230)
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.LIGHT_GRAY = (211, 211, 211)
       
       
        self.window_size = window_size
        self.board_size = board_size
        self.circle_size = circle_size
        pygame.init()
        self.screen = pygame.display.set_mode(self.window_size)
       
    def draw_board(self, state):
       
        for row in range(self.board_size):
            for col in range(self.board_size):
                if (row + col) % 2 == 0:
                    color = self.LIGHT_BLUE
                else:
                    color = self.WHITE
                pygame.draw.rect(self.screen, color, [col * 50, row * 50, 50, 50])
       
       
        for row in range(self.board_size):
            for col in range(self.board_size):
                if state.board[row][col] == 2:
                    color = self.BLACK
                elif state.board[row][col] == 1:
                    color = self.LIGHT_GRAY
                else:
                    continue
                x = col * 50 + 25
                y = row * 50 + 25
                pygame.draw.circle(self.screen, color, [x, y], self.circle_size)
       
       
        for i in range(self.board_size + 1):
            pygame.draw.line(self.screen, self.BLACK, [0, i * 50], [self.window_size[0], i * 50], 1)
            pygame.draw.line(self.screen, self.BLACK, [i * 50, 0], [i * 50, self.window_size[1]], 1)
       
    def run(self):
       
        pygame.display.update()
       
       
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
       
       
        pygame.quit()








    def calc_row_col(self, pos):
        x, y = pos
        col = x // 50
        row = y // 50
        return row, col








    def update(self):
         pygame.display.update()








