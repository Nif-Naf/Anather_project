def get_result(time):

    line_time = []
    hours = 0
    result = None
    line = []
    score = 0

    #Шаг 1. Извлечение и избавляемся от черточки
    for i in time:
        separation = i.split('-')
        line_time.append(separation)
        
    #Шаг 2.
    for i in line_time:
        start = int(i[0])
        end = int(i[1])
        line.append(start)
        line.sort()
        hours = start

        while True:
           hours += 1
           line.append(hours)

           if hours == end:
               break

    #Шаг 3
    line.sort()
    time = True
    for i in line:
        cou = line.count(i)
        score += cou 
        
    if score % len(line) > 2:
        time = False

    return time    

time = [ "12-14", "09-13"]
#time = ['00-02', '03-07', '10-15', '08-09', '16-22']
#time = ['02-00', '07-03', '15-10', '09-08', '22-16']
#time =["00-06", "07-09", "10-12", "15-19", "20-23"]
print(get_result(time))