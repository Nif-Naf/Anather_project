

def gen_seq(score):
    """Generation of a super-growing sequence"""
    sequence = list([1])

    for i in range(score):
        res = sum(sequence) + 3
        sequence.append(res)

    return sequence

def test(sequence):
    total = 0 
    result = True 
    for n in sequence: 
        print("Sum: ", total, "Element: ", n) 
        if n <= total: 
            result = False 
            break 
        total += n 
    return print("Superincreasing sequence: ", result)

obj = gen_seq(10)
print(obj)
test(obj)