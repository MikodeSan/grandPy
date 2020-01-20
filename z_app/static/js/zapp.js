const dialog = document.getElementById('dialog');


const addQuery = (_strUserQuery) => {

    div = addTextDiv();
    time = localTime();

    div.innerHTML = "<p>" + _strUserQuery + " - " + time + "</p>";
    div.classList.add("query_style");
}

const addReply = (_strReply, isfound, map_url) => {

    div = addTextDiv();
    time = localTime();

    let reply = "<p>" + time + " - " + _strReply;
    console.log(reply);

    if (isfound === true) {
        reply += "<br/> <img src=" + map_url + " alt='Static Google Map' title='Google Map'/>";

        console.log(reply);
    }
    reply += "</p>";
    console.log(reply);

    div.innerHTML = reply;

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


getAddress = (reply_json) => {

    console.log(reply_json);
    data = JSON.parse(reply_json);
    isfound = true;
    map_url = ""

    if (data.address) {

        reply = "Address: " + data.address + " @ " + "{lat.: " + data.location.lat + "; long.: " + data.location.lng + "}";
        map_url = data.map

    } else {
        reply = "Address not found";
        isfound = false;
    }

    addReply(reply, isfound, map_url);

    if (data.description) {

        addReply(data.description, false, "");
    }
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

    zajaxPost(parse_url, data, getAddress, false);

    userText_form.value = "";
});

//elt.removeChild(newElt);    // Supprime l'élément newElt de l'élément elt
//elt.replaceChild(document.createElement("article"), newElt);    // Remplace l'élément newElt par un nouvel élément de type article