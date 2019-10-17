#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division             # Division in Python 2.7
from matplotlib import colors
import numpy as np
from matplotlib import rc
import matplotlib.pyplot as plt
import matplotlib
# So that we can render files without GUI

STEPS = 1024

matplotlib.use('Agg')


def plot_color_gradients(gradients, names):
    # For pretty latex fonts (commented out, because it does not work on some machines)
    # rc('text', usetex=True)
    # rc('font', family='serif', serif=['Times'], size=10)
    rc('legend', fontsize=10)

    column_width_pt = 400         # Show in latex using \the\linewidth
    pt_per_inch = 72
    size = column_width_pt / pt_per_inch

    fig, axes = plt.subplots(nrows=len(gradients),
                             sharex=True, figsize=(size, 0.75 * size))
    fig.subplots_adjust(top=1.00, bottom=0.05, left=0.25, right=0.95)

    for ax, gradient, name in zip(axes, gradients, names):
        # Create image with two lines and draw gradient on it
        img = np.zeros((2, 1024, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v)

        im = ax.imshow(img, aspect='auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)

        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3]/2.
        fig.text(x_text, y_text, name, va='center', ha='left', fontsize=10)

    fig.savefig('my-gradients.png')


def hsv2rgb(h, s, v):
    # TODO
    return (h, s, v)


def gradient_rgb_bw(v):
    return (v, v, v)


def gradient_rgb_gbr(v):
    step = int(v * STEPS) - 1

    green = np.concatenate((np.linspace(1, 0, STEPS/2), np.linspace(0, 0, STEPS/2)))
    blue = np.concatenate((np.linspace(0, 0, STEPS/4), np.linspace(0, 1, STEPS/4), np.linspace(1, 0, STEPS/4), np.linspace(0, 0, STEPS/4)))
    red = np.concatenate((np.linspace(0, 0, STEPS/2), np.linspace(0, 1, STEPS/2)))

    return (red[step], green[step], blue[step])


def gradient_rgb_gbr_full(v):
    step = int(v * STEPS) - 1

    # red = np.linspace(0, 1, STEPS)
    red = np.concatenate((
        np.linspace(0, 0, STEPS/2),
        np.linspace(0, 1, STEPS/4),
        np.linspace(1, 1, STEPS/4)
    ))

    green = np.concatenate((
        np.linspace(1, 1, STEPS/4),
        np.linspace(1, 0, STEPS/4),
        np.linspace(0, 0, STEPS/2)
    ))
    # green = np.linspace(1, 0, STEPS)
    # blue = np.concatenate((np.linspace(0, 1, STEPS/2), np.linspace(1, 0, STEPS/2)))
    blue = np.concatenate((
        np.linspace(0, 1, STEPS/4),
        np.linspace(1, 1, STEPS/2),
        np.linspace(1, 0, STEPS/4)
    ))

    print(step, red[step], green[step], blue[step])

    return (red[step], green[step], blue[step])


def gradient_rgb_wb_custom(v):
    # TODO
    return (0, 0, 0)


def gradient_hsv_bw(v):
    # TODO
    return hsv2rgb(0, 0, 0)


def gradient_hsv_gbr(v):
    # TODO
    return hsv2rgb(0, 0, 0)


def gradient_hsv_unknown(v):
    # TODO
    return hsv2rgb(0, 0, 0)


def gradient_hsv_custom(v):
    # TODO
    return hsv2rgb(0, 0, 0)


if __name__ == '__main__':
    def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])
