var async_spinner_id;
var isDone = false;

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

async function wait_trigger() {

    while (isDone == false) {};
    return;
};


async function getAddress(reply_json) {
    console.log('isdone =' + isDone);

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

    console.log('isdone =' + isDone);
    await setTimeout(function() {
        isDone = true;
        console.log('trigger timeout');
    }, 3000);
    console.log('isdone =' + isDone);
    isDone = false;


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

        // disable text input form
        // Last name: <input type="text" name="lname" disabled><br>

        addQuery(strUserText);

        // Display spinner and start interval timer
        display_spinner();
        // async_spinner_id = setInterval(function() { display_spinner() }, 250);

        // start spinner timout delay
        // setTimeout(function() { clearInterval(async_spinner_id); }, 3000);
        // setTimeout(function() {
        //     isDone = true;
        //     console.log('trigger timeout');
        // }, 3000);

        // // Création des informations sur le profil
        // var avatarElt = document.createElement("img");
        // avatarElt.src = profil.avatar_url;
        // avatarElt.style.height = "150px";
        // avatarElt.style.width = "150px";

        let data = new FormData(userInput_form);

        zajaxPost(parse_url, data, getAddress, remove_maps_loader, false);

        userText_form.value = "";
    }
});

const remove_maps_loader = () => {

    let div = document.getElementById("map_loader_id");

    if (div) {
        var waitUntil = new Date().getTime() + 1.5 * 1000;
        while (new Date().getTime() < waitUntil) true;

        div.parentNode.removeChild(div);
    }
};


const display_spinner = () => {

    div = addTextDiv();

    // div.innerHTML = "<p><i id='spin_id' class='far fa-compass'></i></p>";
    // div.innerHTML = "<p><img class='home_avatar' src={{ url_for( 'static', filename='img/grand_father_lineal_color_2369096.png' ) }}/>";
    // div.innerHTML = "<p class='loader'><img id='pin_id' class='home_avatar' src='../static/img/grand_father_lineal_color_2369096.png'/></p>";
    div.innerHTML = "<p><img class='loader' src='../static/img/compass-regular.svg'/></p>";
    div.id = "map_loader_id";
    div.classList.add("reply_style");

    // var c = document.getElementById("spin_id");
    // console.log(c)
    // var ctx = c.getContext("2d");
    // console.log(ctx)

    // ctx.rotate(20 * Math.PI / 180);
}

//elt.removeChild(newElt);    // Supprime l'élément newElt de l'élément elt
//elt.replaceChild(document.createElement("article"), newElt);    // Remplace l'élément newElt par un nouvel élément de type article