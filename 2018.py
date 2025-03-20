import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN().strip())
    result = 1 # N은 항상 포함
    half = (N + 1) / 2
    left_point, right_point = 1, 1
    sum_value = 0

    while left_point < half:
        if sum_value < N:
            sum_value += right_point
            right_point += 1
        elif sum_value >= N:
            if sum_value == N:
                result += 1
            
            sum_value -= left_point
            left_point += 1
    
    print(result)