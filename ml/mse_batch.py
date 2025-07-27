def compute_Qk(X_batch: float, y_batch: float, w: list) -> float:
    residuals = predict(X_batch, w) - y_batch
    return np.mean(residuals ** 2)

# mean squared error
# Q = compute_Qk(X, y, w)
