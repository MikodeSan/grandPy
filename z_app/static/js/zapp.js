const dialog = document.getElementById('dialog');


const addQuery = (_strUserQuery) => {

    div = addTextDiv();
    time = localTime();

    div.innerHTML = "<p>" + _strUserQuery + " - " + time + "</p>";
    div.classList.add("query_style");
}

const addReply = (_strReply) => {

    div = addTextDiv();
    time = localTime();

    div.innerHTML = "<p>" + time + " - " + _strReply + "</p>";
    div.classList.add("reply_style");
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


getAddress = (address_json) => {

    console.log(address_json);
    addr = JSON.parse(address_json);

    reply = "the reply" + " " + addr.query_text
    console.log(reply);

    addReply(reply);
}


const userInput_form = document.getElementById('user_input_form');
userInput_form.addEventListener('submit', function(event) {

    event.preventDefault();
    event.stopPropagation();

    const userText_form = document.getElementById('query_text');

    strUserText = userText_form.value;
    if (strUserText) {

        addQuery(strUserText);
    }

    let user_Object = {
        my_query: strUserText
    };

    // // Création des informations sur le profil
    // var avatarElt = document.createElement("img");
    // avatarElt.src = profil.avatar_url;
    // avatarElt.style.height = "150px";
    // avatarElt.style.width = "150px";

    let data = new FormData(userInput_form);

    zajaxPost("http://127.0.0.1:5000/content/", data, getAddress, false);

    userText_form.value = "";
});

//elt.removeChild(newElt);    // Supprime l'élément newElt de l'élément elt
//elt.replaceChild(document.createElement("article"), newElt);    // Remplace l'élément newElt par un nouvel élément de type article