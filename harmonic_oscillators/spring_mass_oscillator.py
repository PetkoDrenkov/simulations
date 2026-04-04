import matplotlib.pyplot as plt

''' Modeling Hook's Law
u = (m * w**2 * x**2)/2 ; f = -grad(u) = - du/dx = - m * w**2 * x = - k * x = f
(in one dimensional space, the gradient is just ordinary derivative; u is potential)
w = sqrt(k/m) <=> k = m * w**2
f = m * a = -k * x = - m * w**2 * x <=> a = - x * w**2 
'''

def classical_sho(w,x,v=0.):
    dt = 0.01
    x_0 = x
    t_max = 10
    t = 0
    x_points = []
    t_points = []
    while t < t_max:
        a = - (x * w**2)
        v += (a * dt)
        x += (v * dt)
        t += dt
        t_points.append(t)
        x_points.append(x)
    plt.plot(t_points,x_points,label=f"w={w},x={x_0}")
    plt.title("Hook's Law")
    plt.xlabel("time")
    plt.ylabel("x")
    plt.legend()
    plt.show()

