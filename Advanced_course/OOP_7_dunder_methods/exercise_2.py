# Create a class called MyQueue that has __bool__, __repr__ and __len__ methods defined.

# The __bool__ method should return True if the queue has any items and False if it is empty.
# The __repr__ method should return a string in the format MyQueue(items) where items is the
# list of items in the queue.
# The __len__ method should return the number of items in the queue.


class MyQueue:
    def __init__(self, items: list):
        self.items = items

    def __bool__(self):
        return bool(self.items)

    def __repr__(self):
        return f"MyQueue({self.items})"

    def __len__(self) -> int:
        return len(self.items)


queue = MyQueue([1, 2, 3, 4])

print(bool(queue))
print(repr(queue))
print(len(queue))


# 2
class MyQueue:
    def __init__(self):
        self.items = []

    def __bool__(self):
        return bool(self.items)

    def __repr__(self):
        return f"MyQueue({self.items})"

    def __len__(self):
        return len(self.items)


q = MyQueue()
q.items.append(1)
q.items.append(2)
print(bool(q))  # True
print(repr(q))  # MyQueue([1, 2])
print(len(q))  # 2
