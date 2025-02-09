#1
'''print('Hello, Python!')


#2
print('Привет, Python!')
print('Hello, Python!')
print('Bonjour, Python!')
print('Hej, Python!')
print('Hola, Python!')

#3
print('Привет ', end=' ')
print('Python!')

#4
 L_bracket=chr(ord('('))
 R_bracket=chr(ord(')'))
 R_slash=chr(92)
 L_slash=chr(ord('/'))
 undline=chr(ord('_'))
 equal=chr(ord('='))
 dot=chr(ord('.'))
 quotes=chr(ord("'"))
 Db_quotes=chr(ord('"'))
 print(f'{L_bracket}{R_slash}{3*undline}{L_slash}{R_bracket}'
       f'\n{L_bracket}{equal}{quotes}{dot}{quotes}{equal}{R_bracket}'
       f'\n{L_bracket}{2*Db_quotes}{R_bracket}{undline}'
       f'{L_bracket}{2*Db_quotes}{R_bracket}')

#5
print('Привет, Python!\n Hello, Python!\n Bonjour Python!\n Hej, Python!\n Hola, Python!' )

#6
name = input('Как вас зовут?')
print(f'Здравствуйте, {name}')

#7
name = input('Как вас зовут?')
print(f'Здравствуйте, {name}')
hobby = input('Что вам нравится?')
print(f'Отлично!{hobby} - хорошее увлечение.')

#8
login = input('Login:')
password = input('Password: ')
new_password = input('New password: ')
print(f'User{login} has changed the password to {new_password}')

#9
print('Введите плей-лист папы:')
song1 = input()
song2 = input()
song3 = input()
song4 = input()
song5 = input()
print(f'Плей-лист мамы:\n{song5}\n{song4}\n{song3}\n{song2}\n{song1}')

#10
flight_number = input('номер рейса:')
aviacompany_name_rus = input('имя авиакомпании(на русском языке):')
aviacompany_name_eng = input('имя авиакомпании(на английском языке):')
city_of_arriving_rus = input('город прилёта(на русском языке):')
city_of_arriving_eng = input('город прилёта(на английском языке):')
print(f'Заканчивается посадка на рейс {flight_number} авиакомпании {aviacompany_name_rus} до {city_of_arriving_rus} ')
print(f'This is the final boarding call for {aviacompany_name_eng} flight {flight_number} to {city_of_arriving_eng}')

#11
name = input('Как вас зовут?')
print(f'Привет, {name}! ')

#12
silverwatches_amount = 96
silverwatches_price = 48
goldwatches_amount = silverwatches_amount // 16
summarised_cost = int(input('Общая стоимость часов:'))
silverwatches_cost = silverwatches_price * silverwatches_amount
goldwatches_cost = summarised_cost - silverwatches_cost
if goldwatches_amount > 0:
    goldwatches_price = goldwatches_cost / goldwatches_amount
else:
    goldwatches_price = 0
print(goldwatches_price)

#13
blind_zone_R = float(input())
reception_range_R = float(input())
if reception_range_R < blind_zone_R:
    reception_range_R, blind_zone_R = blind_zone_R, reception_range_R
reception_range_S = 3.14*reception_range_R**2
blind_zone_S = 3.14*blind_zone_R**2
coverage_S = reception_range_S-blind_zone_S
print(coverage_S)

#14
result = int(input())
print(result - 4)

#15
sm = float(input())
inch = 2.54*sm
foot = 12*inch
yard = 3*foot
mile = 1760*yard
print(f'{yard} ярдов\n{mile} мили\n{foot} футов\n{inch} дюймов')'''