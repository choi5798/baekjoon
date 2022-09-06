import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
answers = input().rstrip()
counter = Counter(answers)

def from_B_to_R(N):
    i = 0
    count = 1
    while True:
        try:
            i = i + answers[i:].index('R')
            while i < N:
                if answers[i+1] == 'R':
                    i += 1
                else:
                    i += 1
                    count += 1
                    break
        except ValueError:
            break

        except IndexError:
            count += 1
            break
    return count

def from_R_to_B(N):
    i = 0
    count = 1
    while True:
        try:
            i = i + answers[i:].index('B')
            while i < N:
                if answers[i+1] == 'B':
                    i += 1
                else:
                    i += 1
                    count += 1
                    break
        except ValueError:
            break
        except IndexError:
            count += 1
            break
    return count
    
answer = min(from_B_to_R(N), from_R_to_B(N))
print(answer)
