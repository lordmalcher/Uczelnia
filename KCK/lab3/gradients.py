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
    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    r = 0
    g = 0
    b = 0

    if h >= 0 and h < 60:
        r = c
        g = x
        b = 0
    if h >= 60 and h < 120:
        r = x
        g = c
        b = 0
    if h >= 120 and h < 180:
        r = 0
        g = c
        b = x
    if h >= 180 and h < 240:
        r = 0
        g = x
        b = c
    if h >= 240 and h < 300:
        r = x
        g = 0
        b = c
    if h >= 300 and h < 360:
        r = c
        g = 0
        b = x     

    r, g, b = (r + m, g + m, b + m)

    return (r, g, b)


def gradient_rgb_bw(v):
    return (v, v, v)

RED_GBR = np.concatenate((
    np.linspace(0, 0, STEPS/2),
    np.linspace(0, 1, STEPS/2)
    ))
GREEN_GBR = np.concatenate((
    np.linspace(1, 0, STEPS/2),
    np.linspace(0, 0, STEPS/2)
    ))
BLUE_GBR = np.concatenate((
    np.linspace(0, 0, STEPS/4),
    np.linspace(0, 1, STEPS/4),
    np.linspace(1, 0, STEPS/4),
    np.linspace(0, 0, STEPS/4)
    ))

def gradient_rgb_gbr(v):
    step = int(v * STEPS) - 1

    return (RED_GBR[step], GREEN_GBR[step], BLUE_GBR[step])

RED_GRB_FULL = np.concatenate((
    np.linspace(0, 0, STEPS/2),
    np.linspace(0, 1, STEPS/4),
    np.linspace(1, 1, STEPS/4)
))
GREEN_GRB_FULL = np.concatenate((
    np.linspace(1, 1, STEPS/4),
    np.linspace(1, 0, STEPS/4),
    np.linspace(0, 0, STEPS/2)
))
BLUE_GRB_FULL =np.concatenate((
    np.linspace(0, 1, STEPS/4),
    np.linspace(1, 1, STEPS/2),
    np.linspace(1, 0, STEPS/4)
))

def gradient_rgb_gbr_full(v):
    step = int(v * STEPS) - 1

    return (RED_GRB_FULL[step], GREEN_GRB_FULL[step], BLUE_GRB_FULL[step])

RED_WB_CUSTOM = np.concatenate((
    np.linspace(1, 1, STEPS/4),
    np.linspace(1, 0, STEPS/8),
    np.linspace(0, 0, STEPS/4),
    np.linspace(0, 1, STEPS/8),
    np.linspace(1, 1, STEPS/8),
    np.linspace(1, 0, STEPS/8)
))
GREEN_WB_CUSTOM = np.concatenate((
    np.linspace(1, 0, STEPS/8),
    np.linspace(0, 0, STEPS/4),
    np.linspace(0, 1, STEPS/8),
    np.linspace(1, 1, STEPS/4), 
    np.linspace(1, 0, STEPS/8), 
    np.linspace(0, 0, STEPS/8),      
))
BLUE_WB_CUSTOM = np.concatenate((
    np.linspace(1, 1, STEPS/2),
    np.linspace(1, 0, STEPS/8),
    np.linspace(0, 0, 3*STEPS/8),
))

def gradient_rgb_wb_custom(v):
    step = int(v * STEPS) - 1

    return (RED_WB_CUSTOM[step], GREEN_WB_CUSTOM[step], BLUE_WB_CUSTOM[step])

V_BW = np.linspace(0, 1, STEPS)

def gradient_hsv_bw(v):
    step = int(v * STEPS) - 1

    return hsv2rgb(0, 0, V_BW[step])

H_GBR = np.linspace(120, 360, STEPS)

def gradient_hsv_gbr(v):
    step = int(v * STEPS) - 1

    s = 1
    v = 1

    return hsv2rgb(H_GBR[step], s, v)

H_UNKNOWN = np.linspace(120, 0, STEPS)

def gradient_hsv_unknown(v):
    step = int(v * STEPS) - 1

    s = 0.5
    v = 1

    return hsv2rgb(H_UNKNOWN[step], s, v)

H_CUSTOM = np.linspace(0, 360, STEPS)
S_CUSTOM = np.linspace(0.25, 0.75, STEPS)
V_CUSTOM = np.linspace(0.5, 1, STEPS)

def gradient_hsv_custom(v):
    step = int(v * STEPS) - 1

    return hsv2rgb(H_CUSTOM[step], S_CUSTOM[step], V_CUSTOM[step])


if __name__ == '__main__':
    def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])
