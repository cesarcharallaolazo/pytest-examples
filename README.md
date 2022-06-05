# Pytest Examples

##### Some Steps

1. pytest .

2. pytest test_math_func.py

3. pytest test_math_func.py::test_add

4. pytest test_math_func.py -v -k "add or string"

5. pytest test_math_func.py -v -m number

6. pytest test_math_func.py -v -m strings

7. (set failure beforehand) pytest test_math_func.py -v --tb=no (-x) (--maxfail=1)

8. printing: pytest test_math_func.py -v -s

9. quiet mode: pytest test_math_func.py -q

##### Setup & Teardown module (Fixtures)

1. pytest test_student_func.py -v

2. pytest test_student_func.py -v -s (print setup & teardown)
