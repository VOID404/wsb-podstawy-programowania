if __name__ == "__main__":
    l = list(range(1, 11))
    print(l)
    l.append(11)
    print(l)
    l = l[:2] + l[3:]
    print(l)
    for i, v in enumerate(l):
        print(i, v)