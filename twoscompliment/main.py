# Function to find two's complement
def findTwoscomplement(str):
    n = len(str)

    i = n - 1
    while (i >= 0):
        if (str[i] == '1'):
            break

        i -= 1

    if (i == -1):
        return '1' + str

    # Continue traversal after the
    # position of first '1'
    k = i - 1
    while (k >= 0):

        # Just flip the values
        if (str[k] == '1'):
            str = list(str)
            str[k] = '0'
            str = ''.join(str)
        else:
            str = list(str)
            str[k] = '1'
            str = ''.join(str)

        k -= 1

    # return the modified string
    return str


if __name__ == '__main__':
    str = "10010011"
    print(findTwoscomplement(str))
