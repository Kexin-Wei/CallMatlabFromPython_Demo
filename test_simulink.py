import time
import matlab.engine


model_name = 'test'

# Type 1: run the whole
def sim_to_end(eng, model_name):
    out = eng.sim(model_name)
    print(out)

# Type 2
class TestSimulink:
    def __init__(self, ):
        self.eng = None
        self.model_name = model_name
        self.yHistory = 0
        self.tHistory = 0

    def __del__(self):
        if self.eng is not None:
            self._simulink_stop()
            self.eng.quit()
            print("Disconnected from Matlab")

    def _simulink_set_u(self, u):
        self.eng.set_param(f'{self.model_name}/u','value',str(u),nargout=0)

    def _simulink_start_and_pause(self):
        self.eng.set_param(self.model_name, 'SimulationCommand', 'start', nargout=0)
        self.eng.set_param(self.model_name, 'SimulationCommand', 'pause', nargout=0)

    def _simulink_step(self):
        self.eng.set_param(self.model_name, 'SimulationCommand', 'continue', nargout=0)
        self.eng.set_param(self.model_name, 'SimulationCommand', 'pause', nargout=0)
    
    def _simulink_stop(self):
        self.eng.set_param(self.model_name, 'SimulationCommand', 'stop', nargout=0)
    
    def start(self):
        self.eng = matlab.engine.start_matlab()
        print("Connected to Matlab")
        self.eng.addpath(r'./matlab')
        self.eng.eval(f"model = '{self.model_name}';", nargout=0)
        self.eng.eval(f"load_system(model)", nargout=0)

        # initialize 
        self._simulink_set_u(0)
        # get parameters

        # start the simulation and pause
        self._simulink_start_and_pause()
        print("Simulation started and paused")

        self._update_history()
    
    def _update_history(self):
        # Get the simulation history
        self.yHistory = self.eng.workspace['out'].simout
        self.tHistory = self.eng.workspace['out'].time

    def step(self, u):
        if (self.eng.get_param(self.modelName,'SimulationStatus') != ('stopped' or 'terminating')):
            self._simulink_set_u(u)
            self._simulink_step()
            self._update_history()
            print(f"t: {self.tHistory}, y: {self.yHistory}")

def _test(eng):
    # This is a test function to check if the MATLAB engine is working
    # put your test code here
    eng.addpath(r'./matlab')
    sim_to_end(eng, model_name)

def matlab_engine_test():
    eng = matlab.engine.start_matlab()
    tic = time.time()
    _test(eng)
    tic = time.time() - tic
    print(f"Internal elapased time: {tic:.2f} seconds")
    eng.quit()
    return eng

def type1_test():
    tic = time.time()
    matlab_engine_test()
    tic = time.time() - tic
    print(f"External elapased time: {tic:.2f} seconds")

def type2_test():
    tic = time.time()
    test_simulink = TestSimulink()
    test_simulink.start()
    print("Simulation started")
    for i in range(10):
        print(f"Step {i+1}")
        test_simulink.step(i)
        time.sleep(0.1)
    tic = time.time() - tic
    print(f"External elapased time: {tic:.2f} seconds")

if __name__ == "__main__":
    # type1_test()
    type2_test()
