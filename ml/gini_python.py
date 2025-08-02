def gini(labels: list) -> float:
    classes = {}
    for label in labels:
        if label not in classes:
            classes[label] = 0
        classes[label] += 1

    total = len(labels)
    if total == 0:
        return 0
    
    sum = 0.0
    for count in classes.values():
        p = count / total
        sum += p ** 2
    
    gini = 1 - sum
    return gini
  
