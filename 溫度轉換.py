print("01：攝氏、02：華氏")
ac = int(input("輸入："))

if ac == 1:
    celsius = int(input("輸入攝氏溫度："))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} 的華氏是 {fahrenheit}")
elif ac == 2:
    fahrenheit = int(input("輸入華氏溫度："))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} 的攝氏是 {celsius}")
