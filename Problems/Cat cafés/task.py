dict_ = {}

while True:
    s = input()
    if s != "MEOW":
        s = s.split()
        dict_[s[0]] = int(s[1])

    else:
        max_value = max(dict_.values())
        for i in dict_:
            if dict_[i] == max_value:
                print(i)
        break
