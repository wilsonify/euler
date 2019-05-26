![Lines of Code](static/lines_of_code.svg) 
![Coverage](static/code_coverage.svg)

starting from https://github.com/nayuki/Project-Euler-solutions

organize and test project euler problem solutions in python

organized by Difficulty from https://projecteuler.net/archives

prioritized easy to hard	

# Install 

## environment

```bash
python3 -m virtualenv venv
source venv/bin/activate
```

## dependencies
```bash
cd src/euler_python_package
python -m pip install -r requirements.txt
then
python -m setup.py install
or
python -m pip install .
```

# Usage
Within python, import the package
```python
import euler_python
euler_python.easy.p070.problem070()
```
or
from shell, run the script
```bash
cd src/euler_python_package/euler_python/easy
python p070.py
```

# develop
```bash
python -m pip install -r requirements.txt
cd src/euler_python_package
python -m setup.py develop
or
python -m pip install -e .
```

# test
slow running tests are skipped by default
```bash
python -m pip install -r test-requirements.txt
python -m pytest
```

# test coverage 
```bash
python -m pytest --cov=euler_python --cov-report xml:coverage-reports/coverage-euler_python.xml
```

# Analyze
```bash
sonar-scanner  \
-Dsonar.projectKey=euler_python   \
-Dsonar.sources=.   \
-Dsonar.host.url=localhost:9000   \
-Dsonar.login=34d7255ef06ee63e7826c15146b42f49256e8497

```

