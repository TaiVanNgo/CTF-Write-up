# Roboto Sans
Author: Tai

## Description
The flag is somewhere on this web application not necessarily on the website. Find it. Check this out.

## Writeups
I tried to download the whole website again, using `wget -r [link to website]`

I got the folder, when I try to find the `pico` in the whole folder using `grep pico -r *`, but it returns nothing. I tried to discover the folder. when access the folder, I see the robots.txt, it contiains the hint inside that. 

The [robots.txt](https://www.seobility.net/en/wiki/Robots.txt?utm_id=8783357192_87472061646&utm_source=google&utm_medium=cpc&utm_cid=8783357192&utm_agid=87472061646&utm_campaign=geoEN-Wiki&utm_dev=c&utm_devicemodel=&utm_mt=e&utm_term=robots%20txt&gad_source=1&gclid=EAIaIQobChMIhtW24Kq9hwMV7NQWBR02ih9uEAAYASAAEgLamfD_BwE) is the file that instructs the bots (mostly the search engine crawlers). It defines which area of the website are allowed or not allowed to access. 

The content of the `robots.txt`

```
User-agent *
Disallow: /cgi-bin/
Think you have seen your flag or want to keep looking.

ZmxhZzEudHh0;anMvbXlmaW
anMvbXlmaWxlLnR4dA==
svssshjweuiwl;oiho.bsvdaslejg
Disallow: /wp-admin/
```

I noitced the `==` in the end of these weird characters, I knew this is a base64 encryption -> I use the base64 decoded online to decrypt it.
This is the result I got `js/myfile.txt`

Then I tried to access this directory on the website and I got the flag.
Directory: `http://saturn.picoctf.net:57862/js/myfile.txt`
Flag: picoCTF{Who_D03sN7_L1k5_90B0T5_22ce1f22}