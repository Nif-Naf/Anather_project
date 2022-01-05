def get_result(cash, s):
    
    while True:
        cash.sort()
        #c = cash[1] + 3
        
        cash.insert(1, cash[0] + 3)
        cash.remove(cash[0])
        s -= 3

        if s < 3:
            cash.sort()
            cash.insert(1, cash[0] + s)
            cash.remove(cash[0])
            break

    cash.sort()
    #cash.pop()
    v = max(cash)
    b = cash.count(v)

    for i in range(b):
        cash.remove(v)

    return len(cash)


cash = [51, 48, 54, 48]
s = 14
a = get_result(cash, s)
print(a)




