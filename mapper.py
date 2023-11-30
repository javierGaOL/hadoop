#!/usr/bin/python
import sys

for line in sys.stdin:
    if count("\t")=5 in line:
        data = line.strip().split("\t")
        date, time, store, item, cost, payment = data
        print(store+"\t"+cost)