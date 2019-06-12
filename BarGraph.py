''' Graph2D/BarGraph.py
    Author: Ryan Stenmark <ryanpstenmark@gmail.com> (rstenmark.github.io)
    Date: May 16, 2019
'''

import gl
from random import randrange


white = [255, 255, 255]
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]

class BarGraph(object):

    def __init__(self, array=[], xy=(0, 0), margin=3):
        # List containing graph numerical data
        self.array = array
        # List (parallel to self.array) containing [R, G, B] color data
        self.color = array
        # Horizontal margin between elements in graph in pixels
        self.margin = margin
        # Create 8 'cursors' which enable sorts to maintain a state between iterations
        self.cursors = [(0, red), (0, red), (0, red), (0, red),
                        (0, red), (0, red), (0, red), (0, red)]

        # The top left corner of the bar graph
        self.xy = xy

    def set_pos(self, xy):
        self.xy = xy

    def push(self, n, color=white):
        # Push an element onto self.array and self.color like
        #   a FIFO stack.
        self.array.append(n)
        self.color.append(color)

    def pop(self):
        # Pop an element off of self.array and self.color like
        #   a FIFO stack.
        self.color.pop()
        return self.array.pop()

    def insert(self, i, n):
        self.array.insert(i, n)
        self.color.insert(i, white)

    def index(self, i):
        return self.array.index(i)

    def swap(self, i, j):
        # Swaps the elements at self.array[i] and self.array[j] in place
        k = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = k

    def randomize(self, min, max, count, step=1):
        if count is None:
            count = len(self.array)-1

        for i in range(0, count):
            try:
                self.array[i] = randrange(min, max, step)
            except(IndexError):
                self.array.append(randrange(min, max, step))

    def swapWithCursor(self, i, j):
        self.swap(self.cursors[i][0], j)

    def set_cursor(self, i, k, color=red):
        self.cursors[i] = (k, color)

    def get_cursor(self, i):
        return self.cursors[i][0]

    def set_color(self, i, color=white):
        self.color[i] = color

    def reset_colors(self):
        self.color = []
        for _ in self.array:
            self.color.append(white)

    def reset_cursors(self):
        # Set all cursors to point to index 0 with color red
        count_cursors = len(self.cursors)
        self.cursors = []
        for _ in range(0, count_cursors):
            self.cursors.append((0, red))

    def update_cursors(self, limit=8):
        # Update bar colors for current cursor positions
        for i in range(0, limit):
            self.set_color(self.cursors[i][0], self.cursors[i][1])


    def gl_batch(self, window, batch=None):
        # Takes pyglet.graphics.Batch
        # and pyglet.window.Window
        return gl.batch(self, window, batch)