FROM python:3
WORKDIR /usr/src/app
ADD ./main.py /usr/src/app
ADD ./requirements.txt /usr/src/app
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
