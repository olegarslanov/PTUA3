# Create a class method to return the reversed string of a given string.


class Stringa:
    def __init__(self, sentence: str):
        self.sentence = sentence

    def __str__(self):
        return self.sentence

    @classmethod
    def get_reverse_string(cls, sentence: str) -> "Stringa":
        return cls(sentence[::-1])


print(Stringa.get_reverse_string("I love"))


# instance metodu
# class Stringa:
#     def __init__(self, sentence: str) -> None:
#         self.sentence = sentence

#     def get_reverse_string(self):
#         self.sentence = self.sentence[::-1]
#         return self.sentence


# string1 = Stringa("I love life")
# print(string1.get_reverse_string())
