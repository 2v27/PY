# 取得倒數位置可以用負數>score[-1]>取倒數第一位
#score[0:2]>從0取到2位之前，不包含第2位
scores=[90,70,60,50,40]
friend=["ss","dd","ff","gg"]
print(scores[0:2])

##score[0:]>從0取到最後 score[:4]>到第四位之前
scores=[90,70,60,50,40]
friend=["ss","dd","ff","gg"]
print(friend[:4])

pharse ="Hello Jay"
        #012345678
print(pharse[6:])

#extend()>延伸
scores.extend(friend)
print(scores)

#append()>在list最後新增值
scores.append(30)
print(scores)

# .insert(a,b)>a位置插入b
scores.insert(2,2)
print(scores)

#remove(a) >刪除list裡的a值
scores.remove(scores[0])
print(scores)

#clear() >整個清
scores.clear()
print(scores)

#pop() >移除最後一位
scores=[90,70,60,50,40]
friend=["ss","dd","ff","gg"]
print("before "+str(scores))
scores.pop()
print("after "+str(scores))

#sort() >排列
scores=[90,70,60,50,40]
friend=["ss","dd","ff","gg"]
print("before "+str(scores))
scores.sort()
print("after "+str(scores))

#reverse() >翻轉
scores=[90,70,60,50,40]
friend=["ss","dd","ff","gg"]
print("before "+str(scores))
scores.reverse()
print("after "+str(scores))

#.index(a) >回傳第一個a的位置
scores=[90,60,60,50,40]
friend=["ss","dd","ff","gg"]
print(scores.index(60))

#.count(a) >回傳a的數量
scores=[90,60,60,50,40]
friend=["ss","dd","ff","gg"]
print(scores.count(60))

scores=[90,60,60,50,40]
friend=["ss","dd","ff","gg"]
print(len(scores))