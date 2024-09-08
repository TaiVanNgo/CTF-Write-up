# hideme
Author: Tai Ngo


## Description
Author: Geoffrey Njogu

Every file gets a flag. The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye here.

## Writeup
when I tried `strings` it first, I see the text like `secret/UT`, `secret/flag.pngUT`. I think this might be a hidden file inside this file. 

Using `binwalk` to extract the zip data in the file. 

`binwalk -e flag.png`

I can extract a folder, and the `secret` folder is in the extracted folder. The image in that folder contains the flag


FLAG: picoCTF{Hiddinng_An_imag3_within_@n_ima9e_dc2ab58f}