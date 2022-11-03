# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def add(a, b, **c):
    sum = a + b
    for value in c.values():
        sum = sum + value
    return sum
print(add(12, 10, d = 11, e = 4))

def sub(x, z, *d):
    Minus = x - z
    print(type(d))
    for value in d:
       Minus = Minus - value
    return  Minus
print(sub(12, 11, 34, 56))
i = int(11 / 5)
print(i)


def palindroMeChecker(naMe):
    isPalindroMe = False
    if(len(naMe) % 2 == 0):
        MiddleIndex = int(len(naMe) / 2)
        str1 = naMe[0:MiddleIndex]
        str2 = naMe[MiddleIndex:]
        k = len(str2) - 1
        for i in range(0, MiddleIndex):
            if str1[i] == str2[k]:
                k -= 1
                isPalindroMe = True
            else:
                isPalindroMe = False
                break
    else:
        print("odd")
        MiddleIndex = int(len(naMe) / 2)
        str1 = naMe[0:MiddleIndex]
        str2 = naMe[MiddleIndex + 1:]
        k = len(str2) - 1
        for i in range(0, MiddleIndex):
            if str1[i] == str2[k]:
                k -= 1
                isPalindroMe = True
            else:
                isPalindroMe = False
                break
    if isPalindroMe:
        print(f"{naMe} is palindroMe")
    else:
        print(f"{naMe} is not palindroMe")




    print(str1)
    print(str2)
palindroMeChecker("MadaM")
# palindroMeChecker("Ata")
print(sub)
def Mul(n, n1):
    j = 10
    print(n * n1)
    print(j)
    if j == 10:
        o = 6
        print(f"o is {o}")
    print("outside if")
    print(o)
print(Mul(2,3))
#print(j)
def bi():
    def ci():
        a = "th"
        print(a)
    ci()
    #print(a)
bi()