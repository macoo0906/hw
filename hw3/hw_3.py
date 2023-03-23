<<<<<<< HEAD
import get_fixed_price as fixed

per = float(input("할인율은? "))
fixed.get_fixed_price(per)

A_price = float(input('A 상품의 할인된 가격은?'))
print('A 상품의 정가는',fixed.A_price(A_price),'원')


B_price = float(input("B 상품의 할인된 가격은?"))
print('B 상품의 정가는',fixed.B_price(B_price),'원')
