def abs_error(y_true, y_pred):
    return asb(y_true - y_pred) + 1e-10
