from calendar import c
from unittest import result


def calculate (min, max, step):
    sum = 0
    while min<=max :
        sum+=min
        min+=step
    print(sum)
    return sum


calculate(1, 3, 1)
calculate(4, 8, 2)
calculate(-1, 2, 2)

data = {
    "employees": [
        {"name":"John",
        "salary":30000,
        "manager":False },
        {"name":"Bob",
        "salary":60000,
        "manager":True },
        {"name":"Jenny",
        "salary":50000,
        "manager":False },
        {"name":"Tony",
        "salary":40000,
        "manager":False }
    ]
}

def avg(data):
    n = len(data["employees"])
    sum = 0
    count = 0
    for employee in data["employees"]:
        if not employee["manager"]:
            sum = sum + employee["salary"]
            count += 1
    print(int(sum/count))       
    return int(sum/count)

avg(data)


def func(a):
    def multiply(b,c):
        print(a+b*c)
        return a+b*c
    return multiply

func(2)(3, 4)
func(5)(1, -5)
func(-3)(2, 9)


def maxProduct(nums):
    n = len(nums)
    
    if (n<2):
        print("No pairs exists")
        return
    a = nums[0]
    b = nums[1]
    for i in range(0,n):
        for j in range(i+1,n):
            if (nums[i] * nums[j] > a * b):
                a = nums[i]
                b = nums[j]
    print(a*b)

maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([10, -20, 0, -3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([5,-1, -2, 0])
maxProduct([-5, -2])


def twoSum(nums, target):
    a=nums[0]
    b=nums[1]
    a=0
    b=1
    n=len(nums)
    for i in range(0,n):
        for j in range(i+1, n):
            if nums[i]+nums[j] == target:
                a=i
                b=j
    result = f"[{a},{b}]"
    return result


result = twoSum([2,11,7,15],9)
print(result)

def maxZeros(nums):
    count =0
    result =0
    n = len(nums)
    for i in range(0,n):
        if nums[i] == 1:
            count = 0
            continue
        if nums[i] == 0:
            count += 1
            result = max(count,result)
    print(result)
    return result


maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1]) 
maxZeros([0, 0, 0, 1, 1]) 