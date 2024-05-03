# Get the latest base image for python
FROM python:latest
# Put files at the image '/server/' folder.
ADD ipc_client.py /client/
# '/server/' is base directory
WORKDIR /client/
# Expose port 9898 in the container
EXPOSE 9898
# execute the command
CMD [ "python", "/client/ipc_client.py" ]