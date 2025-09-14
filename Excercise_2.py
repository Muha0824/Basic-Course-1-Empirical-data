######################## Excercise 2.2 ###################

# (2,1)
print(3.119 + 1.211)

# (2,2)
print(7354+1246)

#  (2,3)
print(78 + (14/3))

# (2,4)
print((78+14)/3)

# (2,5)
print(1+2*(3+2))

# (2,6)
print((2+4)/2)

# (2, 7)
print((4+2+3+2+4)/5)

# (2,8)
print(2/1/3)

# (2,9)
print(2/3/(3/5))

# (2, 10)
print(1/2 + 5/6)

# (2,11)
print(2**2) 

# (2,12)
print((4**2)**0.5)

# (2,13)
print((2**2) + (4**2))

#(2,14)
print((4**3) + (3**2), "(2.14)")

#(2,15)
print(16**0.5)

#(2,16)
print((2*10**3 + 4 * 10**2)/(2*10**2))

#(2,17)
print((2*10**3 + 4*10**2)/(2*10**2))


####################   Excercise 2.3    ########################

# 1 
a = 1 
b= 2 
print(a+b)

# 2 

# (a)
# I think beecause its basically becomes 101
x = 100 
x = x + 1 
print(x)

# (b) , you can't solve it because even if its 0, 0 doesn't equal 1, no matter what you do. 



# 3 
#(a)
pi = 3.14159 
fraction = 2/3 

#(b)
print(fraction*pi , "Circle")

# (c) 
# Its because we have aprox. our pi, and our 2/3 has floating error as it repeats. 
# so, small values adds to its error 

# (d)
# depends on the excatness of our measurements, yes cm would be a whole number, but 
# anything related to height, weight, age is a continus data value, 
# so yeah you would defintly get a tiny error, but depends what kind of precision you are looking for. 

########################## Excercise 2.4 ######################################

print("Hello World!")

########################## Excercise 2.5 ########################################

width = 68 
length = 105 
area = width * length 
print(type(area))
print(f'The area is {area} square meters')
## Its a int because we haven't converted it to float yet, but it can be done simply by : 
float_value = float(area)
print(type(float_value))
print(f'The area is {float_value} square meters')

########################## Excercise 2.6 ########################################

# 1 
# 2 + 6 / 2 = 4 , so the mean of the data is 4. 

#2 
integers = [4,2,6]

#3 
print(sum(integers)/len(integers))

########################## Excercise 2.7  ########################################

# 1
sigma = list(range(101)) 
print(sigma)
sum(sigma)

# 2 
sumList = sum(sigma)
print(sumList)

birth_year = {
    "Ansar":2004 ,
    "Tazeen":2008,
    "Baria":2012

}

########################## Excercise 2.8  ########################################

# 1 
poinsettias = {
    "Red": 108,
    "Pink":34, 
    "White":40
    
    }

# 2

print("The red poninsettias has ",poinsettias["Red"])


########################## Excercise 2.10  ########################################

# 1 
# so, our n is a discret number or a whole number, where f is a floating value, 
# 1 is a whole number, 
#  And b is our boolean value , which in our case is false as 7 is not 3. 

#2 
# so when we use > it means greater than, so 1,6 is not greater than 2.3, so it will return false. 
print(1.6>2.3)
