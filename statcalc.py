import numpy as np
import string
n = input("how many samples? ")
samples = []


for N in n:
    N= input("how many in each population?")
    for x, i in N:
        x = int(input(f"x {i}: "))
        sample = []
        sample += x
        samples +=sample