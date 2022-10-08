import pandas as pd
from for_bot import *

# da_fr = super_main_def("Гендир", dataset_example)



def to_array(df):
    for_del = df['text']
    mass = []
    for i in for_del:
        mass.append(i)
    return mass


def double(a, b):
    a_set = set(a)
    b_set = set(b)
    set_3 = a_set.intersection(b_set)
    l_ab = (len(a_set) + len(b_set)) // 2
    l_3 = len(set_3)
    return l_3 >= l_ab * 0.8


def doubles_find(df):
    arr = to_array(df)
    b = [arr[0]]
    for i in arr:
        is_break = False
        for j in b:
            if double(i, j):
                is_break = True
                break
        if not is_break:
            b.append(i)
    return [elem[:5] for elem in b]
