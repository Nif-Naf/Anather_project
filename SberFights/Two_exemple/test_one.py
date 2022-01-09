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
    result = set(line_time[0]).issuperset(line_time[1])
    return result

time = [ "12-14", "09-13"]
print(get_result(time))