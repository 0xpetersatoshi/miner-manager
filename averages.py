"""
Calculate Simple and Exponential moving averages.
"""
from typing import List

def calculate_sma(samples: List) -> float:
    """Calculate the Simple Moving Average (SMA)"""
    n = len(samples)

    return sum(samples) / n


def calculate_ema(samples: List) -> float:
    """Calculate the Exponential Moving Average (EMA)"""
    current_value = samples[-1]
    sma = calculate_sma(samples)
    multiplier = _calculate_multiplier(len(samples))
    return ((current_value - sma) * multiplier) + sma


def _calculate_multiplier(n: int) -> float:
    return (2/ (n + 1))