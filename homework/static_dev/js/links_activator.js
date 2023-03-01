const activePage = window.location.pathname;
document.querySelectorAll('a').
forEach(link => {
    if (activePage != '/') {
        if (link.href != 'http://127.0.0.1:8000/') {
            if (link.href.includes(`${activePage}`)) {
                link.classList.add('active');
                link.classList.add('disabled');
            }
        }
    } else {
        if (link.href == 'http://127.0.0.1:8000/') {
            link.classList.add('active');
            link.classList.add('disabled');
        }
    }
});
