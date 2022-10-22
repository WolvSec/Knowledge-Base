FROM debian:latest

RUN apt-get update -y

RUN apt-get install -y apt-transport-https

RUN apt-get install -y \
    build-essential gdbserver cmake pkg-config \
    strace curl wget gcc zsh vim gdb git netcat tmux \
    procps python3 python3-pip python3-dev file binutils sudo locales \
    ruby-standalone

RUN gem install one_gadget

RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en

RUN useradd --create-home --groups sudo --shell /bin/zsh wolvsec
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
WORKDIR /home/wolvsec
USER wolvsec

ENV PATH="${PATH}:/home/wolvsec/.local/bin"

RUN pip3 install pwntools numpy ipython z3-solver

RUN bash -c "$(curl -fsSL https://gef.blah.cat/sh)"

ENTRYPOINT [ "/bin/zsh" ]
