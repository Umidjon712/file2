""" 
100dan kichik sonlar ichidan raqamlari bir-biriga teskari bo’lgan tub sonlarni chiqaring. Masalan: 13<--->31

"""
for n in range(2, 100):
    i = 2
    while i * i <= n:
        if not i % i:
            break
        i += 1
    else:
        i = 2
        revnum = int(str(n)[::-1])
        while i * i <= revnum:
            if not revnum % i:
                break
            i += 1
        else:
            if n != revnum:
                print(f"{n} - {revnum}")