from typing import List


class Leap:
    @staticmethod
    def check(metai) -> bool:
        return (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0)

    @staticmethod
    def range(nuo, iki) -> List[int]:
        sarasas = []
        for metai in range(nuo, iki):
            if (metai % 400 == 0) or (metai % 100 != 0 and metai % 4 == 0):
                sarasas.append(metai)
        return sarasas


if __name__ == "__main__":
    print(Leap.check(2020))
