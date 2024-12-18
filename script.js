const header = document.getElementById('header');

window.addEventListener('scroll', function() {
    const scrollY = window.scrollY;

    if (scrollY > 550) {
        header.style.backgroundColor = 'black'; 
        header.style.color = 'white'; 
    } else {
        header.style.backgroundColor = 'transparent'; 
        header.style.color = 'white'; 
    }
});

const headerUse = document.getElementById('header-use');

window.addEventListener('scroll', function() {
    const scrollY = window.scrollY;

    if (scrollY > 20) {
        headerUse.style.backgroundColor = 'black'; 
        headerUse.style.color = 'white'; 
    } else {
        headerUse.style.backgroundColor = 'transparent'; 
        headerUse.style.color = 'white'; 
    }
});

const modal = document.getElementById('myModal');
const openModalBtn = document.getElementById('openModalBtn');
const closeBtn = document.getElementsByClassName('close')[0];

openModalBtn.onclick = function() {
    modal.style.display = 'block';
}

closeBtn.onclick = function() {
    modal.style.display = 'none';
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

document.getElementById('telegramAuthBtn').addEventListener('click', function() {
    // При нажатии, автоматически инициируем авторизацию через Telegram
    const url = 'https://t.me/Mood_auth_bot?start=auth';  // Замените на ссылку к вашему боту
    window.location.href = url;  // Перенаправляем на Telegram бот
});


// Получаем элементы
const burgerBtn = document.querySelector('.burger-btn');
const menu = document.querySelector('.menu');
const closeButton = document.querySelector('.menu-close');

// Открытие бургер-меню
burgerBtn.addEventListener('click', function() {
    menu.classList.add('active'); // Добавляем класс для показа меню
});

// Закрытие бургер-меню
closeButton.addEventListener('click', function() {
    menu.classList.remove('active'); // Убираем класс для скрытия меню
});






