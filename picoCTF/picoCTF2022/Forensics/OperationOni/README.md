# Operation Oni
Author: Ngo Van Tai

## Description

Author: LT 'syreal' Jones

Download this disk image, find the key and log into the remote machine. Note: if you are using the webshell, download and extract the disk image into /tmp not your home directory.

Remote machine: ssh -i key_file -p 55494 ctf-player@saturn.picoctf.net

## Writeups

With this challenge, it seems like I need to find the key_file in the provided disk image. 

I used `autopsy` and discover the img, then I got the private key, I exported it and `chmod 600` to the private key file, then I access to the machine with the key file, then I got the flag.