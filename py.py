x, a, h = symbols('x, a, h')
def  f_x_2 (x ):
    return  x**2

d_x = np.arange(-100.0 ,100.0 ,1 )
y = f_x_2(d_x)
# x^2 그래프 그림 
fx = x ** 2  
d = Derivative(fx, x)
#도함수 구함 
def  f_dx (a , b ):
    y_1= (d.doit().subs({x:b})) * a
    return  y_1
# x가 b일때 미정계수 배열
# 
#도함수 x 변화 배열
# y_2 = f_dx(a_1)
#도함수 y 변화 배열
first_x = 70  # 처음 x 70 선언 
for  i in  range (1 , 11 ):
    P_P = (first_x ** 2 ) ** (1 /4 ) # 학습량 
    
    if  f_dx(1 ,first_x) < 0 :
        first_x = first_x - P_P
    elif  f_dx(1 ,first_x) > 0 :
        first_x = first_x - P_P
    plt.scatter(first_x, first_x ** 2 )
    
# a_1 = np.arange(-10.0, 50.0, 1)
plt.scatter(first_x, first_x ** 2 )
plt.xlabel("x")
plt.ylabel("y")
plt.plot(d_x, y)
# plt.plot(a_1, a_dx, "r")
plt.show()
