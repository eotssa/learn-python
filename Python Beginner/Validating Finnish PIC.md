Programming exercise:
Valid PIC?
Points:
0

---

In this exercise you will validate Finnish Personal Identity Codes (PIC).

Please write a function named `is_it_valid(pic: str)`, which returns `True` or `False` based on whether the PIC given as an argument is valid or not. Finnish PICs follow the format `ddmmyyXyyyz`, where `ddmmyy` contains the date of birth, `X` is the marker for century, `yyy` is the personal identifier, and `z` is a control character.

The program should check the validity by these three criteria:

1. The first half of the code is a valid, existing date in the format `ddmmyy`.
2. The century marker is either `+` (1800s), `-` (1900s), or `A` (2000s).
3. The control character is valid.

The control character is calculated by taking the nine-digit number created by the date of birth and the personal identifier, dividing this by 31, and selecting the character at the index specified by the remainder from the string `0123456789ABCDEFHJKLMNPRSTUVWXY`. For example, if the remainder was 12, the control character would be `C`.

More examples and explanations of the uses of the PIC are available at the [Digital and Population Data Services Agency](https://dvv.fi/en/personal-identity-code).

NB! Please make sure you do not share your own PIC, for example in the code you use for testing or through the course support channels.

Here are some valid PICs you can use for testing:

- 230827-906F
- 120488+246L
- 310823A9877

--------------


```python

import datetime

#ddmmyyXyyyz
def is_it_valid(pic: str) -> bool:
    
    if len(pic) != 11: 
        return False
    
    # + (1800s), - (1900s) or A (2000s).
    if pic[6] not in ["-", "+", "A"]:
        return False

    # solves the issue for ambigious datetime, since we only parse the xxXX years 
    dct = {}
    dct["+"] = "18"
    dct["-"] = "19"
    dct["A"] = "20"

    try: 
        #day, month, year for pic format --   ddmmyy 10 04 00
        #datetime format is year, month, day 
        is_valid = datetime.datetime(int(dct[pic[6]] + pic[4:6]), int(pic[2:4]), int(pic[:2]))
    except: 
        return False

    
    # nine-digit number created by the date of birth and the personal identifier

    try: 
        nine_digit = int(pic[0:6] + pic[7:10])
    except:
        #value error if not all digits
        return False
    remainder = nine_digit % 31 

    str_ident = "0123456789ABCDEFHJKLMNPRSTUVWXY"

    if pic[10] != str_ident[remainder]:
        return False
    
    return True

```