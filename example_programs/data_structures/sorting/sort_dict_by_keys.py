
# sort values of a dictionary by its keys

structures = {
    '2jel':'antibody',
    '1cse':'subtilisin',
    '1ehz':'tRNA(Phe)',
    }

def sort_dict_by_keys(data):
    keys = data.keys()
    keys.sort()
    return [data[k] for k in keys]


print sort_dict_by_keys(structures)
