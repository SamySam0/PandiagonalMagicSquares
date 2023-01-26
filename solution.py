#!/usr/bin/env python3
from constraint import Problem , AllDifferentConstraint, ExactSumConstraint

# Task 1: Write a function that computes the common sum of each row, column and broken diagonal in a pan-diagonal magic square of size n
def CommonSum(n):
    return int((n**2)*(n**2+1)/(2*n))

# Tests for Task 1
# print("Tests for Task 1")
# print(f"CommonSum(3): {CommonSum(3)}. Expected: 15")
# print(f"CommonSum(4): {CommonSum(4)}. Expected: 34")


# Task 2: Write a function msqList(n, pairList) which, when n is passed an integer n and pairList is passed a (possibly empty) list of pairs [v, i] with 0 ≤ v < n2 and 1 ≤ i ≤ n2, returns the list of magic squares of size n such that, for every pair [v, i] in the list, position v is filled with the integer i.
def msqList(n, pairList):
    magicProblem = Problem()
    squares = list(range(0, n**2)) # Number as variables
    values = list(range(1, n**2 + 1)) # Domain of each variable

    sumOfAddingUp = CommonSum(n)

    magicProblem.addVariables(squares , values)
    magicProblem.addConstraint(AllDifferentConstraint(), squares)

    # Pair constraints
    for pair in pairList:
        magicProblem.addConstraint(ExactSumConstraint(pair[1]), [pair[0]])

    # Diagonal constraints
    magicProblem.addConstraint(ExactSumConstraint(sumOfAddingUp), list(range(0,n**2,n+1)))
    magicProblem.addConstraint(ExactSumConstraint(sumOfAddingUp), list(range(n-1,n**2-n+1,n-1)))

    # Row constraints
    for row in range(n):
        # print([row*n+i for i in range(n)])
        magicProblem.addConstraint(ExactSumConstraint(sumOfAddingUp), [row*n+i for i in range(n)])

    # Column constraints
    for col in range(n):
        # print([col+n*i for i in range(n)])
        magicProblem.addConstraint(ExactSumConstraint(sumOfAddingUp), [col+n*i for i in range(n)])

    return magicProblem.getSolutions()

# Tests for Task 2
# print("Tests for Task 2")
# test1 = msqList(4,[[0,13],[1,12],[2,7]])
# print(test1, "- should return 4 solutions all of each including (0: 13, 1: 12, 2: 7)", f"\n Passed: {len(test1) == 4 and len([1 for i in test1 if (i[0] == 13 and i[1] == 12 and i[2] == 7)]) == 4}")
# test2 = msqList(3,[])
# print(test2, "- should return 8 solutions", f"\n Passed: {len(test2) == 8}")


# Task 3: Write a function pmsList(n, pairList) which, when n is passed an integer n and pairList is passed a (possibly empty) list of pairs [v, i] with 0 ≤ v < n2 and 1 ≤ i ≤ n2, returns the list of pan-diagonal magic squares of size n such that, for every pair [v, i] in the list, position v is filled with the integer i.
def diagonalBLtoTR(n, q):
    l = [q]
    for i in range(n-1):
        q = q - n + 1
        if q < 0:
            q = n**2 + q
        l.append(q)
    return l

def diagonalBRtoTL(n, q):
    l = [q]
    for i in range(n-1):
        q = q + n + 1
        if q > (n**2-1):
            q = q % (n**2)
        l.append(q)
    return l

def pmsList(n, pairList):
    magicProblem = Problem()
    squares = list(range(0, n**2)) # Number as variables
    values = list(range(1, n**2 + 1)) # Domain of each variable

    sumOfAddingUp = CommonSum(n)

    magicProblem.addVariables(squares , values)
    magicProblem.addConstraint(AllDifferentConstraint(), squares)

    # Pair constraints
    for pair in pairList:
        magicProblem.addConstraint(ExactSumConstraint(pair[1]), [pair[0]])

    # Diagonal constraints
    for row in range(n):
        # print(diagonalBLtoTR(n, row*n))
        # print(diagonalBRtoTL(n, row*n))
        magicProblem.addConstraint(ExactSumConstraint(sumOfAddingUp), diagonalBLtoTR(n, row*n))
        magicProblem.addConstraint(ExactSumConstraint(sumOfAddingUp), diagonalBRtoTL(n, row*n))
    
    # Row constraints
    for row in range(n):
        # print([row*n+i for i in range(n)])
        magicProblem.addConstraint(ExactSumConstraint(sumOfAddingUp), [row*n+i for i in range(n)])

    # Column constraints
    for col in range(n):
        # print([col+n*i for i in range(n)])
        magicProblem.addConstraint(ExactSumConstraint(sumOfAddingUp), [col+n*i for i in range(n)])

    return magicProblem.getSolutions()

# Tests for Task 3
# print("Tests for Task 4")
# test3 = pmsList(4,[[0,13],[1,12],[2,7]])
# print(test3, "- should return solutions, one of which is (0: 13, 1: 12, 2: 7, 3: 2, 4: 8, 5: 1, 6: 14, 7: 11, 8: 10, 9: 15, 10: 4, 11: 5, 12: 3, 13: 6, 14: 9, 15: 16)", f"\n Passed: {len(test3) > 1 and test3[0] == {0: 13, 1: 12, 2: 7, 3: 2, 4: 8, 5: 1, 6: 14, 7: 11, 8: 10, 9: 15, 10: 4, 11: 5, 12: 3, 13: 6, 14: 9, 15: 16}}")
# test4 = pmsList(3,[])
# print(test4, "- should return empty", f"\n Passed: {len(test4) == 0}")


# Debug
if __name__ == '__main__':
    print("debug run...")
