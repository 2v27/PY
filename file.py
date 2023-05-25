    # 讀取、寫入 
    # open("檔案路徑",mode="開啟模式") mode="r" 讀取 mode="w" 複寫 mode="a" 在原先資料後寫東西 
    #file=open("C:/Users/NCUE-06/Desktop/outer.txt",mode="r")

# file_in=open("inner.txt",mode="r")
# file_out=open("C:/Users/NCUE-06/Desktop/outer.txt",mode="r")
# print(file_in.read())
# print("**************************")
# print(file_out.read())
# file_in.close()
# file_out.close()

    #readline >一次讀一行

# file_in=open("inner.txt",mode="r")
# file_out=open("C:/Users/NCUE-06/Desktop/outer.txt",mode="r")
# print(file_in.readline())
# print(file_out.readline())
# file_in.close()
# file_out.close()

    #搭配for_loop
# file_in=open("inner.txt",mode="r")
# for num in file_in:
#     print(num)
# file_in.close()

    #readlines >把資料丟到列表裡
# file_in=open("inner.txt",mode="r")
# print(file_in.readlines())
# file_in.close()

    #write
# file_in=open("inner.txt",mode="w")
# file_in.write("10\n70\n60\n50\n40")
# file_in.close()

    #append
# file_in=open("inner.txt",mode="a",encoding="utf-8")
# file_in.write("\n 測試換行")
# file_in.close()

    #不用close的方式
with open("inner.txt",mode="a",encoding="utf-8") as file:
    file.write("\n測試with")