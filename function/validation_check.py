import re

# 회원 가입시 패스워드 검증.
def register_password_check(password):

    # 영문, 숫자 특수문자 중에 3종류 이상을 조합하여 최소 8자리 이상의 길이로 구성.
    pattern1 = "^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$"
    pattern1 = re.compile(pattern1)
    eng_num_char = bool(re.search(pattern1, password))

    # 영문 숫자 패턴
    pattern2 ="^(?=.*[a-zA-Z])(?=.*\d)[A-Za-z\d]{10,}$"
    pattern2 = re.compile(pattern2)
    eng_num = bool(re.search(pattern2, password))

    # 영문 특수문자 패턴
    pattern3 = "^(?=.*[a-zA-Z])(?=.*[@$!%*#?&])[A-Za-z@$!#%*?&]{10,}$"
    pattern3 = re.compile(pattern3)
    eng_char = bool(re.search(pattern3, password))

    # 숫자 특수문자 패턴
    pattern4 ="^(?=.*\d)(?=.*[@$!%*#?&])[\d@$!#%*?&]{10,}$"
    pattern4 = re.compile(pattern4)
    num_char = bool(re.search(pattern4, password))

    check_list = [eng_num_char,eng_num,eng_char,num_char]

    if True in check_list:
        return True
    else:
        return False


# 이메일 검증.
def register_email_check(id):

    pattern = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    result = bool(pattern.match(id))

    if result:
        return True
    else:
        return False

# 사용자 이름 검증
def register_name_check(name):

    pattern = re.compile('^[ㄱ-ㅎ|가-힣|a-z|A-Z|]+$')
    result = bool(pattern.match(name))

    if result:
        return True
    else:
        return False


