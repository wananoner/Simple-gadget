# PM2.5.py
def main():
    PM = eval (input("What is today a PM2.5？:  "))
    if PM > 250:
        print("Zhongduwuran!")
    elif PM > 150:
        print("Yanzhongwuran!")
    elif PM > 115:
        print("Qingduwuran!")
    elif PM > 75:
        print("kongqihuanjingShizhong!")
    elif PM > 35:
        print("kongqizhilianglianghao!")
    else:
        print("Youxiu!")
main()
