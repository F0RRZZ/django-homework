var xmlHttp;

function getServerTime() {
    try {
        xmlHttp = new XMLHttpRequest();
    } catch (err1) {
        try {
            xmlHttp = new ActiveXObject('Msxml2.XMLHTTP');
        } catch (err2) {
            try {
                xmlHttp = new ActiveXObject('Microsoft.XMLHTTP');
            } catch (eerr3) {
                alert("AJAX not supported");
            }
        }
    }
    xmlHttp.open('HEAD', window.location.href.toString(), false);
    xmlHttp.setRequestHeader("Content-Type", "text/html");
    xmlHttp.send('');
    return xmlHttp.getResponseHeader("Date");
}

let serverTime = new Date(getServerTime());

let currentDate = new Date();

let difference = currentDate.getTime() - serverTime.getTime();

let delta = Math.abs(difference / (1000 * 60 * 60 * 24));

let year;

if (delta < 24) {
    year = currentDate.getFullYear();
} else {
    year = serverTime.getFullYear();
}
document.write("Copyright &copy; " + year + ". All rights reserved.");
