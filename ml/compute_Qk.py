def compute_Qk(X_batch, y_batch, w):
    residuals = predict(X_batch, w) - y_batch
    return np.mean(residuals ** 2)
