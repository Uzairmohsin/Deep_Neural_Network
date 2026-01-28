# Linear Regression with Delta Rule and Noise
## 📌 What We Learned

Linear Regression predicts continuous output using a linear equation.

Model equation used:

y_pred = w * x + b


Gaussian noise was added to simulate real-world data:

y_actual = w * x + b + noise


Noise was generated using NumPy’s normal distribution:

noise = np.random.normal(0, sigma, size=x.shape)


Prediction error was calculated as:

error = y_actual - y_pred


We trained the model using the Delta Rule.

Weight and bias were updated iteratively:

w = w + alpha * error * x
b = b + alpha * error


We iterated the update rule multiple times to reduce error.

After training, the best-fit regression line was plotted over noisy data.

Learned how improper math symbols break formatting in GitHub README.

Used plain text and code blocks for correct GitHub rendering.

## 🧠 Key Takeaway

Delta Rule updates weights using error and learning rate to obtain the best regression line, even in the presence of noise.
