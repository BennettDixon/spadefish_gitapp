# base python image
FROM python:3.5.7-alpine3.8

# set working directory
WORKDIR '/app'

RUN pip3 install flask && \
    pip3 install requests

# move backend directory into root of app directory
# OK b/c backend image contains no frontend code
COPY ./backend .
# copy models into the backend api directory for use
COPY ./models ./api/v1/models