FROM python:3.9-slim
WORKDIR /usr/src/app
ADD /loaderio-076c28cc9768845a827bec34e9b3aa9b /usr/src/app
ADD index.html /usr/src/app
ADD script.js /usr/src/app
ADD styles.css /usr/src/app
ADD requirements.txt /usr/src/app
ADD main.py /usr/src/app
RUN pip install -r requirements.txt
CMD ["python3", "main.py"]
