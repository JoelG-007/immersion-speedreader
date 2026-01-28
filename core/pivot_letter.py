def get_pivot_index(word):
    l = len(word)
    if l <= 2:
        return 0
    elif l <= 5:
        return l // 2
    else:
        return int(l * 0.35)
    
