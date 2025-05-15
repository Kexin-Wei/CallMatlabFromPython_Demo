# Install matlab engine

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

