#This is a single line comment
#This is a second single line comment :)

#variables
print("Luke Skywalker")
print(1.6)
user_name = "Luke Skywalker"
print(user_name)
number=100
number+=16
print(number)
alex="alex"
Alex="Alex"
print(Alex)
print(alex)

#String Concatenation
print("my name is " + user_name)
print(f"my name is {user_name} not Darth Vader")
num=10000*1616161
print(str(num)[1:6])

#functions
def subtract_numbers(a,b):
    output=a-b
    return output
print(subtract_numbers(5,6))

#Variable Scope
name="Alex"
def say_hello():
    name="Kate"
    return f"hello {name}"

print(say_hello())



