import matlab.engine

eng = matlab.engine.start_matlab()

eng.addpath(r'./matlab')
[a,b] = eng.test_add(1, 2, nargout=2)
print(a,b)