# Linear Regression using Delta Rule with Noise

## Overview
This experiment demonstrates linear regression trained using the Delta Rule. Gaussian noise is added to the data to simulate real-world conditions, and the model learns the best-fit regression line through iterative weight updates.

## What We Learned

- Linear regression is a supervised learning algorithm used to predict continuous values.
- The linear model equation used in this experiment is:
  y_pred = w * x + b
- Input data was generated using the NumPy linspace function.
- Gaussian noise was added to the output to represent real-world uncertainty.
- Noise was generated using the NumPy random normal function.
- The actual output was calculated by adding noise to the linear model.
- Prediction error was calculated as the difference between actual and predicted output.
- The Delta Rule was used to update weight and bias values.
- Weight update depended on learning rate, error, and input value.
- Bias was updated using the same error term.
- The model parameters were updated iteratively for multiple epochs.
- After training, the learned regression line represented the best fit for noisy data.
- Proper formatting of formulas using code blocks was learned for GitHub README files.

## Conclusion
This experiment shows how the Delta Rule helps linear regression models learn optimal parameters even in the presence of noise, resulting in a best-fit regression line.
