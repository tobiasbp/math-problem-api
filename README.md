# math-problem-api
A REST API for math problems. Developed with [FastAPI](https://fastapi.tiangolo.com).
See the documentation, and try out the latest development version of the
API [here](https://ir9z2y.deta.dev/docs).

The API wraps the Python package [_math-problem-generator_](https://github.com/tobiasbp/math-problem-generator).

# Development
* Setup Python virtual environment: `python3 -m venv .venv`
* Activate virtual environment: `source .venv./bin/activate`
* Install Python packages : `pip install -r scr/requirements.txt`
* Install Python packages for development: `pip install -r requirements-dev.txt`
* Deactive virtual environment when done: `deactivate`

# How to run
* Go to dir _src_
* Start server: `uvicorn main:app --reload`
* Explore documentattion: `http://127.0.0.1:8000/docs`