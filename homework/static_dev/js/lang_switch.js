const langArr = {
    'home': {
        'ru': 'На главную',
        'en': 'Home',
    },
    'catalog': {
        'ru': 'Список товаров',
        'en': 'Catalog',
    },
    'about': {
        'ru': 'О проекте',
        'en': 'About',
    },
    'new': {
        'ru': 'Новинки',
        'en': 'New items',
    },
    'friday': {
        'ru': 'Пятница',
        'en': 'Friday',
    },
    'unchanged': {
        'ru': 'Непроверенное',
        'en': 'Unchanged',
    },
    'feedback': {
        'ru': 'Обратная связь',
        'en': 'Feedback',
    },
    'admin': {
        'ru': 'Админка',
        'en': 'Admin',
    },
    'userlist': {
        'ru': 'Список пользователей',
        'en': 'Userlist'
    },
    'logout': {
        'ru': 'Выйти',
        'en': 'Logout'
    },
    'login': {
        'ru': 'Войти',
        'en': 'Login'
    },
    'signup': {
        'ru': 'Зарегистрироваться',
        'en': 'Sign up'
    },
    'profile': {
        'ru': 'Профиль',
        'en': 'Profile'
    }
}

const allLang = ['en', 'ru']
const select = document.querySelector('select');

let currentLang = localStorage.getItem('language') || 'ru';

select.addEventListener('change', changeURLLanguage);

function changeURLLanguage() {
    currentLang = select.value;
    localStorage.setItem('language', currentLang);
    location.href = window.location.pathname + '#' + currentLang;
    location.reload();
}

function changeLanguage() {
    let hash = window.location.hash;
    hash = hash.substr(1);
    if (!allLang.includes(hash)) {
        location.href = window.location.pathname + '#' + currentLang;
        location.reload();
    }
    select.value = hash;
    for (let key in langArr) {
        document.querySelector('.lng-' + key).innerHTML = langArr[key][hash];
    }
}

changeLanguage();
