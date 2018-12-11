#!/usr/bin/python

'''

Created on 2017年12月13日

@author: E.E.Luang
'''


print("简化版个税计算。\n起征点是3500。\n\n输入你的税前收入，计算出税后收入。")

str_salary=input('请输入你的税前月薪（RMB）：')

str_do51=input('算不算五险一金?(y/n, 默认y) ')


if not str_salary.isdigit():
    print("输入的不是数值。")
    exit()

salary = int(str_salary)

# 算不算五险一金
if not str_do51=='n':
    five=salary*0.11+10
    gjj = salary*0.1

    salary = salary-gjj-five
    print('五险：',five,'一金：',gjj,' 后，剩余：',salary)



if salary <= 5000:
    print("少于起征点，不用扣税。税收收入："+5000)
    exit()

# 去掉起征点 
net_salary = salary-5000

# 根据收入区间计算扣税比例，得出税后收入
if net_salary<=1500:
    theTax = net_salary*0.03
    print('个税第1档，3%，扣税：',theTax,'.税后:',(net_salary-theTax+3500))

elif net_salary>1500 and net_salary<=4500:
    theTax = net_salary*0.1-105
    print('个税第2档，10%，扣税：',theTax,'.税后:',(net_salary-theTax+3500))

elif net_salary>4500 and net_salary<=9000:
    theTax = net_salary*0.2-555
    print('个税第3档，20%，扣税：',theTax,'.税后:',(net_salary-theTax+3500))
    
elif net_salary>9000 and net_salary<=35000:
    theTax = net_salary*0.25-1005
    print('个税第4档，25%，扣税：',theTax,'.税后:',(net_salary-theTax+3500))
    
elif net_salary>35000 and net_salary<=55000:
    theTax = net_salary*0.3-2755
    print('个税第5档，30%，扣税：',theTax,'.税后:',(net_salary-theTax+3500)) 
    
elif net_salary>55000 and net_salary<=80000:
    theTax = net_salary*0.35-5505
    print('个税第6档，35%，扣税：',theTax,'.税后:',(net_salary-theTax+3500)) 
    
else :
    theTax = net_salary*0.45-13505
    print('个税第7档，45%，扣税：',theTax,'.税后:',(net_salary-theTax+3500)) 

