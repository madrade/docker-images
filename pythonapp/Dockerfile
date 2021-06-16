FROM alpine

LABEL maintainer="Radovan Jakab <radovan.jakab@t-systems.com>"

ADD app.tgz /

RUN apk add python3 py3-pip \
	&& pip3 install uvicorn fastapi jinja2 python-multipart

WORKDIR /app

CMD [ "/usr/bin/env", "python3", "/app/dashboard.py" ] 

# CMD "/usr/bin/env python3 /app/dashboard.py"
