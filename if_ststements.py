# 如果
hungry = True
if hungry:
    print("eat")
# 如果 否則
rainy = True
if rainy:
    print("I wil drive")
else:
    print("I will walk")
# 如果 或是如果 或是如果 否則
score = 100
if score == 100:
    print("給你1000")
elif score >= 80:
    print("給你500")
elif score >= 60:
    print("給你100")
else:
    print("你給我1000")

# 如果 a&b 否則
score = 80
rainy = True
if score == 100 and rainy:
    print("Give u 1000")
else:
    print("Give me 2000")

# 如果 aorb 否則
score = 100
rainy = True
if score == 100 or rainy:
    print("Give u 1000")
else:
    print("Give me 2000")

# 如果 aor !b 否則
score = 100
rainy = True
if score != 100 or not (rainy):
    print("Give u 1000")
else:
    print("Give me 2000")

def max_num1(n1,n2,n3):
    return max(n1,n2,n3)
print(max_num1(50,70,10))

def max_num2(n1,n2,n3):
    max=n1
    if n1>n2 and n1>n3:
        max=n1
    elif n2>n1 and n2>n3:
        max=n2
    else:
        max=n3
    return max
print(max_num1(50,90,10))