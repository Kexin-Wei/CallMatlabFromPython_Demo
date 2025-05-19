import time
import matlab.engine
import numpy as np


model_name = "test"


# Type 1: run the whole
def sim_to_end(eng, model_name):
    out = eng.sim(model_name)
    print(out)


def _test(eng):
    # This is a test function to check if the MATLAB engine is working
    # put your test code here
    eng.addpath(r"./matlab")
    sim_to_end(eng, model_name)


def matlab_engine_test():
    eng = matlab.engine.start_matlab()
    tic = time.time()
    _test(eng)
    tic = time.time() - tic
    print(f"Internal elapased time: {tic:.2f} seconds")
    eng.quit()
    return eng


if __name__ == "__main__":
    tic = time.time()
    matlab_engine_test()
    tic = time.time() - tic
    print(f"External elapased time: {tic:.2f} seconds")
