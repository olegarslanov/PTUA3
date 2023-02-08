
#print()
# print(object(s), sep=separator, end=end, file=file, flush=flush)

print("hello world")

print("hello", "world")

print(*["hello", "world"])

print("hello world", sep=",")

print("hello", "world", sep=" amazing ")

print('hello world') == str, True


#type()
a='alibaba'
print(type(a))

if type(a) == str:
    print('This is a text')

print(type(1) == str)


# len()
print(type(len(['a',2,"c"])), 'Mindaugas', sep='-')


#round()
print(round(1.999))
print(round(1.5555, 2))


#sorted()
# sorted(iterable, key=None, reverse=False)
money_list =['a','c','f','Antanas', 'Martynas']
print(sorted(money_list, key=None, reverse=True))



