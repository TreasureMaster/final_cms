FROM python:3.10

ARG PROJECT_ENVIRONMENT_TYPE
# ARG PIP_REQUIREMENTS
# ARG WORK_DIR

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip setuptools
COPY ./sysadmin/requirements /tmp/requirements/
RUN pip3 install -r /tmp/requirements/${PROJECT_ENVIRONMENT_TYPE}.txt
#  && useradd -ms /bin/bash auction

# USER auction

# WORKDIR /home/auction
# WORKDIR ${WORK_DIR}

# COPY --chown=auction ./auction-project /home/auction/
# COPY --chown=auction ./auction-project ${WORK_DIR}

WORKDIR /app
COPY . /app
# RUN chmod ug+x -R ./entrypoints
# COPY ./entrypoints/supervisor/${PROJECT_ENVIRONMENT_TYPE}.conf /etc/supervisor/supervisord.conf