#!/bin/bash

python -m pytest -s -vv --failed-first -x --cov-report term-missing --cov=. tests
