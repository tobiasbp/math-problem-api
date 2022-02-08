from enum import Enum
from sys import maxsize
from math_problem_generator import generator as mg

from fastapi import FastAPI, Query

app = FastAPI()


class ValidOperators(str, Enum):
    addition = "add"
    subtraction = "sub"
    multiplication = "mul"
    division = "div"


@app.get("/v1/problem/math/simple/{op}")
async def root(
    op: ValidOperators,
    no_of_problems: int = Query(
        25,
        ge=1,
        le=100,
    ),
):
    return mg.simple_problems(op=op, no_of_problems=no_of_problems)
