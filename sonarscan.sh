#!/usr/bin/env bash

/opt/sonar-scanner-3.3.0.1492-linux/bin/sonar-scanner \
-Dsonar.projectKey=euler_python   \
-Dsonar.sources=.   \
-Dsonar.host.url=http://10.152.183.181:9000   \
-Dsonar.login=34d7255ef06ee63e7826c15146b42f49256e8497