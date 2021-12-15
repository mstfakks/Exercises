def faktoriyel(number):
    if number == 0:
        return 1
    else:
        return number*faktoriyel(number-1)

number = int(input("Faktöriyelini almak istediğiniz sayıyı giriniz: "))
print(faktoriyel(number))

