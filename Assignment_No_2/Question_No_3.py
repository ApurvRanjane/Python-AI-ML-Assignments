a = 10
b = 10

print(id(a)) #same memory adress for immutable objects, if they hold same value
print(id(b)) #same memory adress for immutable objects, if they hold same value

a = [10]
b = [10]

print(id(a)) #diffrent memory adress for mutable objects, if they hold same value
print(id(b)) #diffrent memory adress for mutable objects, if they hold same value