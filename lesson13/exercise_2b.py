# first, to do basic tasks with strings


def lower_text(text:str) -> str :
    return text.casefold()


def upper_text(text:str) -> str :
    return text.upper()


def contrary_text(text:str) -> str :
    return text[::-1]


def split_text(text:str) -> str :
    return text.split()


def replace_text(text:str) -> str:
    return text.replace("dont","really")


def combining_text(text1:str, text2:str) -> str:
   text = text1 + text2
   return text


def leet_text(text:str) -> str:
    replacement = (('A','4'),('b','6'),('d','|>'),('e','3'),('o','0'),('s','5'),('t','7'),('i','1'),('n',"|\|"),('u','|_|'),('z','2'))
    leet = text
    for old,new in replacement:
        leet = leet.replace(old,new)
    return(leet)

if __name__ == "__main__":
    print(f"It is String module!")


















