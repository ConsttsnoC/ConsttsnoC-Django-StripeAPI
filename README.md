<!-- Заголовок -->
<h1 align="center">
  <br>
  Простое Django-приложение с использованием Stripe API
  <br>
</h1>
<!-- Описание -->
<p align="center">
  <a href="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" target="_blank">

  </a>
</p>
<!-- Иконки -->
<p align="center">
  <img src="https://img.shields.io/badge/Django-3.2.7-green">
  <img src="https://img.shields.io/badge/Python-3.8.10-blue">
  <img src="https://img.shields.io/badge/Stripe-API-orange">
  <img src="https://img.shields.io/badge/Deploy-Docker-blueviolet">
</p>

 <div>
      <h1>Всем привет, я <a href="https://www.gilmanov.net/" target="_blank">Константин</a> <img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
      <h3>Этот репозиторий содержит решение тестового задания по созданию Django + Stripe API бэкенда.</h3>
  <center>
<a href="https://stripeapi.pythonanywhere.com/" style="display: inline-block; background-color: #1e88e5; color: #ffffff; padding: 12px 24px; border-radius: 5px; text-decoration: none; font-size: 18px; font-weight: bold; text-align: center;">DEMO</a>
</center>

<h4>Установка и запуск <img src="https://github.githubassets.com/images/icons/emoji/rocket.png" height="30"/></h4>
  <p>Чтобы запустить приложение локально, выполните следующие шаги:</p>
  <ol>
    <li>Клонируйте репозиторий: <code>git clone https://github.com/ConsttsnoC/ConsttsnoC-Django-StripeAPI.git</code></li>
    <li>Перейдите в директорию проекта: <code>cd \TestProject\payment_root</code></li>
<li>Создайте и активируйте виртуальное окружение:</li>

<code>python3 -m venv venv</code>

<code>.\env\Scripts\activate</code>
<li>Установите зависимости: <code>pip install -r requirements.txt</code></li>
<li>Создайте базу данных: <code>python manage.py migrate</code></li>
<li>Запустите сервер: <code>python manage.py runserver</code></li>
<li>Откройте браузер и перейдите по адресу <a href="http://localhost:8000/"></a>http://localhost:8000/
</ol>

<h4>Docker <img src="https://github.githubassets.com/images/icons/emoji/rocket.png" height="30"/></h4>
<p>Чтобы запустить приложение через Docker, выполните следующие шаги:</p>
<ol>
<li>Загрузите и установите <a href="https://www.docker.com/products/docker-desktop/">Docker</a></li>
<li>Собрать проект <code>docker-compose build</code></li>
<li>Запустить проект <code>docker-compose up -d</code></li>
<li>Остановить проект <code>docker-compose down</code></li>
</ol>
