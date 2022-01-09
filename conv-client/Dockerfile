FROM node:16.13.0-alpine AS client_builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM nginx:1.18.0-alpine as production-stage

RUN mkdir /app

# Copy the conf and content to docker host
COPY --from=client_builder /app/dist /app

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]