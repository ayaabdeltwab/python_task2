num=int( input("enter your number: "))
sorted_dict = {}
multiplication_table = [[i*j for j in range(1, i+1)] for i in range(1, num+1)]

print(multiplication_table)