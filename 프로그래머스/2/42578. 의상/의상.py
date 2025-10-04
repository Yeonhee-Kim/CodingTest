from collections import Counter
def solution(clothes):
    hash_table = {}
    for value, key in clothes:
        if key in hash_table:
            hash_table[key].append(value)
        else:
            hash_table[key] = [value]
    
    cnt = 1
    for v in hash_table.values():
        cnt *= (len(v) + 1)
    
    return cnt - 1