from datetime import date


[2,5,7,8,9] #list
["Hello","World"]
(3,5,1,5,7,3,4) #Tuple
("Hello","World")
{2,4,5} #Set
{"Hello","World"}
{"apple":"蘋果","data":"資料"} #Dictionary
data=3
print([2,5,7,8,9])

x=3/6 #小數除法 0.5
x=3//6 #除法取整數
x=2**3 #2的3次方
x=2**0.5 #開根號
x=7%3 #取餘數

x="""三個雙引號支援換行""" #或是使用\n當換行

S="Hello"*3+"World" #HelloHelloHelloWorld

S="Hello"
print([0]) #印出第一個字元
print[s[1:4]] #包含開頭1 不包含結尾的4 故印出 ell
print[1:] #重開頭算起取得後面所有東西
print[:4] #不包含結尾取得前面所有字元

grades=[12,60,10,30,24]
print(len(grades))
print(grades[3:])
grades[0]=55
print(grades)
grades[1:4]=[]
print(grades)
grades += [12,33]
print(grades)
print(len(grades))
data=[[2,3,4,5],[3,5,2]]
print(data[0][1])
data[0][0:2]=[1,1,1]
print(data)