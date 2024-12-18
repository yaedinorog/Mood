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


const burgerBtn = document.querySelector('.burger-btn');
const menu = document.querySelector('.menu');
const closeButton = document.querySelector('.menu-close');

// Открытие меню
burgerBtn.addEventListener('click', function() {
    menu.classList.add('active'); 
});

// Закрытие меню
closeButton.addEventListener('click', function() {
    menu.classList.remove('active'); 
});

// Закрытие меню при клике вне его
document.addEventListener('click', function(event) {
    if (!menu.contains(event.target) && !burgerBtn.contains(event.target)) {
        menu.classList.remove('active');
    }
});

// Получаем элементы
const copyText = document.getElementById('copyText');
const WinWin = document.getElementById('modal');
const closeModal = document.querySelector('.close');

// Ссылка для копирования (можно использовать любую ссылку)
const linkToCopy = "https://www.example.com";

// Функция для копирования ссылки в буфер обмена
copyText.addEventListener('click', function() {
    // Создаём временный элемент input для копирования ссылки
    const tempInput = document.createElement('input');
    tempInput.value = linkToCopy;
    document.body.appendChild(tempInput);
    
    // Выбираем и копируем текст
    tempInput.select();
    document.execCommand('copy');
    
    // Удаляем временный input
    document.body.removeChild(tempInput);
    
    // Показываем модальное окно
    modalWin.style.display = 'flex';

    // Закрываем модальное окно через 2 секунды
    setTimeout(function() {
        modalWin.style.display = 'none';
    }, 2000);
});

// Закрытие модального окна при нажатии на крестик
closeModal.addEventListener('click', function() {
    modalWin.style.display = 'none';
});
