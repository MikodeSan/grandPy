const dialog = document.getElementById('dialog');


const addReply = (_strReply) => {

    div = addTextDiv();
    time = localTime();

    div.innerHTML = "<p>" + time + " - " + _strReply + "</p>";
    div.classList.add("reply_style");
}

const addQuery = (_strUserQuery) => {

    div = addTextDiv();
    time = localTime();

    div.innerHTML = "<p>" + _strUserQuery + " - " + time + "</p>";
    div.classList.add("query_style");
}

const addTextDiv = () => {

    const div = document.createElement("div");
    dialog.appendChild(div);

    return div;
}

const localTime = () => {
    date = new Date();
    return date.toLocaleTimeString();
}

const userInput_form = document.getElementById('user_input_form');
userInput_form.addEventListener('submit', function(event) {

    event.preventDefault();
    event.stopPropagation();

    const userText_form = document.getElementById('query_text');

    strUserText = userText_form.value;
    if (strUserText) {

        addQuery(strUserText);
        addReply(strUserText);
    }
    userText_form.value = "";

    let user_Object = {
        my_query: strUserText
    };

    // Création d'un objet FormData
    var formData = new FormData(userInput_form);

    // Création et configuration d'une requête HTTP POST vers le fichier post_form.php
    var req = new XMLHttpRequest();

    req.addEventListener("load", function() {
        if (req.status >= 200 && req.status < 400) {
            // Appelle la fonction callback en lui passant la réponse de la requête 
            console.log(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function() {
        console.error("Erreur réseau avec l'URL " + url);
    });

    req.open("POST", "http://127.0.0.1:5000/content");
    // Envoi de la requête en y incluant l'objet
    req.send(formData);

    // let request = new XMLHttpRequest();
    // request.open("POST", "http://127.0.0.1:5000/content/");
    // request.setRequestHeader("Content-Type", "application/json");
    // tmp = JSON.stringify(user_Object)
    // console.log(tmp)

    // print(tmp)
    // request.send(tmp);
    // console.log('post request')
});

//elt.removeChild(newElt);    // Supprime l'élément newElt de l'élément elt
//elt.replaceChild(document.createElement("article"), newElt);    // Remplace l'élément newElt par un nouvel élément de type article