# second, basic tasks with lists.


def max_list (lst:list) -> int:
    return(max(lst))    


def list_append(lst:list) -> list:
   lst.append("test")
   return lst


def count_list(lst:list) -> int:
   return(len(lst))


def count_freq_item_list(my_list):
    count_freq = my_list.count(1)
    return count_freq


if __name__ == "__main__":
    print(f"It is List module!")
















