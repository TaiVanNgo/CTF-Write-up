# Pickle Rick
```
export IP=10.10.106.86
```

# Nmap 
```
	nmap -sC -sV -oN nmap/initial 10.10.106.86
```

Use nikto scan
`nikto -h http://$IP | tee nikto.log`
we can use the `$IP` as I use the commmand of export IP=10.10.106.86, we just simply use the $IP

use gobuster (brute-force attack)




# Task 1
1. What is the first ingredient that Rick needs?

```
R1ckRul3s
```

```
Wubbalubbadubdub
```
to see the content of the 2 files .txt, we use this command
while read line; do echo $line;done < clue.txt
while read line; do echo $line;done < Sup3rS3cretPickl3Ingred.txt
or we can use:
grep . clue.txt
grep . Sup3rS3cretPickl3Ingred.txt

Answer: mr. meeseek hair

2. What is the second ingredient that Rick needs?

Vm1wR1UxTnRWa2RUV0d4VFlrZFNjRlV3V2t0alJsWnlWbXQwVkUxV1duaFZNakExVkcxS1NHVkliRmhoTVhCb1ZsWmFWMVpWTVVWaGVqQT0
some weird base64 character

use base64 -d to decrypt this 

after a while, we have the "rabbit hole"
```
echo Vm1wR1UxTnRWa2RUV0d4VFlrZFNjRlV3V2t0alJsWnlWbXQwVkUxV1duaFZNakExVkcxS1NHVkliRmhoTVhCb1ZsWmFWMVpWTVVWaGVqQT0== | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d | base64 -d
base64: invalid input
base64: invalid input
rabbit hole      

```


To get this answer, we use `less /home/rick/"second ingredients"`

ANSWER: 1 jerry tear

3. What is the last and final ingredient?

sudo less /root/3rd.txt
Answer: fleeb juice

