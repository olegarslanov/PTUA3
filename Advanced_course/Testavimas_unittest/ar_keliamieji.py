def ar_keliamieji(metai) -> bool:
    if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
        return True
    else:
        return False


if __name__ == "__main__":
    print(ar_keliamieji(2000))
    print(ar_keliamieji(2020))
    print(ar_keliamieji(2100))
