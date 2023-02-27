const activePage = window.location.pathname;
document.querySelectorAll('a').
forEach(link => {
    if (link.href.includes(`${activePage}`) && activePage != '/') {
        link.classList.add('active');
        link.classList.add('disabled');
        link
    } else if (activePage == '/') {
        if (link.href == 'http://127.0.0.1:8000/'){
            link.classList.add('active');
            link.classList.add('disabled');
        }
    }
});
