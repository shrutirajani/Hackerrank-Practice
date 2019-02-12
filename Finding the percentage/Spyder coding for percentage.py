#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:13:18 2019

@author: shrutirajani
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        record = input().split()
        name, marks = record[0], record[1:]
        marks = list(map(float, marks))
        student_marks[name] = marks
    query = input()
    print('{0:.2f}'.format(*[(sum(scores)/len(scores)) for name, scores in 
student_marks.items() if name == query]))
