#!/usr/bin/env python3

def return_evens(num_list):
    even_list = []
    for evens in num_list:
        if evens % 2 == 0:
            even_list.append(evens)

def make_exclamation(sentence_list):
    return [phrase+"!" for phrase in sentence_list]