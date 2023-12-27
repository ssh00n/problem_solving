import sys
input = sys.stdin.readline
# 4659 비밀번호 발음하기

# 1. 모음(a, e, i, o, u) 하나를 반드시 포함
# 2. 모음이 3개 혹은 자음이 3개 연속으로 오면 안 됨
# 3. 같은 글자가 연속적으로 두 번 오면 안되나, ee와 oo는 허용

def check_password(password: str) -> bool:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_included = False

    last_char = ''
    vowel_count = 0
    consonant_count = 0

    for char in password:
        # 모음 체크
        if char in vowels:
            vowel_included = True
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0

        # 연속된 문자 체크 (ee와 oo는 제외)
        if char == last_char and char not in {'e', 'o'}:
            return False

        # 모음이나 자음이 3개 연속으로 오는지 체크
        if vowel_count == 3 or consonant_count == 3:
            return False

        last_char = char

    return vowel_included

while True:
    password = input().rstrip()
    if password == 'end':
        break
    
    is_acceptable = check_password(password)
    
    if is_acceptable:
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
