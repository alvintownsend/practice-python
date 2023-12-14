#!/usr/bin/env python3
import math
import random
import string
import time

def is_palindrome_slow(palindrome:str) -> bool:
    """ Detects if the string is a valid palindrome.
    Uses Python to reverse the string into a char array and join it back together.
    """
    return palindrome == "".join(reversed(palindrome))

def is_palindrome_fast(palindrome:str) -> bool:
    """ Detects if the string is a valid palindrome.
    Uses the "Pythonic Way".
    """
    return palindrome == palindrome[::-1]

def is_palindrome_custom(palindrome:str) -> bool:
    """ Detects if the string is a valid palindrome.
    Splits the string and checks the beginning of the left to the end of the right, going inwards.
    """
    half_length = math.floor(len(palindrome) / 2)
    position = 0
    while position < half_length:
        backwards_position = -position - 1
        print(f"[{backwards_position}:{backwards_position - 4}]")
        print(f"{palindrome[position:position + 4]}, {palindrome[backwards_position:backwards_position - 4]}")
        if palindrome[position:position + 4] != palindrome[backwards_position:backwards_position - 4]:
            return False 
        position += 1
    return True

def is_palindrome_custom_as_list(palindrome:str) -> bool:
    """ Detects if the string is a valid palindrome.
    Try converting the String to a list and operate on that.
    """
    # palindrome = list(palindrome)
    palindrome = [*palindrome]
    half_length = math.floor(len(palindrome) / 2)
    position = 0
    while position < half_length:
        if palindrome[position] != palindrome[-position - 1]:
            return False 
        position += 1
    return True

def is_palindrome_custom_as_bytes(palindrome:str) -> bool:
    """ Detects if the string is a valid palindrome.
    Try converting the String to a list and operate on that.
    """
    # palindrome = list(palindrome)
    palindrome = bytes(palindrome, 'utf-8') 
    half_length = math.floor(len(palindrome) / 2)
    position = 0
    while position < half_length:
        if palindrome[position] != palindrome[-position - 1]:
            return False 
        position += 1
    return True

def timer(func:callable, palindrome:str, name:str, count:int, expects:bool) -> None:
    """ Prints the time it takes to execute the given method.
    """
    tic = time.perf_counter()
    print(f"calling {func.__name__} with a {name}: {count} times of {len(palindrome)} length")
    result = True
    for _ in range(1, count):
       result = result and func(palindrome)
    toc = time.perf_counter()
    print(f"time: {toc - tic:0.4f} seconds")
    if result is not expects:
        print(f"expecting {expects} but got {result}")
    print()

if __name__ == "__main__":
    count = 100000
    half_palindrome_length = 1000
    palindrome_front = "".join(random.choice(string.ascii_lowercase) for _ in range(half_palindrome_length))
    palindrome_back = palindrome_front[::-1]
    palindrome = palindrome_front + palindrome_back
    palindrome_uneven = palindrome_front + "x" + palindrome_back
    non_palindrome_different_mid = palindrome_front + "az" + palindrome_back
    non_palindrome_different_ends = "a" + palindrome_front + palindrome_back + "z"

    # timer(is_palindrome_slow, palindrome, "palindrome", count, True)
    # timer(is_palindrome_fast, palindrome, "palindrome", count, True)
    timer(is_palindrome_custom, palindrome, "palindrome", count, True)
    # timer(is_palindrome_custom_as_list, palindrome, "palindrome", count, True)
    # timer(is_palindrome_custom_as_bytes, palindrome, "palindrome", count, True)

    # timer(is_palindrome_slow, palindrome_uneven, "uneven palindrome", count, True)
    # timer(is_palindrome_fast, palindrome_uneven, "uneven palindrome", count, True)
    # timer(is_palindrome_custom, palindrome_uneven, "uneven palindrome", count, True)
    # timer(is_palindrome_custom_as_list, palindrome_uneven, "uneven palindrome", count, True)
    # timer(is_palindrome_custom_as_bytes, palindrome_uneven, "uneven palindrome", count, True)

    # timer(is_palindrome_slow, non_palindrome_different_mid, "non-palindrome, different middle", count, False)
    # timer(is_palindrome_fast, non_palindrome_different_mid, "non-palindrome, different middle", count, False)
    # timer(is_palindrome_custom, non_palindrome_different_mid, "non-palindrome, different middle", count, False)
    # timer(is_palindrome_custom_as_list, non_palindrome_different_mid, "non-palindrome, different middle", count, False)
    # timer(is_palindrome_custom_as_bytes, non_palindrome_different_mid, "non-palindrome, different middle", count, False)
    
    # timer(is_palindrome_slow, non_palindrome_different_ends, "non-palindrome, different edges", count, False)
    # timer(is_palindrome_fast, non_palindrome_different_ends, "non-palindrome, different edges", count, False)
    # timer(is_palindrome_custom, non_palindrome_different_ends, "non-palindrome, different edges", count, False)
    # timer(is_palindrome_custom_as_list, non_palindrome_different_ends, "non-palindrome, different edges", count, False)
    # timer(is_palindrome_custom_as_bytes, non_palindrome_different_ends, "non-palindrome, different edges", count, False)

