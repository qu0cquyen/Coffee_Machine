def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return closest_mod_5(x + 1)