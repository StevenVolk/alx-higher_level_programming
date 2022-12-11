#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        scores = 0
        weights = 0
        for score, weight in my_list:
            scores += score * weight
            weights += weight
        w_average = scores / weights
        return (w_average)
    else:
        return (0)
