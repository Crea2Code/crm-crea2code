FROM ubuntu:latest
LABEL authors="chala"

ENTRYPOINT ["top", "-b"]