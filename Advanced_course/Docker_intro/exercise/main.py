# Google is launching a network of autonomous pizza delivery drones and wants you to create a
# flexible rewards system (Pizza Points™) that can be tweaked in the future. The rules are
# simple: if a customer has made at least N orders of at least Y price, they get a FREE pizza!
# Create a function that takes a dictionary of customers, a minimum number of orders and a
# minimum order price. Return a list of customers that are eligible for a free pizza.


uzsakym_dict = {
    "client1": {"Oleg": {"order1": 10.00, "order2": 12, "order3": 6, "order4": 15}},
    "client2": {"Tauras": {"order1": 15, "order2": 5.30, "order3": 6, "order4": 9}},
    "client3": {"Arturas": {"order1": 10, "order2": 12, "order3": 10.25}},
    "client4": {
        "Vytautas": {"order1": 20, "order2": 14, "order3": 9.80, "order4": 18.20}
    },
}


# # praeinam per raktus 1 lygio dict
# for client in uzsakym_dict.keys():
#     uzsakym_suma = []
#     # praeinam per raktus 2 lygio einamajam client
#     for person in uzsakym_dict[client].values():
#         # praeinam per raktus 2 lygio einamajam client ir asmens
#         for order in person.values():
#             # tikrinam, ar skaicius, jei taip dadedam i list
#             if isinstance(order, (int, float)):
#                 uzsakym_suma.append(order)

#     list = []
#     for i in uzsakym_suma:
#         if i >= 10:
#             list.append(i)
#             if len(list) >= 3:
#                 print(f"{client} can get free pica")


list_users_free_pica = []


# praeinam per raktus 1 lygio dict
def list_user_free_pica():
    for client in uzsakym_dict.keys():
        uzsakym_suma = []
        # praeinam per raktus 2 lygio einamajam client
        for person in uzsakym_dict[client].values():
            # praeinam per raktus 2 lygio einamajam client ir asmens
            for order in person.values():
                # tikrinam, ar skaicius, jei taip dadedam i list
                if order >= 10:
                    uzsakym_suma.append(order)

        if len(uzsakym_suma) >= 3:
            list_users_free_pica.append(client)

    return list_users_free_pica


# print(list_user_free_pica())
