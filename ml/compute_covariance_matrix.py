import numpy as np

def compute_covariance_matrix(samples: np.ndarray, means: np.ndarray) -> np.ndarray:
    num_samples = len(samples)
    VV_total = np.zeros((3, 3))
    N = samples[0].shape[1]
    
    for x, mean in zip(samples, means):
        a = (x.T - mean).T
        VV = np.array([
            [np.dot(a[0], a[0]) / N, np.dot(a[0], a[1]) / N, np.dot(a[0], a[2]) / N],
            [np.dot(a[1], a[0]) / N, np.dot(a[1], a[1]) / N, np.dot(a[1], a[2]) / N],
            [np.dot(a[2], a[0]) / N, np.dot(a[2], a[1]) / N, np.dot(a[2], a[2]) / N]
        ])
        VV_total += VV
    
    return VV_total / num_samples
