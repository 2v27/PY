# for letter in "Test":
#     print(letter)

# for num in [0,1,2,3,4]:
#     print(num)

#range(a,b) >a到b之前
# for num in range(1,10):
#     print(num)

# 試做pow

def power(base,power):
    result=1#任何數的0次方=1
    for index in range(power):
        result*=base
    return result

print(power(2,0))
