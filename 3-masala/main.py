""" 
Bo’luvchilar soni aniq 9ga teng bo’lgan 1000 dan kichik barcha sonlarni toping: Masalan: 36 (1, 2, 3, 4, 6, 9, 12, 18, 36)

"""
print(f"\n1000 dan kichik barcha sonlarni kiriting: ")
n = int(input("n = "))

count = 0

i = 1
while i <= n:
    if n % i == 0:
        print(f"  {i}", end = "")
        count += 1
    i += 1
        
if count == 9:
    print(f"\n  Bo'luvchilari {count} taga teng")
elif count < 9:
    print(f"\n  Bo'luvchilari 9 tadan kam")
else:
    print(f"\n  Bo'luvchilari 9 tadan ko'p")