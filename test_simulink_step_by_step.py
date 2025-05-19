import time
import matlab.engine
import numpy as np


model_name = "test"


class TestSimulink:

    def __init__(self):
        self.eng = None
        self.model_name = model_name
        self.u = 0
        self.yHistory = 0
        self.tHistory = 0

    def __del__(self):
        if self.eng is not None:
            self._simulink_stop()
            self.eng.quit()
            print("Disconnected from Matlab")

    def _simulink_set_u(self, u):
        self.u = u
        self.eng.set_param(f"{self.model_name}/u", "value", str(u), nargout=0)

    def _simulink_start_and_pause(self):
        self.eng.set_param(
            self.model_name,
            "SimulationCommand",
            "start",
            "SimulationCommand",
            "pause",
            nargout=0,
        )

    def _simulink_step(self):
        self.eng.set_param(
            self.model_name,
            "SimulationCommand",
            "continue",
            "SimulationCommand",
            "pause",
            nargout=0,
        )

    def _simulink_stop(self):
        self.eng.set_param(self.model_name, "SimulationCommand", "stop", nargout=0)

    def start(self):
        self.eng = matlab.engine.start_matlab()
        print("Connected to Matlab")
        self.eng.addpath(r"./matlab")
        self.eng.eval(f"model = '{self.model_name}';", nargout=0)
        self.eng.eval(f"load_system(model)", nargout=0)

        # initialize
        self._simulink_set_u(0)
        # get parameters

        # start the simulation and pause
        self._simulink_start_and_pause()
        print("Simulation started and paused")

        self._update_history()

    def _get_matlab_workspace_var(self, var_name):
        # Get the variable from the MATLAB workspace
        self.eng.eval(f"temp = {var_name};", nargout=0)
        return np.array(self.eng.workspace["temp"]).flatten()

    def _update_history(self):
        # Get the simulation history
        self.yHistory = self._get_matlab_workspace_var("out.simout")
        self.tHistory = self._get_matlab_workspace_var("out.tout")

    def step(self, u):
        if self.eng.get_param(self.model_name, "SimulationStatus") != (
            "stopped" or "terminating"
        ):
            self._simulink_set_u(u)
            self._simulink_step()
            self._update_history()


if __name__ == "__main__":
    tic = time.time()
    test_simulink = TestSimulink()
    test_simulink.start()
    print("Simulation started")
    for i in range(10):
        tic2 = time.time()
        test_simulink.step(i)
        tic2 = time.time() - tic2
        print(
            f"Step {i+1}， u: {test_simulink.u}"
            f", t: {test_simulink.tHistory[-1]:.2f}, y: {test_simulink.yHistory[-1]:.2f}"
            f", time: {tic2:.2f} seconds"
        )
    tic = time.time() - tic
    print(f"External elapased time: {tic:.2f} seconds")
