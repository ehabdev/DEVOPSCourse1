FROM python:3.7-alpine
ADD . /run
WORKDIR /run
RUN pip install flask
RUN pip install MySQL-python
RUN chmod 644 rest_app.py
EXPOSE 5000
CMD ["python", "rest_app.py"]