FROM scratch

LABEL maintainer="radovan.jakab@t-systems.com"

ADD alpine-minirootfs-3.13.5-x86_64.tar.gz /

RUN apk add cmatrix

CMD ["/usr/bin/cmatrix"]
