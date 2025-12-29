FROM ubuntu:latest
LABEL authors="vo"

ENTRYPOINT ["top", "-b"]