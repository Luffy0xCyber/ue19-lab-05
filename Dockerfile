FROM python:3.13.0

RUN useradd -m -s /bin/bash user
USER user

WORKDIR /home/user/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN rm requirements.txt

COPY src .

ENTRYPOINT ["python", "app.py"]
