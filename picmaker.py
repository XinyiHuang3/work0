#! /usr/bin/python

import sys

f = open("image.ppm", "w+")
header = "P3\n500 500\n255\n"
f.write(header)

  
for i in range(500):
    for j in range(500):
	if i %25 == 0 or j%25 == 0:
		f.write("0 0 0\n")
	else: 
		
		f.write(str(i % 250) + " " + str(j % 250) + " " +  str(i+j% 250) + "\n")

f.close()