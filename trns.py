def find_order(order, key):
    for i in range(len(key)):
        order[key[i]] = i

def main():
    key = input("Enter Key: ")
    text = input("Enter PlainText: ")

    c = len(key)
    r = len(text) // c
    if len(text) % c:
        r += 1

    order = {}
    find_order(order, key)

    mat = ["" for _ in range(r)]

    ind = 0
    tsize = len(text)
    for i in range(r):
        for j in range(c):
            if ind >= tsize:
                mat[i] += 'x'
            else:
                mat[i] += text[ind]
                ind += 1

    cipher = ""
    for it in order.items():
        j = it[1]
        for i in range(r):
            cipher += mat[i][j]

    print("Cipher Text:", cipher)

if __name__ == "__main__":
    main()
