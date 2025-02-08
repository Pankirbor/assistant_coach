# FROM node:20-alpine as build
# WORKDIR /app
# COPY package*.json ./
# RUN npm install
# COPY . ./
# RUN npm run build_coach
# CMD cp -r build result_build

# Шаг 1: Используйте официальный Node.js образ как базовый
FROM node:18 as build

# Шаг 2: Установите рабочую директорию
WORKDIR /usr/src/app

# Шаг 3: Копируйте package.json и package-lock.json
COPY package*.json ./

# Шаг 4: Установите зависимости
RUN npm install

# Шаг 5: Копируйте все остальные файлы в контейнер
COPY . .

# Шаг 6: Сборка приложения
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
