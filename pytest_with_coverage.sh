#!/usr/bin/env bash
python -m pytest \
--cov=euler_python \
--cov-report xml:coverage-reports/coverage-euler_python.xml

