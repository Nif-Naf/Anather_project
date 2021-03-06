def get_result(cash, s):
    
    while True:
        """Основной бесконечный цикл."""

        # Сам смысл заменить самый маленький элемент на его сумму с числом 3. 
        # Подставляем вперед него сумму а сам первый элемент просто удаляем.

        cash.sort()                     # Сортируем список.
        cash.insert(1, cash[0] + 3)     # Вставляем 2 элементом сумму 1-го элемента и 3.
        cash.remove(cash[0])            # Удаляем первый элемент списка. 
        s -= 3                          # Отнимаем у переменной s 3.


        if s < 3:
            """Условие прерывание цикла: когда s будет меньше 3."""
            cash.sort()                          # Сортируем список.
            cash.insert(1, cash[0] + s)          # Вставляем 2 элементом сумму 1-го элемента и того что осталось от s.
            cash.remove(cash[0])                 # Удаляем первый элемент списка.
            break                                # Выходим из цикла.

    cash.sort()                                  # Сортируем список.
    max_elem = max(cash)                         # Ищем самый большой элемент списка.
    how_max_elem = cash.count(max_elem)          # Определяем сколько таких больших элементов в спике.

    for i in range(how_max_elem):
        """В этом цикле удаляем самые большие элементы."""
        cash.remove(max_elem)                    # Удаляем максимальные элементы.

    return len(cash)                             # Возвращаем длину списка функции.


cash = [51, 48, 54, 48]
s = 14
a = get_result(cash, s)
print(a)




