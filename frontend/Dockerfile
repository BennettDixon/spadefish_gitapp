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
# Copy from builder so only files needed are included in final image
COPY --from=builder /app/lib/main.js /usr/share/nginx/html/lib/main.js
COPY --from=builder /app/css/main.css /usr/share/nginx/html/css/main.css
COPY --from=builder /app/about.html /usr/share/nginx/html/about.html
COPY --from=builder /app/index.html /usr/share/nginx/html/index.html