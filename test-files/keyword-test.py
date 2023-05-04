keyword = input('입력 메시지 : ')

## print(keyword)

# 주식 => KOSPI, KOSDAQ, KOSPI200
if keyword == '주식':
    print('KOSPI: 2409')
    print('KOSDAQ: 84')
    print('KOSPI200: 324')

# 로또, lotto, Lotto => 로또 번호 + 당첨 금액
elif keyword in ['로또', 'lotto', 'Lotto']:
    print('1, 2, 3, 4, 5, 6, 7, 1000000')

# 쇼핑 스팸 => 스팸 검색결과 중 가장 위에 있는거 응답
# 쇼핑 냉장고 => 냉장고 검색결과 ... 
elif keyword.split()[0] == '쇼핑' :
    print('최저가 검색: ')
    print(keyword.split()[1])

else:
    print('모르는 명령어 입니다.')

