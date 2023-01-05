def partition(S, l, h):
    i = (l - 1)
    x = S[h]

    for j in range(l, h):
        if S[j] <= x:

            i = i+1
            S[i], S[j] = S[j], S[i]

    S[i+1], S[h] = S[h], S[i+1]
    return (i+1)

def quickSortIterative(S, l, h):
    size = h - l + 1
    stack = [0] * (size)

    top = -1
    top = top + 1
    stack[top] = l
    top = top + 1
    stack[top] = h

    while top >= 0:
        h = stack[top]
        top = top - 1
        l = stack[top]
        top = top - 1

        p = partition(S, l, h)

        if p-1 > l:
            top = top + 1
            stack[top] = l
            top = top + 1
            stack[top] = p - 1

        if p+1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

S = [3,1,23,5,43,3,2,2,34,]
n = len(S)
quickSortIterative(S, 0, n-1)

for i in range(n):
    print(S[i], end=" "),