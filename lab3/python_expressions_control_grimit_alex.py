x=-2
y=3*(abs(2*x)+4)
#Boolean
print(f"a: {1==1}")
print(f"one is equal to two {1==2}")

#Literals and Variables
print(f"a :{16}")
num=20
print(f"a :{num}")

#precedence
print(2-3*4)
print(1+3*(4+4)/3*2)

#Relational operators
#Equality
print(f"is 'alex' == 'alexander'? {'alex'=='alexander'}")
#Comparison
print(f"is 7 <= 8? {7<=8}")
#Logical
a=1
print(f"NOT test :{not a}")

#IF statement, ELSE statement
bank_balance = 100
if bank_balance > 200:
    money = 500
    bank_balance += money
else:
    print("balance is less than or equal to 200.")

#ELIF statement
if bank_balance == 10:
    print("Bank balance is 10 dollars.")
elif bank_balance < 10:
    print("Bank balance is less than 10 dollars.")
else:
    print("Bank balance is greater than 10 dollars.")

#Ternary Operator 
fuel = 18
print("Fill tank now" if fuel<=5 else "There's enough fuel")

#While loop
funds=100
while funds >= 10:
    print("There are enough funds available.")
    funds-=10
print("There are not enough funds remaining.")

#For loop
movies = ["harry potter", "lord of the rings", "star wars"]
for movie in movies:
    print(f"movie: {movie}")

#break
for i in range(3):
    print(f"i: {i}")
    if i == 2:
        break

#continue
for i in range(20):
    #skips 10 and 20 in the range
    if i == (10 or 20):
        continue
    print(f"i * 100 = {i * 100}")




         