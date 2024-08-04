""" 
100dan kichik sonlar ichidan raqamlari tarkibida 3 raqami qatnashgan barcha sonlarni va shu sonlar sonini chiqaring.
Javob : 0:100 -> {3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53, 63, 73, 83, 93}

"""


for i in range(100):
    if i % 10 == 3:
        print(f" {i}", end = ",")
    elif i // 10 == 3 and i % 10 != 3:
        print(f" {i}", end = ",")
    elif i / 10 == 3:
        print(f" {i}", end = ",")