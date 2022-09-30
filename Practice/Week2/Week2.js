function calculate (min,max,step) {
    var sum =0;
    var a = min;
    var b = max;
    var arr = [];
    for(i = min; i<=max; i += step){
        sum += i;
        arr.push(i);
        b = i;
    }
    console.log(sum)
    return sum
}

calculate(1,3,1);
calculate(4, 8, 2);
calculate(-1, 2, 2);

var data ={
    "employees":[
    {"name":"John",
    "salary":30000,
    "manager":false },
    {"name":"Bob",
    "salary":60000,
    "manager":true },
    {"name":"Jenny",
    "salary":50000,
    "manager":false },
    {"name":"Tony",
    "salary":40000,
    "manager":false }]
    };
    
    var x = data.employees[0].manager;
    function avg (data) {
    var n = data.employees.length;
    var salary = 0;
    var count = 0;
        for(let i=0; i<n; i++) {
            if(data.employees[i].manager == false) {
                salary += data.employees[i].salary;
                count += 1;
            }
        }
    console.log(salary/count)
    }
    
avg(data);

function func(a) {
 var sum = 0;
    return (b,c) => {
        sum = a+(b*c);
        console.log(sum);
        return sum
    }

}

function  add(a,b) {
    
}

func(2)(3,4)
func(5)(1, -5)
func(-3)(2, 9)

function maxProduct (arr) {
    var n = arr.length;
    if(n<2) {
        console.log("No pairs exists"+"<br>");
        return;
    }
    // if(n==2) {
    //     document.write("the result is "+ arr[0]*arr[1])
    // }
    var result = arr[0]*arr[1];
    for(let i = 0; i<n ; i++) {
        for(let j = i+1 ; j < n; j++) {
            if(arr[i]*arr[j] > result)  {
                // var result2 = "";
                result = arr[i]*arr[j];
                // result2=Math.max(result,result2);
            }
        }
    }
    console.log(result)
}


maxProduct([5, 20, 2, 6]);
maxProduct([10, -20, 0, 3]);
maxProduct([10, -20, 0, -3]);
maxProduct([-1, 2]);
maxProduct([-1, 0, 2]);
maxProduct([5, -1, -2, 0]);
maxProduct([-5, -2]);

function twoSum(nums,target) {
    var n = nums.length;
    var a = nums[0];
    var b = nums[1];
    var x= 0;
    var y= 1;
    var final = nums[0]+nums[1];
    if(n<2) {
        document.write("Not enough elements for this function");
    }
    for(let i = 0; i < n; i++) {
        for(let j = i+1; j < n; j++) {
            if(nums[i] + nums[j] == target) {
                a = nums[i];
                b = nums[j];
                x = i;
                y = j;
                final = nums[i]+nums[j];
            }    
        }
    } return ("["+x+", "+y+"]")
}

let result=twoSum([2, 11, 7, 15], 9);
console.log(result);



function maxZeros(nums) {
    var count = 0;
    var result = 0;
    for(let i=0; i<nums.length; i++)
        if (nums[i] == 1) {
            count = 0;
        }
        else if (nums[i] == 0) {
            count += 1;
            result = Math.max(result,count);
        }
    console.log(result);
}

maxZeros([0, 1, 0, 0]);
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]);
maxZeros([1, 1, 1, 1, 1]);
maxZeros([0, 0, 0, 1, 1]);
