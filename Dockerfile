FROM python:3.9-slim
WORKDIR /usr/src/app
ADD /loaderio-eeef6ede4ae688b61da6ad126031492a.txt /usr/src/app
ADD index.html /usr/src/app
ADD script.js /usr/src/app
ADD styles.css /usr/src/app
CMD ["python", "-m", "http.server", "8080"]
