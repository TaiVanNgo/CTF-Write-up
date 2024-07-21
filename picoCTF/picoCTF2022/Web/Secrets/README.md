# Secrets
Author: Tai

## Description
Author: Geoffrey Njogu

We have several pages hidden. Can you find the one with the flag? The website is running here.

## Writeup

The challenge gives me a website, when I checked to the page source, I saw there's a image from the `secret/assets`, I tried to connect to that directories, but got nothing, I tried go to `secret/` and there's a label said that "Finally. You almost found me. you are doing well", I knew that I am on right track, I see there's also a link to `hidden/file.css`, I agained access teh `hidden` directoy to check is there any flag, and realize there's a `/superhidden` and I got the flag

The secret directory to get the flag
`http://saturn.picoctf.net:59556/secret/hidden/superhidden/`

FLAG: picoCTF{succ3ss_@h3n1c@10n_39849bcf}