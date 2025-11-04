#init a base image ()
FROM python

EXPOSE 5000


#define present working directory
WORKDIR /demo-deployment

#copy the contain to the working dir
ADD . /demo-deployment

#run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt

#define the command to start the container
CMD ["flask", "run", "--host", "0.0.0.0"]



