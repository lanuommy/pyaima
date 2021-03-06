import json
import _json
import sys
import os
import xlwt
import requests
from bs4 import BeautifulSoup
#selectid = requests.get("https://www.aimatech.com/outlets/query")

#创建excel
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
#根据爱玛电动车在前端写死的select里，找出规则，按顺序排列
cityList = [

"北京",
"安徽",
"福建",
"甘肃",
"广东",
"广西",
"贵州",
"海南",
"河北",
"河南",
 "黑龙江",
 "湖北",
 "湖南",
 "吉林",
 "江苏",
 "江西",
 "辽宁",
 "内蒙古",
 "宁夏",
 "青海",
 "山东",
 "山西",
 "陕西",
 "上海",
 "四川",
 "天津",
 "西藏",
 "新疆",
 "云南",
 "浙江",
 "重庆"
]
#定义book，创建sheet
sheet = book.add_sheet('list', cell_overwrite_ok=True)
count = 0
for i in range(2,33):
    info = requests.get("https://www.aimatech.com/outlets/list?ccode=0&pcode=%s"%(i))
    jsonall = json.loads(info.text[11:-1])

    print("已经写完第一条数据，进入第二条")
    # 写入表头，定义好列
    sheet.write(0, 0, label='城市名字')
    sheet.write(0, 1, label='门店地址')
    sheet.write(0, 2, label='门店名字')
    sheet.write(0, 3, label='联系电话')
    #    print(jsonall)
    for a in jsonall:
        # 添加sheet
        addr = a['addr']
        name = a['realname']
        phonenumber = a['mobile']


        count = count + 1
        
        sheet.write(count, 0, cityList[i-2])
        sheet.write(count, 1, addr)
        sheet.write(count, 2, name)
        sheet.write(count, 3, phonenumber)

book.save('D:\Python_files\爱玛电动车所有门店信息.xls')
