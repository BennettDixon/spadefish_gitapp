# prepare builder stage of image
FROM node:alpine as builder
# set working directory
WORKDIR '/app'
# copy files to build image
COPY ./package.json ./
RUN npm install
# split run/copy cmds to cache the packages version of the image
COPY ./ ./
# run the npm deploy script in package.json
RUN npm run deploy


# production stage, use the files built
FROM nginx:alpine
# TODO fix how its build and copied
COPY --from=builder /app/lib /user/share/nginx/html/lib
COPY --from=builder /app/css /user/share/nginx/html/css