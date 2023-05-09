shopping_bag = {}

def buy(lst) :
    print('[구입]')
    item = input('상품명? ')
    if item == '' :
        return False
    amount = int(input('수량은? '))
    lst[item] = amount
    print(f'장바구니에 {item} {amount}개가 담겼습니다.')
    print()

def show(list):
    print(f'>>> 장바구니 보기 : {list}')

def find(l):
    print('[검색]')
    key=input('장바구니에서 확인하고자 하는 상품은? ')
    if key in l:
        print(f'{key}은 (는) {l[key]}개 담겨있습니다.')
    else :
        print(f'장바구니에 {key}은 (는) 없습니다.')


while True:
    if buy(shopping_bag) == False:
        break
show(shopping_bag)
find(shopping_bag)
