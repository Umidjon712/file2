""" 
1 + 11 + 111 + 1111 + .. n hadlar qatorining yig'indisini topish dasturini yozing.
Test:
n= 5
Kutilayotgan natija:
1 + 11 + 111 + 1111 + 11111
Sum: 12345

"""

n = int(input("n: "))
i = 1
sum = 1
while i <= n:
    if i == 1:
        print(f"{str(1) * i}", end = "") 
    else:
        print(f" + {str(1) * i}", end = "") 
        sum += int(str(1) * i)
    i += 1

print(f"\nsum = {sum}")