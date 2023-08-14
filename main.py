statment=input("enter your : ").lower()
litter = input("enter character:").lower()
indices=[]
for index , char in enumerate (statment):
    if char == litter:
        indices.append(index)

print(indices)