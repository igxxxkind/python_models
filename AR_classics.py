import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def simplest_ar_1(par, N):
    """
       A simplest AR process with one root and without a constant.
        Inputs:
        pars - an autoregressive parameter
        N - length of the process
        Returns:
        process - simulated AR process
    """
    noise = np.random.randn(N)
    simulated = noise.copy()
    for item in range(1, N):
        simulated[item] = par*simulated[item-1] + noise[item]
    return simulated


def simple_ar_1(pars, N):
    """
       Simple AR process with one root and a constant.
        Inputs:
        pars - constant and an autoregressive parameter
        N - length of the process
        Returns:
        process - simulated AR process
    """
    const = pars.pop(0)
    noise = np.random.randn(N)
    simulated = const + noise.copy()
    for item in range(1, N):
        simulated[item] = const + pars*simulated[item-1] + noise[item]
    return simulated

def simulate_ar(pars, N):
    """
        A more general AR process with N roots and a constant.
        Inputs:
        pars - constant and an autoregressive parameter
        N - length of the process
        Returns:
        process - simulated AR process
    """
    const = pars.pop(0)
    M = len(pars)
    noise = np.random.randn(N)
    simulated = const + noise.copy()
    for item in range(1,N):
        if item < M:
            simulated[item] = const + np.dot(pars[:item], simulated[:item]) + noise[item]
        else:
            simulated[item] = const + np.dot(pars, simulated[(item-M):item]) + noise[item]
    return simulated
    
    
# test