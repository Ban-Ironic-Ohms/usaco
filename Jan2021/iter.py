from itertools import compress, product
items = [1, 2, 3, 4]
def combinations(items):
    return ( set(compress(items,mask)) for mask in product(*[[0,1]]*len(items)) )

print(combinations(items))