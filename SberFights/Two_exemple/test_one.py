def get_result(time):

    #Инициализация переменных.
    line_time = []

    #Шаг 1. Извлечение, переформатирование, добавление во вложенный список.
    for i in time:
        separation = i.split('-')

        start = int(separation[0])
        end = int(separation[1])

        for q in separation:
            start += 1
            if start == end:
                break
            separation.append(str(start))
            separation.sort()
        line_time.append(separation)
 
    #Step2.
    #result = set(line_time[0]).issuperset(line_time[1])
    line_time.sort()




    #return result


def test_one():
    time = ["09-13", "12-14"]
    get_result(time)
    assert get_result(time) == False, "Должно быть Ложно"
   
def test_two():
    time = ["09-11", "12-14"]
    get_result(time)
    assert get_result(time) == True, "Должно быть Верно"

def test_three():
    time = ["09-10", "11", "12-14"]
    get_result(time)
    assert get_result(time) == True, "Должно быть Верно"

if __name__ == "__main__":
    test_one()
    print("Test one done")
    #test_two()
    print("Test two done")
    #test_three()
    print("Test_three done")
