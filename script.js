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

const authButton = document.getElementById('telegramAuthBtn');

  authButton.addEventListener('click', function() {
    window.location.href = 'chats.html'; 
  });

// document.getElementById('telegramAuthBtn').addEventListener('click', function() {
//     // При нажатии, автоматически инициируем авторизацию через Telegram
//     const url = 'https://t.me/Mood_auth_bot?start=auth';  // Замените на ссылку к вашему боту
//     window.location.href = url;  // Перенаправляем на Telegram бот
// });

const checkbox = document.getElementById('checkbox');

function toggleButtonState() {
    if (checkbox.checked) {
        authButton.classList.remove('disabled');
        authButton.classList.add('active');
        authButton.disabled = false; 
    } else {
        authButton.classList.remove('active');
        authButton.classList.add('disabled');
        authButton.disabled = true; 
    }
}

checkbox.addEventListener('change', toggleButtonState);

toggleButtonState();

const burgerBtn = document.querySelector('.burger-btn');
const menu = document.querySelector('.menu');
const closeButton = document.querySelector('.menu-close');

burgerBtn.addEventListener('click', function() {
    menu.classList.add('active'); 
});

closeButton.addEventListener('click', function() {
    menu.classList.remove('active'); 
});

document.addEventListener('click', function(event) {
    if (!menu.contains(event.target) && !burgerBtn.contains(event.target)) {
        menu.classList.remove('active');
    }
});

const copyText = document.getElementById('copyText');
  const notification = document.getElementById('notification');

  async function copyLink() {
    try {
      const link = "https://t.me/your_bot"; 

      await navigator.clipboard.writeText(link);

      showNotification();
    } catch (err) {
      console.error('Ошибка при копировании: ', err);
      alert('Не удалось скопировать ссылку. Попробуйте вручную.');
    }
  }

  function showNotification() {
    notification.style.display = 'block'; 
    setTimeout(function() {
      notification.style.display = 'none';
    }, 3000); 
  }

  copyText.addEventListener('click', function(event) {
    event.preventDefault();  
    copyLink();
  });
