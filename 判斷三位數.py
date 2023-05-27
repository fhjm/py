a=int(input("輸入數字"))
if a>=100:
    print("這是三位數")
elif a<=1000:
    print("這是四位數")
elif a<=99:
    print("這是二位數")
elif a<10:
    print("這是一位數")