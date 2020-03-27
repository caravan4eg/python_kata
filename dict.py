locations = {} # пустой словарь
locations['Валентин'] = 'Москва'
locations['Андрей'] = 'Санкт-Петербург'
locations['Светлана'] = 'Казань'
print(locations)
print('Иван' in locations)
print('Валентин' in locations)
print(f'Светлана живет в городе {locations["Светлана"]}')

course_by = 'CARAVAN4EG - FFull-stack developer'
i = 0
while i < len(course_by):
    print('* ' + course_by[i].center(30) + ' *')
    i = i + 1
