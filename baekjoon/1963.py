from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

input = sys.stdin.readline

# 입력 : 1000이상의 소수

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+ 1):
        if num % i == 0:
            return False
    return True

def find_prime(prime_from, prime_to):
    q = deque()
    cnt = 0
    visited = set()
    q.append((prime_from, cnt))
    
    while q:
        prime_cur, cur_cnt = q.popleft()
        if prime_cur == prime_to:
            # print(f"prime_cur: {prime_cur}, prime_to: {prime_to}")
            return cur_cnt
        
        # TODO : 현재 prime에서 destination prime으로 가기 위해
        # 각 자릿수를 변경해보며, 이 숫자가 소수인지 확인한다
        # 소수면 큐에 넣고, count + 1
        
        for i in range(4):
            for j in range(10):
                if (i == 0 and j == 0) or (prime_cur[i] == str(j)):
                    continue
                prime_cur_list = list(prime_cur)
                prime_cur_list[i] = str(j)
                prime_next = ''.join(prime_cur_list)
                
                if is_prime(int(prime_next)) and prime_next not in visited:
                    visited.add(prime_next)
                    # print(visited)
                    # print(f"visited : {visited}")
                    q.append((prime_next, cur_cnt+1))
    
    return "Impossible"
        

def main():
    T = int(input())
    for _ in range(T):
        prime_from, prime_to = map(str, input().rstrip().split())
        print(find_prime(prime_from, prime_to))


main()