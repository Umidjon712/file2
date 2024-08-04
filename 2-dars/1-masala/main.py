"""
1-masala

Foydalanuvchi 2 ta son kiritadi, shu son orqali shaxmat doskasidagi rangni aytish kerak: 

Input:   1 4     (yani 1 chi qator, 4 chi ustun)
Output: oq

Input:   1 3
Output: qora

"""


son1 = int(input("son1: "))
son2 = int(input("son2: "))

if son1 % 2 and not son2 % 2:
    print(f"oq")
else:
    print(f"qora")