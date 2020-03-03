import sys


def solution(N):
    A = str(N)
    A = A.replace('4', '2')
    A = int(A)
    B = N - A
    return A, B


T = int(sys.stdin.readline().strip())
for i in range(T):
    N = int(sys.stdin.readline().strip())
    A, B = solution(N)
    print(f'Case #{int(i+1)}, {A} {B}')

