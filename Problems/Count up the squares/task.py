integ = int(input())

if integ == 0:
    print(integ)
else:
    sum_ = 0
    lst_intg = []
    while True:
        lst_intg.append(integ)
        sum_ += integ
        if sum_ == 0:
            print(sum([i ** 2 for i in lst_intg]))
            break
        integ = int(input())
