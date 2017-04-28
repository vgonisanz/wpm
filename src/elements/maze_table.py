# -*- coding: utf-8 -*-
import curses   # TODO remove for my colors or color pairs.
from element import Element

from random import *

class MazeTable(Element):
    """MazeTable: Table to draw a maze map. Use offset to allow a player too,
    Coordinates table, maze is lesser because offset between horizontal and vertical
    [0,0]
        --------> X
        |   *   ·
        |       ·
    Y   v · · · (w, h)
    """
    def __init__(self, width, height, x0, y0, x_offset = 3, y_offset = 1):
        self.background.logger.info("Creating mazetable")

        # Initialize all variables
        self._maze_map = [] # map[x][y]
        self._map_width = int(width / x_offset) + 1
        self._map_height = int(height / (1 + y_offset)) + 1
        self._x_offset = x_offset
        self._y_offset = y_offset

        # Assign
        super(MazeTable, self).__init__(width, height, x0, y0)
        return None

    def generate_random_maze(self):
        """Generate a random maze map
        :return: None
        """
        self.logger.info("Generating %dx%d maze" % (self._map_width, self._map_height))
        self._maze_map = []

        for i in range(self._map_width):
            n = []
            for j in range(self._map_height):
                n.append([1,1,0,0,0]) #right, bottom, captured, backtrack, color
            self._maze_map.append(n)

        for y in range(self._map_height):
            self._maze_map[0][y]=[1,0,1,0,0];
            self._maze_map[self._map_width-1][y]=[1,0,1,0,0];

        for x in range(self._map_width):
            self._maze_map[x][0]=[0,1,1,0,0]
            self._maze_map[x][self._map_height-1]=[0,1,1,0,0]

        self._maze_map[0][0]=[0,0,1,0,0]
        self._maze_map[self._map_width-1][0]=[0,0,1,0,0]


        playerstart=(1,1)
        playerexit=(self._map_width-1,self._map_height-1)
        mazestart=playerstart

        x,y=mazestart
        backtrack=1
        captures=0
        solutiontrack=0

        while 1:
            if (x,y)==playerexit:
                solutiontrack=backtrack

            if solutiontrack>0 and solutiontrack==self._maze_map[x][y][3]:
                solutiontrack=solutiontrack-1
                self._maze_map[x][y][4]=2

            if self._maze_map[x][y][2]==0:
                self._maze_map[x][y][2]=1
                captures=captures+1
                #if captures%10000==0:
                #    print >> stderr, 100*captures/(self._map_width*self._map_height), "%"

        #    self._maze_map[x][y][2]=1
            self._maze_map[x][y][3]=backtrack
            possibilities=[]
            for a,b in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                if a>=0 and a<self._map_width and b>=0 and b<self._map_height:
                    if self._maze_map[a][b][2]==0:
                        possibilities.append((a,b))

            if len(possibilities)==0:
                self._maze_map[x][y][3]=0
                backtrack=backtrack-1
                if backtrack==0:
                    break
                for a,b in [(x+1,y),(x-1,y),(x,y+1),(x,y-1),(-1,-1)]:
                    if a>=0 and a<self._map_width and b>=0 and b<self._map_height:
                        if self._maze_map[a][b][3]==backtrack:
                            break

                x=a
                y=b
                continue

            pos=randint(0,len(possibilities)-1)
            a,b=possibilities[pos]
            if a<x: self._maze_map[a][b][0]=0
            if a>x: self._maze_map[x][y][0]=0
            if b<y: self._maze_map[a][b][1]=0
            if b>y: self._maze_map[x][y][1]=0
            x=a
            y=b
            backtrack=backtrack+1

        self.logger.info("Maze generated, visited: %d" % captures)
        return None

    def draw(self):
        """Draw maze from map generated.
        x-Offset between cols, recommended 3
        y-Offset between rows, recommended 1
        Tile value: 4 bits in tile_values dictionary
        Bit 4: up, bit 3: left, bit 2: down and bit 1: right
        bit = 1 --> half line in that position

        return: None
        """
        #             [ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15 ]
        tile_values = [' ','╶','╷','┌','╴','─','┐','┬','╵','└','│','├','┘','┴','┤','┼']

        self.set_cursor_position(0, 0)
        for j in range(0, self._map_height - 1):
            for i in range(0, self._map_width - 1):
                # Check down and right character in tile and next ones.
                u = self._maze_map[i][j][0]
                l = self._maze_map[i][j][1]
                d = self._maze_map[i][j+1][0]
                r = self._maze_map[i+1][j][1]
                char = u * 8 + l * 4 + d * 2 + r

                # Odd position for maze, even for player
                x_pos = self._x_offset * i
                y_pos = (1 + self._y_offset) * j
                self.print_character(tile_values[char], x_pos, y_pos)

                # Position horizontal fixed, x + offset depending right character, add space/wall for player
                for offset in range(1, self._x_offset + 1):
                    self.print_character(tile_values[r * 5], x_pos + offset, y_pos)

                # Position vertical fixed, y + offset depending down character, add space/wall for player
                for offset in range(1, self._y_offset + 1):
                    self.print_character(tile_values[d * 10], x_pos, y_pos + offset)

        self.window.refresh()
        return None
