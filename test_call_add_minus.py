import time

def get_matlab_engine():
    import matlab.engine
    eng = matlab.engine.start_matlab()
    return eng

def test_add_minus(eng):
    eng.addpath(r'./matlab')
    [a,b] = eng.add_minus(1, 2, nargout=2)
    print(a,b)


if __name__ == "__main__":
    tic = time.time()
    test_add_minus(get_matlab_engine())
    tic = time.time() - tic
    print(f"Elapsed time: {tic:.2f} seconds")
    # eng.quit()cd 