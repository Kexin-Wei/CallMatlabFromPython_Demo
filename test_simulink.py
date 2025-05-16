import time

model_name = 'test'

# Type 1: run the whole
def sim_to_end(eng, model_name):
    out = eng.sim(model_name)
    print(out)

# Type 2
class TestSimulink:
    def __init__(self, eng, model_name):
        self.eng = eng
        self.model_name = model_name
        self.yHistory = 0
        self.tHistory = 0
    
    def start(self):
        self.eng
    
    def update_history(self):
        # Get the simulation history
        self.yHistory = self.eng.workspace['simout']
        self.tHistory = self.eng.workspace['tout']
        

    def open(self):
        self.eng.open_system(self.model_name, nargout=0)

    def close(self):
        self.eng.close_system(self.model_name, nargout=0)

    def sim(self):
        self.eng.sim(self.model_name)



def _test(eng):
    # This is a test function to check if the MATLAB engine is working
    # put your test code here
    eng.addpath(r'./matlab')
    sim_to_end(eng, model_name)
    


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
