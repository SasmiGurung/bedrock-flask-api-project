#init a base image ()
FROM python:3.10

EXPOSE 5000


#define present working directory
WORKDIR /aws-text-summarizer

#copy the contain to the working dir
ADD . /aws-text-summarizer

#run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt

#define the command to start the container
CMD ["python", "app.py"]