## 오류 ##
# 오류_클래스 : IndexError, ValueError, ZeroDivisionError, ...

# try:
#   오류 예상 코드
# except [오류_클래스 [as 변수]]:
#   오류 발생시 처리 코드
# [finally:
#   무조건 실행 코드]

# 기본 #
nums = [1,10,20,50]

try:
    nums_index = int(input('NUMS 인덱스: '))   # 오류 발생 예상 지역1
    div_int = int(input('인덱스를 나눌 정수: '))    # 오류 발생 예상 지역2

    print(nums[nums_index]/div_int)

except IndexError:
    print('인덱스 오류')
except ZeroDivisionError:
    print('0 오류')
except ValueError:
    print('숫자만 입력 가능')
finally:
    print('수고하셨습니다')

# 기본 + as 변수 #
nums = [1,10,20,50]
try:
    nums_index = int(input('NUMS 인덱스: '))   # 오류 발생 예상 지역1
    div_int = int(input('인덱스를 나눌 정수: '))    # 오류 발생 예상 지역2

    print(nums[nums_index]/div_int)

except IndexError as i:     # 변수
    print(i)
except ZeroDivisionError as z:     # 변수
    print(z)
except ValueError as v:     # 변수
    print(v)






