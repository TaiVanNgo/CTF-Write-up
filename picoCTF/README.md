# <span style="color:#ff0000">Some useful tools for the picoCTF</span>

## Forensics

Can use for image (png, jpg)

- `hexeditor` -> see header file
- `exiftool` -> Discover metadata
- `file` -> see the file type
- `strings -10` (-10 -> only return the results which has at least 10 characters)
- `binwalk`
- `wireshark` or `tshark -nr [file]`
- `zsteg` -> Find hidden files in `bmp`
- `ls -alR [file] | more` (remember to use more)
-> List all the files in a big folder  
- `grep [keyword] -R *` -> grep keywords in the big folder
- `steghide extract -sf [file] -p [password]`
  Others
- `sha256sum` [what is SHA-256 checksum](./Others/what%20is%20SHA-256%20checksum.md)
- `pdftotext` -> try with pdf file, we may be extract some redacted text
- `fcrackzip -b -D -p [path-to-word-list] -u [file.zip]` -> Using this to crack the password of a Zip file

## Reverse Engineering

- `Strings -10` (-10 -> only return the results which have at least 10 characters)
- `Ghidra` -> used to reverse the code
- `upx-ucl` -d [file] -> To decompress a upx file
- `autopsy` (if cannot run try `sudo autopsy`) -> use to discover the autospy

## Web 
- `wget -r [link to website]`: Download all the files from a website
- `grep [word] -r *`: Find recursively
- Check the `robots.txt` directory
