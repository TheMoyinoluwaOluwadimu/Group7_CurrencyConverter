number = input("number : ")
number = [char for char in number]
#num = int(number[0])
for i in range(len(number)):
    number[i] = int(number[i])
    if number[i] >= 2:
        print("only takes 0s and 1s")
    if number[i] == 0 or 1:
        
