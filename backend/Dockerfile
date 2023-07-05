FROM python:3.10.2-slim-bullseye

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR .

COPY ./helper/requirements/dev.txt .
RUN pip install -r dev.txt

COPY . .

# The connection was reset bug thing
#CMD ["python", "manage.py", "runserver"]