# Pytest Examples

##### Some Steps

1. pytest tests/ . -v

2. pytest tests/test_math_func.py -v

3. pytest tests/test_math_func.py::test_add -v

4. pytest tests/test_math_func.py -v -k "add or string"

5. pytest tests/test_math_func.py -v -m number

6. pytest tests/test_math_func.py -v -m strings

7. (set failure beforehand) pytest tests/test_math_func.py -v --tb=no (-x) (--maxfail=1) (--disable-warnings)

8. printing: pytest tests/test_math_func.py -v -s

9. quiet mode: pytest tests/test_math_func.py -q

##### Setup & Teardown module (Fixtures)

1. pytest tests/test_student_func.py -v

2. pytest tests/test_student_func.py -v -s (print setup & teardown)


##### Unit Tests & Code Coverage

        pytest tests/ . -v (--disable-warnings)     
        pytest --cov=src tests/ -v (--disable-warnings) (--cov-report term-missing)