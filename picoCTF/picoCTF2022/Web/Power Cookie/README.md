# Power Cookie
Author: Tai Ngo

## Description
Author: LT 'syreal' Jones
Can you get the flag?

Additional details will be available after launching your challenge instance.

## Writeup
When I clicked the button and observe the traffic, I regconize there's a file `check.php`, the cookies contain `isAdmin: '0'`. Then I know that if we can manipulate this to `true`, we can get the flag. I went to the `storage`, access cookie and modify that, then I achieved the flag when refershed the page.

Flag: picoCTF{gr4d3_A_c00k13_0d351e23}
