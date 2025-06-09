print("Hello World222!")

a = 3
b = 2

# komentarz jednolinijkowy

'''
komentarz 
wielonijkowy
'''

if a < b:
    print("Warunek spełniony!")
    print("A < B")
elif a > b:
    print("Warunek przeciwny spełniony")
elif a == b:
    print("A = B")
else:
    print("Inny wynik")

"""
if warunek_1:
    costam
if warunek_2:
    cos_innego
"""

print("To się wykona zawsze!")

for liczba in range(10, 20, 2):
    print(liczba)

napis = "Ala ma kota"

for litera in napis:
    print(litera)

print(napis[::-1]) # slicing [od:do:krok]
print(napis[4:-2])

x = 10
while x > 5:
    x -= 1
    print(x)

x = 10
while True:
    x -= 1
    print(x)
    if x < 5:
        break

pesel = 1234567890

if pesel % 2 == 0:
    print("Pesel jest parzysty!")
else:
    print("Pesel jest nieparzysty!")


liczba_1 = 2
liczba_2 = 3
wynik = liczba_1 + liczba_2

for i in range(wynik):
    print("Obliczenia")


def compute_bmi(weight, height): # deklaracja funkcji
    bmi = weight / height ** 2
    return round(bmi, 2)

# print(compute_bmi(80, 1.8)) # wywołanie funkcji

result = compute_bmi(80, 1.8)
print(result)


def is_prime(number):
    for dzielnik in range(2, int(number ** (1/2) + 1)):
        if number % dzielnik == 0:
            return False
    return True


import math
print(math.sqrt(25))


def change_cases(sentence):
    result_sentence = ""
    for index in range(len(sentence)):
        if sentence[index].islower():
            result_sentence += sentence[index].upper()
        elif sentence[index].isupper():
            result_sentence += sentence[index].lower()
        else:
            result_sentence += sentence[index]
    return result_sentence


def generate_list(number):
    result = number
    my_list = []
    for i in range(10):
        my_list.append(result)
        result += number
    return my_list


def generate_list_2(number):
    return list(range(number, number * 10 + 1, number))


if __name__ == "__main__":
    """
    print("Hello!")
    my_weight = float(input("Podaj wagę w kg: "))
    my_height = float(input("Podaj wysokość w m: "))
    my_bmi = compute_bmi(my_weight, my_height)
    print("Moje BMI:", my_bmi)
    print(f"Moje BMI: {my_bmi}")
    print(is_prime(25))
    
    print(change_cases("Ala ma kota Filemona"))
    #print(len("Ala ma kota Filemona"))
    #print("Ala ma kota Filemona"[4])
    print("Ala ma kota Filemona".swapcase())
    """
    returned_list = generate_list_2(4)
    print(returned_list[::-1])
    print(returned_list[::2])
    print(returned_list[:-1])
    if 18 in returned_list:
        print(returned_list.index(18))


