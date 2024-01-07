#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def info():
    print("""Name   :  Truong Minh Phuong
ID     :  HE181016
Class  :  AI1811""")

def ex1():
    n = int(input("Enter numbers of element in array: "))
    arr = []
    sum = 0
    for i in range(n):
        arr.append(int(input(f"Element {i + 1}: ")))
        sum += arr[i]

    avg = sum / n

    min_sub = abs(arr[0] - avg)
    for i in range(n):
        if abs(arr[i] - avg) < min_sub:
            min_sub = arr[i] - avg

    print(arr)
    for i in range(n):
        if (arr[i] - avg) == min_sub:
            print(f"The position of element which has value nearest to the average of the array: {i}")
            break

def ex2():
    def cast_float(n):
        try:
            n = float(n)
            return True
        except ValueError:
            return False
    while True:
        grade = input("Enter the grade in the decimal system: ")
        if not cast_float(grade):
            print("Invalid grade.")
        else:
            grade = float(grade)
            if (grade > 10) or (grade < 0):
                print("Invalid grade, grade must be between 0 and 10.")
            else:
                break

    if grade >= 8.5 and grade <= 10.0:
        print('Alphabet grade: A\n4th grade: 4')
    elif grade >= 7.0 and grade < 8.5:
        print('Alphabet grade: B\n4th grade: 3')
    elif grade >= 5.5 and grade < 7.0:
        print('Alphabet grade: C\n4th grade: 2')
    elif grade >= 4.0 and grade < 5.5:
        print('Alphabet grade: D\n4th grade: 1')
    else:
        print('Alphabet grade: F\n4th grade: 0')

def ex3():
    n = int(input("Enter numbers of element in array: "))
    arr = []
    for i in range(n):
        arr.append(int(input(f"Element {i + 1}: ")))

    distinct_arr = []
    for i in range(n):
        if arr[i] not in distinct_arr:
            distinct_arr.append(arr[i])

    print("input: ", end='')
    for i in range(n):
        print(arr[i], end=' ')
    print()
    print("output: ", end='')
    for i in range(len(distinct_arr)):
        print(distinct_arr[i], end=' ')
    print()

def main():
    def cast(ans):
        if ans == 'a':
            return True, ans
        else:
            try:
                ans = int(ans)
                if 0 < ans < 5:
                    return True, ans
                else:
                    print("Usage: [1-4, a].")
                    return False, None
            except ValueError:
                print("Usage: [1-4, a].")
                return False, None

    print("a: Student information")
    print("1: Problem 1")
    print("2: Problem 2")
    print("3: Problem 3")
    print("4: Exit")
    print()
    while True:
        choose = input("> ")
        success, choose = cast(choose)
        if success:
            if choose == 'a':
                info()
            elif 1 <= choose <= 4:
                if choose == 4:
                    print("Exiting.")
                    break
                else:
                    if choose == 1:
                        ex1()
                    elif choose == 2:
                        ex2()
                    elif choose == 3:
                        ex3()


if __name__ == "__main__":
    main()


# In[ ]:




