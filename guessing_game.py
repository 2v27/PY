secret_num=10
gus_num=None
count=3
out_of_limit=False
gus_times=0

# while gus_num!=secret_num and count!=0:
#     gus_num=int(input("Enter ur ans "))
#     if gus_num>secret_num:
#         count-=1
#         print("Lower")
#     elif gus_num<secret_num:
#          count-=1
#          print("Higher")
# if count==0:
#     print("Fail")
# else:
#      print("cong")

######################
while gus_num!=secret_num and not(out_of_limit):
    if gus_times<count:
        gus_times+=1
        gus_num=int(input("Enter ur ans "))
        if gus_num>secret_num:
            print("Lower")
        elif gus_num<secret_num:
            print("Higher")
    else:
        out_of_limit=True      
          
if  out_of_limit==True:
    print("Fail")
else:
     print("cong")