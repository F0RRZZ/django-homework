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

select.addEventListener('change', changeURLLanguage);

function changeURLLanguage() {
    let language = select.value;
    location.href = window.location.pathname + '#' + language;
    location.reload();
}

function changeLanguage() {
    let hash = window.location.hash;
    hash = hash.substr(1);
    if (!allLang.includes(hash)) {
        location.href = window.location.pathname + '#ru';
        location.reload();
    }
    select.value = hash;
    document.querySelector('.lng-home').innerHTML = langArr['home'][hash];
    document.querySelector('.lng-catalog').innerHTML = langArr['catalog'][hash];
    document.querySelector('.lng-about').innerHTML = langArr['about'][hash];
}

changeLanguage();
