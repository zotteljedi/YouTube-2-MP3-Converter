FROM python:3.7-alpine
MAINTAINER zotteljedi

# Copy root
COPY . /

# install requirements by python app
RUN pip install --no-cache-dir -r /requirements.txt

# setup db
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

# third party
RUN apk add  --no-cache ffmpeg

# set entrypoint
CMD ["python3", "/run.py"]