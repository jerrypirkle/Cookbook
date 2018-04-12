#https://www.youtube.com/watch?v=DQBlq45c1T4
def decode(encodedNum):
    """The Barksdale Code (Transposition Cipher) from The Wire:
    Jump to the other side of the 5 on the keypad, and swap 5's and 0's."""
    trans = {
    "1":"9", "2":"8", "3":"7",
    "4":"6", "5":"0", "6":"4",
    "7":"3", "8":"2", "9":"1",
    "0":"5"}
    prezbod  = ""
    for i in encodedNum:
        prezbod += trans[i]
    return prezbod
