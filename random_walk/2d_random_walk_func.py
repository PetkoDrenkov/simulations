import random
import matplotlib.pyplot as plt

def random_walk(n,x_0:int,y_0:int):
    x_v = []
    y_v = []
    x = x_0
    y = y_0
    for i in range(n):
        step = random.choice(['n','s','o','w'])
        if step == 'n':
            y += 1
        elif step == 's':
            y -= 1
        elif step == 'o':
            x += 1
        elif step == 'w':
            x -= 1
        x_v.append(x)
        y_v.append(y)
    plt.plot(x_v, y_v, '-', linewidth=1.7)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.title('Random Walk')
    plt.show()
    print(f"x={x},y={y}")


#random_walk(1500,1,2)













