import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradient descent.
    Return (w, b).
    """
    n, m = X.shape
    w = np.zeros(m)
    bias = 0.0
    for _ in range(steps):
        model = np.dot(X,w) + bias
        _predict = _sigmoid(model)
        er = _predict - y
        dw = (1/n) * np.dot(X.T, er)
        db = (1/n) * np.sum(er)
        w -= lr *dw
        bias -= lr * db
    return w,bias