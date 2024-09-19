# interencdec
Author: Tai Ngo

## Description
Author: NGIRIMANA Schadrack

Can you get the real meaning from this file. Download the file here. 

## Writeups

The challenge provided us with a base64 encoded (I saw the `==` in the end of the string), then I decode it, it returns an another base64 encoded message, I then decoded it one more time. Now it return the string have the same pattern with our flag.

I regconized that it is Ceasar, I use the [decoder online](https://www.dcode.fr/caesar-cipher) to solve this.

FLAG: picoCTF{caesar_d3cr9pt3d_ea60e00b}