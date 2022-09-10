FROM debian:latest

RUN apt-get update

RUN apt-get install -y build-essential strace ltrace curl wget gcc

RUN apt-get install -y zsh vim gdb git

RUN apt-get install -y netcat

RUN useradd --create-home --shell /bin/zsh wolvsec
WORKDIR /home/wolvsec
