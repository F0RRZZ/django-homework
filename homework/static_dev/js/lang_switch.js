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