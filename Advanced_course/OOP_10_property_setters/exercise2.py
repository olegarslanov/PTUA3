# Write a User class that has a password property. The password property should be a computed
#  property that checks whether the password is strong enough. A password is considered strong
#  if it has at least 8 characters, contains at least one uppercase letter, one lowercase letter,
#  and one number.


class User:
    def __init__(self):
        self.password = password

    @property
    def password(self):
        return self.__weight

    @password.setter
    def lenght(self, lenght):
        if lenght >= 8:
            raise ValueError("negative weight")
        self.__weight = new_weight


b = Box()
b.weight = 100
print(b.weight)  # 100
b.weight = -10  # ValueError
