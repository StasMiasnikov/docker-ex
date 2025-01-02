FROM jenkins/ssh-agent
USER root
RUN apt-get update &&  apt-get install -y make autoconf libtool openssl libpsl-dev
RUN chown -R 1000:1000 /usr/local/
