''' Graph2D/main.py
    Author: Ryan Stenmark <ryanpstenmark@gmail.com> (rstenmark.github.io)
    Date: May 16, 2019
'''


import pyglet as pyg
pyg.options['vsync'] = True
import BarGraph as bg
import Sorts
import random as rand
from time import sleep

xy = (int(1920), int(1080))
win = pyg.window.Window(width=xy[0], height=xy[1])

if __name__ == '__main__':
    reset = True
    margin = 0
    min, max, count, step = 22, 880, 16*2, 22
    bargraph = bg.BarGraph([], (0, 0), margin)
    bargraph.randomize(min, max, count, step)
    bargraph.reset_colors()
    flat_env = pyg.media.procedural.LinearDecayEnvelope(0.2)
    @win.event
    def on_mouse_scroll(x, y, scrollx, scrolly):
        Sorts.bogosort(bargraph, True)

    fps_display = pyg.clock.ClockDisplay(color=(0.0, 0.0, 0.0, 1.0))

    @win.event
    def on_draw():
        win.clear()
        batch = bargraph.gl_batch(win)
        batch.draw()
        fps_display.draw()

    def update(dt):
        triangle = pyg.media.procedural.Triangle(dt,
                                        frequency=bargraph.array[bargraph.get_cursor(1)],
                                        envelope=flat_env)
        triangle.play()
        if Sorts.selectionsort(bargraph, True) and reset:
            bargraph.randomize(min, max, count)



    pyg.clock.schedule_interval(update, 1/100000)
    pyg.app.run()
