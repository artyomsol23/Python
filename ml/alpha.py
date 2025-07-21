import math

def alpha(error_rate: float) -> float:
  if not 0 <= error_rate <= 1:
        raise ValueError('error_rate != [0, 1]')
  
  if error_rate <= 0:
      return float('inf')
  elif error_rate >= 1:
      return float('-inf')

  # 1e-10 для численной стабильности
  alpha = 0.5 * math.log((1 - error_rate + 1e-10) / (error_rate + 1e-10))
  
  return alpha
  
