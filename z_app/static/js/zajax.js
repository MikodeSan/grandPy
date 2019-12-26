function afficher(reponse) {
    console.log(reponse);
}

function zajaxGet(url, callback) {

    let request = new XMLHttpRequest();

    request.open("GET", url);

    request.addEventListener("load", function() {
        if (request.status >= 200 && request.status < 400) {

            /* reply of the request */
            callback(request.responseText);
        } else {
            console.error(request.status + " " + request.statusText + " " + url);
        }
    });
    request.addEventListener("error", function() {
        console.error("Erreur réseau avec l'URL " + url);
    });
    request.send(null);
}

function zajaxPost(url, data, callback, isJson) {

    let request = new XMLHttpRequest();

    request.open("POST", url);

    request.addEventListener("load", function() {
        if (request.status >= 200 && request.status < 400) {

            callback(request.responseText);
        } else {
            console.error(request.status + " " + request.statusText + " " + url);
        }
    });

    request.addEventListener("error", function() {
        console.error("Erreur réseau avec l'URL " + url);
    });

    if (isJson) {
        req.setRequestHeader("Content-Type", "application/json");
        data = JSON.stringify(data);
    }

    request.send(data);
}