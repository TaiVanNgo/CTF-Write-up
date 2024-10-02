# The Numbers
Author: Tai Ngo

## Description
Author: Danny

The numbers... what do they mean?

## Writeups 

This challenge provides me with the imgage of number, the hint indicates that the flag are encrypted to the number.

In python, we use the `string.ascii_uppercase[]`, but it started from 0, for example: `string.ascii_uppercase[0]` returns `"A"`, so we need to minus one to extract the flag

Flag; PICOCTF{THENUMBERSMASON}