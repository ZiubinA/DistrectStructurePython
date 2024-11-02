# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from prettytable import PrettyTable

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
pow = 4
a = 2
const = 32
array = [1,0,1,0,0]
arrayOfNumb = []
array4 = []
array3 = []
array2 = []
array1 = []
array0 = []
def calculating(array, a, pow, const, i):
    newArray = []
    x = a ** pow
    y = x * 2
    if y < const:
        while newArray.__len__() < const:
            j = array[i]
            if j == 1:
                x = a ** pow
                while x > 0:
                    x -= 1
                    newArray.append(j)
                x = a ** pow
                while x > 0:
                    x -= 1
                    newArray.append(0)

                x = a ** pow
                while x > 0:
                    x -= 1
                    newArray.append(0)

                x = a ** pow
                while x > 0:
                    x -= 1
                    newArray.append(j)

            if j == 0:
                x = a ** pow
                while x > 0:
                    x -= 1
                    newArray.append(j)

                x = a ** pow
                while x > 0:
                    x -= 1
                    newArray.append(1)

                x = a ** pow
                while x > 0:
                    x -= 1
                    newArray.append(1)

                x = a ** pow
                while x > 0:
                    x -= 1
                    newArray.append(j)

    else:
        j = array[i]
        if j == 1:
            while x > 0:
                x -= 1
                newArray.append(j)

            x = a ** pow
            while x > 0:
                x -= 1
                newArray.append(0)

        if j == 0:
            while x > 0:
                x -= 1
                newArray.append(j)

            x = a ** pow
            while x > 0:
                x -= 1
                newArray.append(1)

        i += 1

    return newArray

array4 = calculating(array, a, pow, const, 0)
array3 = (calculating(array, a, pow - 1, const, 1))
array2 = (calculating(array, a, pow - 2, const, 2))
array1 = (calculating(array, a, pow - 3, const, 3))
array0 = (calculating(array, a, pow - 4, const, 4))

def searching(array0, array1, array2, array3, array4):
    i = 0
    firstArray = []
    secondArray = []
    flag = 0
    while i < 31:
        firstArray.append(array0[i])
        firstArray.append(array1[i])
        firstArray.append(array2[i])
        firstArray.append(array3[i])
        firstArray.append(array4[i])
        secondArray.append(array0[i + 1])
        secondArray.append(array1[i + 1])
        secondArray.append(array2[i + 1])
        secondArray.append(array3[i + 1])
        secondArray.append(array4[i + 1])

        y = 0
        while y < 5:
            if (firstArray[y] != secondArray[y]):
                flag += 1
            y += 1
        if(flag > 1):
            return 2
        else:
            flag = 0
        i += 1
        firstArray = []
        secondArray = []

    return flag




t = PrettyTable(['index', 'array'])
t.add_row([4, calculating(array, a, pow, const, 0)])
t.add_row([3, calculating(array, a, pow - 1, const, 1)])
t.add_row([2, calculating(array, a, pow - 2, const, 2)])
t.add_row([1, calculating(array, a, pow - 3, const, 3)])
t.add_row([0, calculating(array, a, pow - 4, const, 4)])


print(t)
firstArray = []
secondArray = []
if(searching(array0, array1, array2, array3, array4) == 2):
    print("the array is incorrect")
else:
    print("the array is correct!!")



