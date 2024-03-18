import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    arr = [[] for _ in range(N)]

    for _ in range(M):
        i, j, k = map(int, IN().split())

        for n in range(i, j+1):
            arr[n-1].append(k)
    
    result = ''
    for a in arr:
        value = a[-1] if a else 0

        result += str(value) + " "
    
    print(result)