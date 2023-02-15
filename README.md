<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Простой Django + Stripe API бэкенд</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f6f8fa;
      }
      .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 30px;
        background-color: #fff;
        border-radius: 5px;
        box-shadow: 0 0 10px rgba(0,0,0,.1);
      }
      h1 {
        font-size: 32px;
        text-align: center;
        margin-top: 0;
      }
      h3 {
        font-size: 24px;
        text-align: center;
        margin-top: 10px;
      }
      a {
        color: #0366d6;
        text-decoration: none;
      }
      a:hover {
        text-decoration: underline;
      }
      ul {
        list-style: none;
        padding: 0;
        margin: 0;
      }
      li {
        margin-bottom: 10px;
      }
      .step {
        display: flex;
        align-items: center;
        margin-bottom: 30px;
      }
      .step .number {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 40px;
        height: 40px;
        background-color: #0366d6;
        color: #fff;
        font-size: 24px;
        font-weight: bold;
        border-radius: 50%;
        margin-right: 20px;
      }
      .step h4 {
        font-size: 24px;
        margin: 0;
      }
      .step p {
        margin: 0;
      }
      .bonus {
        border-top: 1px solid #e1e4e8;
        padding-top: 30px;
      }
      .bonus h4 {
        margin-top: 0;
      }
      .bonus ul {
        display: flex;
        flex-wrap: wrap;
      }
      .bonus li {
        width: calc(33.33333% - 20px);
        margin-right: 20px;
      }
      .bonus h5 {
        font-size: 18px;
        margin-bottom: 10px;
      }
      .bonus p {
        margin: 0;
      }
      .bonus i {
        font-size: 24px;
        margin-right: 5px;
        color: #0366d6;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Всем привет, я <a href="https://www.gilmanov.net/" target="_blank">Константин</a> <img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
      <h3>Этот репозиторий содержит решение тестового задания по созданию простого Django + Stripe API бэкенда.</h3>
      <div class="steps">
<h4>Установка и запуск</h4>
        <ul>
          <li class="step">
            <div class="number">1</div>
            <div class="info">
<div>
  <h4>Установка и запуск <img src="https://github.githubassets.com/images/icons/emoji/rocket.png" height="30"/></h4>
  <p>Чтобы запустить приложение локально, выполните следующие шаги:</p>
  <ol>
    <li>Клонируйте репозиторий: <code>git clone https://github.com/your_username/your_repository.git</code></li>
    <li>Перейдите в директорию проекта: <code>cd your_repository</code></li>
    <li>Установите зависимости: <code>pip install -r requirements.txt</code></li>
    <li>Создайте базу данных: <code>python manage.py migrate</code></li>
    <li>Запустите сервер: <code>python manage.py runserver</code></li>
    <li>Откройте браузер и перейдите по адресу <a href="http://localhost:8000/">http://localhost:8000/</a></li>
  </ol>
  <p>Для запуска приложения с использованием Docker выполните следующие шаги:</p>
  <ol>
    <li>Установите Docker и Docker Compose</li>
    <li>Склонируйте репозиторий и перейдите в директорию проекта</li>
    <li>Соберите Docker-образ: <code>docker-compose build</code></li>
    <li>Запустите Docker-контейнер: <code>docker-compose up</code></li>
    <li>Откройте браузер и перейдите по адресу <a href="http://localhost:8000/">http://localhost:8000/</a></li>
  </ol>
</div>