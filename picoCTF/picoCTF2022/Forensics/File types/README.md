# File types
Author: Tai Ngo

## Description
Author: Geoffrey Njogu

This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can. You can download the file from here.

## Writeups

When I read the content of the `.pdf` file, it looks like some bash code, so I tried to run it. Of course I granted permission to the file, using `chmod +x Flag.pdf`. Then I can execute it using `./Flag.pdf`. It return a file, I use `file` to chekc the file type. 

At this step just follow these step
1. Check the file type (using `file [name of file]`). 
2. They are all the compress files, we need to find the way to decompress or extract it. Search on the internet to find the appropriate tools. Notice that there are few files that have to be exactly renamed to the appropriate extension to decompress. For example like the `.cpio` file. Using `mv [oldfile] [newNameFile]` to rename the file.

At the very last step, I extracted a file ascii value, phewww, finally. This is a hex text, just use convert online tool to convert it back to normal text. Then we got the flag.

Flag: picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}