import collections
persons = [
    {
        "name": "Anna",
        "age": "19",
        "gender": "Female"
    },
    {
        "name": "Artour",
        "age": "39",
        "gender": "Male"
    },
    {
        "name": "Boris",
        "age": "28",
        "gender": "Male"
    },
    {
        "name": "Vlada",
        "age": "25",
        "gender": "Female"
    },
    {
        "name": "Franchesco",
        "age": "33",
        "gender": "Male"
    },
    {
        "name": "Franchesca",
        "age": "25",
        "gender": "Female"
    },
    {
        "name": "Angela",
        "age": "40",
        "gender": "Female"
    },
    {
        "name": "Evgenia",
        "age": "55",
        "gender": "Female"
    },
    {
        "name": "Inokentij",
        "age": "55",
        "gender": "Male"
    },
    {
        "name": "Fedor",
        "age": "55",
        "gender": "Male"
    },
    {
        "name": "Maksim",
        "age": "20",
        "gender": "Male"
    },
    {
        "name": "Kate",
        "age": "23",
        "gender": "Female"
    },
    {
        "name": "Margarita",
        "age": "28",
        "gender": "Female"
    },
    {
        "name": "Konstantsin",
        "age": "30",
        "gender": "Male"
    },
    {
        "name": "Anastasia",
        "age": "13",
        "gender": "Female"
    },
    {
        "name": "Fedor",
        "age": "19",
        "gender": "Male"
    }
]
men = 0
women = 0
overall = 0
above18 = 0
for i in (persons):
    overall +=1
    if i['gender']=='Male':
        men+=1
    if i['gender']=='Female':
        women+=1
    if i['age']>='18':
        above18+=1
print (f'В списке всего {overall} человек. Из них {men} мужчин и {women} женщин. Совершеннолентних - {above18} человек.')
names = [i['name'] for i in persons]
print (f'Список всех имен: {names}')
ages = [i['age'] for i in persons]
print (f'Отсортированный список возрастов без повторений: {sorted (set(ages)) }')
men_above35_fromF = [i['name'] for i in persons if i['age']>'35' and i['gender'] == 'Male' and 'F' in i['name']]
print (f'Список мужчин старше 35-ти с именем на "F" : {men_above35_fromF}')
Counter = collections.Counter(names)
print (f'Три самых встречающихся имени: {Counter.most_common(3)}')
