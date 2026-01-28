import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(0, 1, 100)


true_w = 2.5
true_b = 1.0


noise = np.random.normal(0, 100, size=x.shape)


y = true_w * x + true_b + noise


w = 0.0
b = 0.0
alpha = 0.01   
epochs = 50


for _ in range(epochs):
    for i in range(len(x)):
        yp = w * x[i] + b         
        e = y[i] - yp              
        w = w + alpha * e * x[i]   
        b = b + alpha * e          


y_pred = w * x + b


plt.scatter(x, y, label="Noisy Data", color="blue", s=15)
plt.plot(x, y_pred, label="Best Fit Line", color="red", linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Linear Regression using Delta Rule (50 Iterations)")
plt.show()


print("Learned weight (w):", w)
print("Learned bias (b):", b)
