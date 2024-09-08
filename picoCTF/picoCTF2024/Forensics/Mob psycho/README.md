# Mob psycho

Author: Tai Ngo

## Description
Author: NGIRIMANA Schadrack

Can you handle APKs? Download the android apk here. 


## Writeups
THis challenge provides us a `.apk` file. I can unzip that by using `unzip`. It extracts a lot of data, but I can easily find the file named `flag.txt`.

I used `ls -alR * | more` -> I can list all the file in the big folder,

The `flag.txt` contains the hex string, I converted it into characters then I got the flag.


FLAG: picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_85dbd215}

