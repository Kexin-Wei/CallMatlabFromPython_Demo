# Call MATLAB from Python
Here trying two ways to call MATLAB from Python:
1. Use MATLAB Engine API for Python
2. Use MATLAB Compiler SDK to create a shared library and call it from Python

The first method is easier to use and requires Matlab to be installed on the machine. Refer to [MATLAB Engine API for Python](https://www.mathworks.com/help/matlab/matlab_external/call-matlab-functions-from-python.html) for more details. The second method is more complex and requires MATLAB Compiler SDK to be installed. Refer to [MATLAB Compiler SDK](https://www.mathworks.com/help/compiler_sdk/gs/create-a-python-application-with-matlab-code.html) for more details.

# Use MATLAB Engine API for Python
## Install matlab engine

1. check patible python version from [here](https://www.mathworks.com/support/requirements/python-compatibility.html)
2. follow [matlab instructions](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html) to install matlab engine
    ```bash
    cd "matlabroot\extern\engines\python"
    python -m pip install .
    ```
3. start test matlab engine
    ```python
    import matlab.engine
    eng = matlab.engine.start_matlab()
    ```

## Examples
## Call a simple funtion
*need to set nargout to get multiple outputs
```python
[a,b] = eng.test_add(1, 2, nargout=2)
print(a,b)
```
## Call Simulink model
```python
eng.sim("simulinkModelName")
```

# Other methods
Other ways to call a compiled Simulink model in Python
- Package the Simulink model as a Functional Mockup Unit (FMU): Call the FMU from Python using third-party libraries such as FMPy
- Package the Simulink model as a simulation service API 
(using MATLAB Production Server): RESTful API for scalable applications
- Generate C/C++ code or shared library from the Simulink 
model: Call the generated code using CTYPES or related wrappers
