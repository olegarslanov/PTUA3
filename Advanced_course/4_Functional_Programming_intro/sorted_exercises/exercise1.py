# Write a Python program to sort a list of tuples using Lambda. Original list of tuples:
# [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90),
# ('Maths', 97)]


a = [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]

print(sorted(a, key=lambda x: x[1]))
a.sort(key=lambda x: x[1])
print(a)

print(a[0])
print(a[0][1])
