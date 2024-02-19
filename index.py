even_number = [2,4,6,8,10,12,14]
print(even_number[2:5])

a=range(1,11)
print(type(a))
print(a)
print(list(a))
a=list(range(2,15,2))
print(list(range(2,15,2)))
print(*a)

mix_list = [1,[1,'one',2,'two',3,'three'],4]
print(mix_list[1][1::2])

my_list = [0,1,2,3,4,5]
print(
    my_list[2:20]
)
harf = "abcdefg"
my_list = list(harf)
print(my_list[::-1])

my_list = ['a',[1,2,3],[90,89,78],20,30]
my_list[2] = [99,89,78] 
print(my_list)

my_list[0:1] = ['a','b','c'] 
print(my_list)

a =range(5,20)
print(type(a))
print(list(a))
print(list(range(2,21,3)))

mytuple=(1,2,3,4,5,6)
print(mytuple)
print(tuple("itop"))
mytuple2 = 3,1,5,6
print(mytuple2)
print(type(mytuple2))

mytuple = tuple(range(1,10))
print(mytuple)

a= [1,2,3]
b= (1,2,3)
import sys
print(sys.getsizeof(a))