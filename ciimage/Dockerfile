FROM ubuntu

ENV \
  PYTHON3_CMD=python3 \
  PY_INSTALLE=run_install.py \
  PY_STARTUP=run_startup.py

RUN apt-get update && apt-get upgrade -y
RUN apt-get -y install ${PYTHON3_CMD} ${PYTHON3_CMD}-pip

ADD ${PY_INSTALLE} .
ADD ${PY_STARTUP} .

RUN ${PYTHON3_CMD} ${PY_INSTALLE} && ${PYTHON3_CMD} ${PY_STARTUP}