def tree_error_rate(y_true: list, y_pred: list) -> float:
    if len(y_true) != len(y_pred):
        raise ValueError("y_true != y_pred")
    
    if not y_true:
        return 0.0
    
    errors = sum(1 for true, pred in zip(y_true, y_pred) if true != pred)
    
    return errors / len(y_true)
