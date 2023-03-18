def get_radius(prompt):
    r = int(input(prompt)) 
    return r 

def get_circle_area(r):
    result = r * r * 3.14
    return result 

radius = get_radius("넓이를 입력받을 원의 반지름은? ")
s = get_circle_area(radius)
print('반지름 ',radius,'인 원의 넓이 = 3.14 x',radius, 'x',radius, '=',s )   