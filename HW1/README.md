Project: HW1 Dinner Party
Class: PSU CS 441/541 - Artificial Intelligence (Fall 2019)
Author: Prathik Sannecy
Email: prathik@pdx.edu
Date: 10/21/19

This project provides a solution to the HW1 Dinner Party problem (see HW1ProjectDescription). Basically, given a set of people, it will optimize the seating arrangement at the dinner table to achieve the maximum score.

For optimizing, I used a local state space search. I sorted the people by whose position gave the lowest score (individually). Then, I started swapping people's positions in that order until I exhausted all combinations in this order.
In the end, this returns a local maximum. Although it may not be the absolute maximum, it runs very quickly (within a few seconds), and gives results close to the absolute max.
I tried adding some randomization in an effort to find the absolute max, but in the end, it didn't help at all and I got back the exact same results (but taking a longer time).

Results on my Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz machine (Ubuntu):
instance1: 96 (almost instantaneously)
instance2: 541 (about 3 seconds)
instance3: 161 (about 3 seconds)

To run this program:
python3 DinnerPartyMain.py

The output is sent to stdout, you may redirect it to another file from the terminal.

Example input files are in the Input_Files directory, to use them at the prompt enter:
Input_Files/hw1-inst1.txt
or whichever input file you'd like to use

