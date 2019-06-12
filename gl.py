''' Graph2D/gl.py
    Author: Ryan Stenmark <ryanpstenmark@gmail.com> (rstenmark.github.io)
    Date: May 16, 2019
'''

import pyglet as pyg

def batch(bargraph, window, batch):
    if batch is None:
        batch = pyg.graphics.Batch()
    window_size = window.get_size()
    elements_count = len(bargraph.array)
    elements_minimum = min(bargraph.array)
    elements_maximum = max(bargraph.array)
    bar_width = window_size[0] / elements_count - bargraph.margin - (bargraph.margin / elements_count)
    v0, v1, v2, v3 = (0, 0), (0, 0), (0, 0), (0, 0)

    do_once = True
    for i in range(0, len(bargraph.array)):

        element_value = bargraph.array[i]
        element_color = bargraph.color[i]

        if do_once:
            # Don't 'indent' first bar

            # Follow OpenGL CCW rules:
            # top left
            v0 = (v0[0] + bargraph.margin,
                  window_size[1] * (element_value / elements_maximum) - bargraph.margin)
            # bottom left
            v1 = (v0[0],
                  0 + bargraph.margin)
            # bottom right
            v2 = (v0[0] + bar_width,
                  0 + bargraph.margin)
            # top right
            v3 = (v0[0] + bar_width,
                  window_size[1] * (element_value / elements_maximum) - bargraph.margin)
            do_once = False
        else:
            # top left
            v0 = (v0[0] + bargraph.margin + bar_width,
                  window_size[1] * (element_value / elements_maximum) - bargraph.margin)
            # bottom left
            v1 = (v0[0],
                  0 + bargraph.margin)
            # bottom right
            v2 = (v0[0] + bar_width,
                  0 + bargraph.margin)
            # top right
            v3 = (v0[0] + bar_width,
                  window_size[1] * (element_value / elements_maximum) - bargraph.margin)


        batch.add(4, pyg.gl.GL_QUADS, None,
                  ('v2f', [v0[0], v0[1], v1[0], v1[1],
                           v2[0], v2[1], v3[0], v3[1]]),
                   ('c3f', element_color*4)
                   )

    return batch