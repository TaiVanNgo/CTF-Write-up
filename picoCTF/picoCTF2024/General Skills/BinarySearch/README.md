# Binary Search
Author: Tai Ngo

## Description
Author: Jeffery John

Want to play a game? As you use more of the shell, you might be interested in how they work! Binary search is a classic algorithm used to quickly find an item in a sorted list. Can you find the flag? You'll have 1000 possibilities and only 10 guesses. Cyber security often has a huge amount of data to look through - from logs, vulnerability reports, and forensics. Practicing the fundamentals manually might help you in the future when you have to write your own tools! You can download the challenge files here:z

## Writeups

Apply the binary search by hand to get the flag

First iteration: (0 + 1000)/2 = 500

if it's smaller -> use 500 as the max value, then we use (0 + 500) / 2. And apply the same process for following gueses

if it's larger -> use 500 as the min value, then we calculate (500 + 1000) / 2. And apply the same process for following gueses
