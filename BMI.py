height = float(input("請輸入身高（單位：公分）："))
weight = float(input("請輸入體重（單位：公斤）："))

# 計算BMI
bmi = weight / ((height/100) ** 2)

# 根據BMI值顯示不同的結果
if bmi < 18.5:
    print("您的BMI值為", bmi, "屬於體重過輕。")
elif 18.5 <= bmi < 24:
    print("您的BMI值為", bmi, "屬於正常範圍。")
elif 24 <= bmi < 27:
    print("您的BMI值為", bmi, "稍微有些過重。")
elif 27 <= bmi < 30:
    print("您的BMI值為", bmi, "屬於輕度肥胖。")
elif 30 <= bmi < 35:
    print("您的BMI值為", bmi, "屬於中度肥胖。")
else:
    print("您的BMI值為", bmi, "屬於重度肥胖。")
