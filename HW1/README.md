Project: HW1 Dinner Party
Class: PSU CS 441/541 - Artificial Intelligence (Fall 2019)
Author: Prathik Sannecy
Date: 10/21/19

This project provides a solution to the HW1 Dinner Party problem (see HW1ProjectDescription). Basically, given a set of people, it will optomize the seating arrangement at the dinner table to achieve the maximum score.

For optomizing, I used a greedy algorithm. I sorted the people by whose position gave the lowest score (individually). Then, I started swapping people's positions in that order until I exhausted all combinations.

To run this program:
python3 src/DinnerPartyMain.py

The output is sent to stdout, you may redirect it to another file from the terminal.

Example input files are in the Input_Files directory, to use them at the prompt enter:
Input_Files/hw1-inst1.txt
or whichever input file you'd like to use