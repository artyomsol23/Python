def gini(labels: list) -> float:
    classes = {}
    
    for label in labels:
        if label not in classes:
            classes[label] = 0
        classes[label] += 1
    
    if len(labels) == 0:
        return 0.0
    
    sum = 0.0
    
    for count in classes.values():
        p = count / len(labels)
        sum += p ** 2
    
    return 1 - sum
