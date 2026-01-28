# Linear Regression with Delta Rule and Noise

## What We Learned

- Linear regression is used to predict continuous values.
- The linear model used is:
  y_pred = w * x + b
- Gaussian noise was added to simulate real-world data.
- Noise was generated using NumPy random normal function.
- Actual output was calculated as:
  y_actual = w * x + b + noise
- Error was calculated using:
  error = y_actual - y_pred
- Model was trained using the Delta Rule.
- Weight update rule used:
  w = w + alpha * error * x
- Bias update rule used:
  b = b + alpha * error
- We iterated the weight update multiple times to reduce error.
- After training, the best-fit regression line was plotted.
- Learned correct formula formatting for GitHub README using code blocks.

## Key Takeaway

Delta Rule updates weights iteratively using error and learning rate to obtain the best regression line even in noisy data.
