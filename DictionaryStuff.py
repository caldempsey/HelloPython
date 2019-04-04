/**
Filtering things
**/

def aggregate_key_values(dict_list: list, keys: list):
    return {k: sum(d.get(k, 0) for d in dict_list) for k in keys}

def aggregate_key_values_at_filter(dict_list: list, keys: list, filter: list):
    return {k: sum(d.get(k, 0) for d in dict_list) for k in keys if filter in d.values()}
