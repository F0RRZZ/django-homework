const activePage = window.location.pathname;
document.querySelectorAll('a').
forEach(link => {
    if (link.href.includes(`${activePage}`)) {
        link.classList.add('active');
        link.classList.add('disabled');
        }
});
