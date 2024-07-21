# Search source
Author: Tai

## Description
Author: Mubarak Mikail

The developer of this website mistakenly left an important artifact in the website source, can you find it? The website is here

## Writeups

In this challenge, I read the hint, I decided to download this website to my machine by using `wget -r [link of the website]`, I tried to use `wget [link of the website]` first, but it only downloaded 1 file `index.html`, we need to download recursively, that's why we use `-r`, then we got the folder, I use the `grep` recursively and find the flag easily.

The command: `grep pico -R *` 

Flag: picoCTF{1nsp3ti0n_0f_w3bpag3s_587d12b8}