FROM python:alpine 

LABEL maintainer="Radovan Jakab <radovan.jakab@t-systems.com>"

ADD https://github.com/madrade/textadventure/archive/refs/heads/2021.05-tsys.zip /

RUN unzip 2021.05-tsys.zip -d app

WORKDIR /app/textadventure-2021.05-tsys

CMD [ "/usr/bin/env", "python3", "game.py" ]

