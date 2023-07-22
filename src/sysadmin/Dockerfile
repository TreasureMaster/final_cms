FROM python:3.10

ARG PROJECT_ENVIRONMENT_TYPE

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip setuptools
COPY ./requirements /tmp/requirements/
RUN pip3 install -r /tmp/requirements/${PROJECT_ENVIRONMENT_TYPE}.txt
#  && useradd -ms /bin/bash auction

# USER auction

# COPY --chown=auction ./auction-project /home/auction/

WORKDIR /app
COPY . /app
RUN chmod ug+x ./entrypoints/entrypoint.sh
# COPY ./entrypoints/supervisor/${PROJECT_ENVIRONMENT_TYPE}.conf /etc/supervisor/supervisord.conf