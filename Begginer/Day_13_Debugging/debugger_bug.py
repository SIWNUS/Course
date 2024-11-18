import random;
import maths;

# #bugged code
# def mutate(a_list):
#     b_list = []
#     new_items = 0
#     for items in a_list:
#         new_items = items * 2
#         new_items += random.randint(1, 3)
#         new_items = maths.add(new_items, items)
#     b_list.append(new_items)
#     print(b_list) #result: [None]

# mutate([1, 2, 3, 5, 8, 13])

#corrected code
def mutate(a_list):
    b_list = []
    new_items = 0
    for items in a_list:
        new_items = items * 2
        new_items += random.randint(1, 3)
        new_items == maths.add(new_items, items)
        b_list.append(new_items)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])