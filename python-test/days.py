# day.py
day = "星期一星期二星期三星期四星期五星期六星期天"
n = input("请输入星期数（1-7）： ")
pos = (int(n)-1) * 3
days = day[pos:pos+3]
print("今天是："+days+".")
