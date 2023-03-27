#  Объявите класс с именем TravelBlog и объявите в нем атрибут:

# total_blogs: 0
# Создайте экземпляр этого класса с именем tb1, сформируйте в нем два локальных свойства:

# name: 'Франция'
# days: 6
# Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.

# Создайте еще один экземпляр класса TravelBlog с именем tb2, сформируйте в нем два
# локальных свойства:

# name: 'Италия'
# days: 5

# Увеличьте значение атрибута total_blogs класса TravelBlog еще на единицу.
# P.S. На экран ничего выводить не нужно.


class TravelBlog:
    total_blogs = 0


print(TravelBlog.__dict__)

tb1 = TravelBlog()
print(tb1.__dict__)
tb1.name = "Франция"
tb1.days = 6
print(tb1.__dict__)
print(TravelBlog.__dict__)

setattr(TravelBlog, "total_blogs", 1)
print(TravelBlog.__dict__)

tb2 = TravelBlog()
tb2.name = "Италия"
tb2.days = 5

setattr(TravelBlog, "total_blogs", 2)
print(TravelBlog.__dict__)
