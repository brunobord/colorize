#!/usr/bin/env python
#-*- coding: utf-8 -*-


import color, termcolors

def test_colors():
    style = color.color_style()
    style.ERROR = termcolors.make_style(fg='red', opts=('bold',))
    style.INFO = termcolors.make_style(fg='blue')
    style.OK = termcolors.make_style(fg='green')
    style.WARNING = termcolors.make_style(fg='yellow')

    print style.ERROR('I am red and bold')
    print style.INFO('I am blue')
    print style.OK('I am green')
    print style.WARNING('I am yellow')

if __name__ == '__main__':
    test_colors()
