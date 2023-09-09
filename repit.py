def best_friend(txt, a, b):
    pos = txt.find(a)
    pos = txt.find(a, pos + 1)
    pos2 = txt.find(b)
    if pos < pos2:
        return True
    return False



print(best_friend("we found your dynamite", "d", "y"))




