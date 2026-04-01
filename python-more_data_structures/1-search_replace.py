#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Return a new list: replace item if it matches 'search', else keep original
    return [replace if x == search else x for x in my_list]
