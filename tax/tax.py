#!/usr/bin/python

'''

五险一金：
养老 8%
医疗 2% +10元大病统筹
失业1%

公积金"假设" 10%

个人所得税计算

档    税率    区间判定    速算扣除
1    3%    1500    0
2    10%    1500-4500    105
3    20%    4500-9000    555
4    25%    9000-35000    1005
5    30%    35000-55000    2755
6    35%    55000-80000    5505
7    45%    80000-         13505


Created on 2017年12月13日

@author: E.E.Luang
'''


print("简化版个税计算。\n起征点是3500。\n\n输入你的税前收入，计算出税后收入。")

str_salary=input('请输入你的税前月薪（RMB）：')

if not str_salary.isdigit():
    print("输入的不是数值。")
    exit()

salary = int(str_salary)

five=salary*0.11+10
gjj = salary*0.1

salary = salary-gjj-five
print('五险：',five,'一金：',gjj,' 后，剩余：',salary)


if salary <= 3500:
    print("少于起征点，不用扣税。税收收入："+3500)
    exit()

# 去掉起征点 
net_salary = salary-3500

if net_salary<=1500:
    theTax = net_salary*0.03
    print('第1档，3%，扣税：',theTax,'.税后:',(net_salary-theTax+3500))

elif net_salary>1500 and net_salary<=4500:
    theTax = net_salary*0.1-105
    print('第2档，10%，扣税：',theTax,'.税后:',(net_salary-theTax+3500))

elif net_salary>4500 and net_salary<=9000:
    theTax = net_salary*0.2-555
    print('第3档，20%，扣税：',theTax,'.税后:',(net_salary-theTax+3500))
    
elif net_salary>9000 and net_salary<=35000:
    theTax = net_salary*0.25-1005
    print('第4档，25%，扣税：',theTax,'.税后:',(net_salary-theTax+3500))
    
elif net_salary>35000 and net_salary<=55000:
    theTax = net_salary*0.3-2755
    print('第5档，30%，扣税：',theTax,'.税后:',(net_salary-theTax+3500)) 
    
elif net_salary>55000 and net_salary<=80000:
    theTax = net_salary*0.35-5505
    print('第6档，35%，扣税：',theTax,'.税后:',(net_salary-theTax+3500)) 
    
else :
    theTax = net_salary*0.45-13505
    print('第7档，45%，扣税：',theTax,'.税后:',(net_salary-theTax+3500)) 

