FROM ubuntu:latest as build

WORKDIR /Blueyes

RUN echo "Welcome to Blueyes"
RUN echo "--------------------------------"
RUN echo "Now Installing Blueyes"
RUN apt-get   update
RUN docker pull mysql
RUN echo systemctl service mysql start
COPY pyproject.toml pyproject.toml
RUN echo "--------------------------------"
FROM python:latest 
RUN  python -m build

CMD ["echo", "Main.py"]