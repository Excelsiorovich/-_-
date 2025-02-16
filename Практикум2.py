#1
summ = int(input())
print((summ - (96 * 48)))

#2
country_name=input()
part_country=country_name.split(' ')
for x in part_country:
    print(x)

#3
price=(input(''))
print(sum(map(int, price.split(' '))))

#4
person=int(input('Person:'))
wives=int(input('How many wives did a man have?'))
bags=int(input('How many bags did the wife have?'))
cat=int(input('How many cat did the bag have?'))
kittens=int(input('How many kitty did the cat have?'))
people= person+1+person*wives #+1Bangs who made a wish to go to St. Ives
animals= wives*bags*cat+wives*bags*cat*kittens
print(animals+people)

#5
planned_revenue=float(input('Write down the planned revenue the company:'))
profit= 0.19*planned_revenue
print('Прибыль за год:', round(profit, 2))

#6
# 1дюйм=0,0254м
# 1фунт=0,45359237кг
weight=float(input())
height=float(input())
print(round(((weight*0.453592)/((height*0.0254)**2)),2))

#7
# 1га=10000м^2
# 1см=0,01м
#1м^3=1000л(воды)
print(10000*0.01*1000)

#8
N=int(input(''))
M=int(input())
print(M//(N+1))

#9
import math
N=int(input(''))
K=int(input())
print(N-((math.floor(N/(K)))*K))

#10
# 1миля=1609.34м
distance=float(input())
print(int(distance//1609.34))