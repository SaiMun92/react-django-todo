# pull official base image
FROM node:12.19.0

# set working directory
WORKDIR /app/frontend

# add `/app/node_modules/.bin` to $PATH
#ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# add app
COPY . ./

EXPOSE 3000

# start app
CMD ["npm", "run", "dev"]
