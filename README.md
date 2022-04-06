# math-problem-api
A REST API for math problems. Developed with [FastAPI](https://fastapi.tiangolo.com).
This API wraps the Python package [_math-problem-generator_](https://github.com/tobiasbp/math-problem-generator).

See the documentation, and try out the latest versions of the API:
* Development (Deployed on any oush to main branch): https://math-problem-api-dev.deta.dev/docs
* Production (Deployed on release): https://math-problem-api-prod.deta.dev/docs


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