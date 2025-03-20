import sys

IN = sys.stdin.readline 

if __name__ == "__main__":
    N = int(IN().strip())
    map_info = IN().strip()
    result = 0

    for i in range(len(map_info) - 1):
        if map_info[i] == 'E' and map_info[i+1] == 'W':
            result += 1
    
    print(result)