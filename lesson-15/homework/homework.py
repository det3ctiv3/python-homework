import matplotlib.pyplot as plt
import numpy as np
#task1
values = np.linspace(-10,10,1000)
def quadratic_func(x):
    return x**2 - 4*x + 4
y = quadratic_func(values)
plt.plot(values, y, label="quadratic func", c='r')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


#task2
values_trig = np.linspace(0, (2*np.pi), 100)
def sin_func(x):
    return np.sin(x)
def cos_func(x):
    return np.cos(x)
sin_y = sin_func(values_trig)
cos_y = cos_func(values_trig)
plt.plot(values_trig, sin_y, label="sin func", c='b')
plt.plot(values_trig, cos_y, label="cos func", c='g')
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


#task3
fig, axes = plt.subplots(2,2, figsize=(10,5))
x1 = np.linspace(-2,2,100)
x2 = np.linspace(0,2*np.pi,100)
x3 = np.linspace(0,2,100)
x4 = np.linspace(0,3,100)
axes[0,0].plot(x1, x1**3, label="Cubic", c='r')
axes[0,0].set_xlabel("x")
axes[0,0].set_ylabel("y")

axes[0,1].plot(x2, np.sin(x2), label="Sin", c='b')
axes[0,1].set_xlabel("x")
axes[0,1].set_ylabel("y")

axes[1,0].plot(x3, np.exp(x3), label="Exp", c='g')
axes[1,0].set_xlabel("x")
axes[1,0].set_ylabel("y")

axes[1,1].plot(x4, np.log(x4+1), label="Logs", c='b')
axes[1,1].set_xlabel("x")
axes[1,1].set_ylabel("y")
plt.show()


#task4
x_values = np.random.uniform(0,10,100)
y_values = np.random.uniform(0,10,100)
plt.scatter(x_values, y_values, c='r', s=y_values, label="data", marker='o' )
plt.title("Random function")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()


#task5
data = np.random.normal(0,1,1000)
plt.hist(data, bins = 30, alpha = 0.9, color='red')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Histogram")
plt.show()


#task6
fig = plt.figure()
ax = plt.axes(projection='3d')
x = np.linspace(-5,5,200)
y = np.linspace(-5,5,200)
xx, yy = np.meshgrid(x,y)
zz = np.cos(xx**2 + yy**2)
ax.set_title("3D Surface Plot of $cos(x^2 + y^2)$")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis (cos(x² + y²))")
ax.plot_surface(xx, yy, zz, cmap='viridis')


#task7
categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [200, 150, 250, 175, 225]
colors = ['red', 'blue', 'green', 'orange', 'purple']
plt.bar(categories, values, color=colors)
plt.title("Costs by Categories")
plt.xlabel("Categories")
plt.ylabel("Cost")
plt.show()



#task8
time_periods = ['T1', 'T2', 'T3', 'T4']
category_A = [100,150,200,150]
category_B = [90,100,220,190]
category_C = [200,150,130,80]
plt.bar(time_periods, category_A, label='Category A', color='red')
plt.bar(time_periods, category_B, bottom=category_A, label='Category B', color='blue')
plt.bar(time_periods, category_C,
        bottom=[a + b for a, b in zip(category_A, category_B)],
        label='Category C', color='green')

plt.title("Stacked Bar Chart of Category Contributions")
plt.xlabel("Time Periods")
plt.ylabel("Values")
plt.legend()

plt.show()
