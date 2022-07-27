FROM python:3.7-alpine
ADD . /run
WORKDIR /run
RUN pip install flask
RUN pip install mysql
RUN chmod 644 rest_app.py
CMD ["python", "rest_app.py"]
