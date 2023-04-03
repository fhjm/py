import random

a=random.randrange(1,10)
aa=random.randrange(1,10)
ans=int(input(f'{a}除{aa}是多少？：'))

if ans == a//aa:
    print("答對惹:D")
else:
    print("X 這麼簡單你不會")
print(f'{a}除{aa}答案是：{a/aa}\n')