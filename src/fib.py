def fibonacci(n):
    a1, a2 = 1, 1
    i = 2
    while(i<n):
        tmp = a2
        a2 = a1 + a2
        a1 = tmp
        i += 1

    return a2




if __name__ == "__main__":
    r = fibonacci(n=6)
    print(r)