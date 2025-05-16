import time


def test_add_minus(eng):
    eng.addpath(r'./matlab')
    [a,b] = eng.add_minus(1, 2, nargout=2)
    print(a,b)


def _test(eng):
    # This is a test function to check if the MATLAB engine is working
    # put your test code here
    test_add_minus(eng)


def matlab_engine_test():
    import matlab.engine
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