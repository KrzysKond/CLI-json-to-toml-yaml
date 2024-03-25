FROM python:3.9
LABEL authors="KrzysKond"

RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user

ADD main.py .

RUN pip install --upgrade pip
RUN pip install toml
RUN pip install pyyaml

USER app_user
COPY . .
CMD ["bash"]