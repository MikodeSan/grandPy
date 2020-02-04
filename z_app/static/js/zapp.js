var async_spinner_id;
var isDone = false;

// document.onload = function 
document.addEventListener('readystatechange', event => {

    // if (event.target.readyState === "interactive") { //same as:  ..addEventListener("DOMContentLoaded".. and   jQuery.ready
    //     alert("All HTML DOM elements are accessible");
    // }

    if (event.target.readyState === "complete") {
        addReply(welcome, false, null);
    }
});

var dialog = document.getElementById('dialog');


const addQuery = (_strUserQuery) => {

    div = addTextDiv();
    time = localTime();

    div.innerHTML = "<p id='query'>" + _strUserQuery + "</p>" + "<span class=time>" + time + "</span>";
    div.classList.add("query_style");
}

const addReply = (_strReply, isfound, map_url) => {

    div = addTextDiv();
    time = localTime();

    let reply = "<p id='reply'>" + _strReply + "</p>";
    // console.log(reply);

    if (isfound === true) {
        reply += "<img style='border-radius:12px' src=" + map_url + key + " alt='Static Google Map' title='Google Map'/><br/>";
    }
    reply += "<span class=time>" + time + "</span>";
    // console.log(reply);

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

    reply = data.reply;
    addReply(reply, false, null);

    if (data.address) {
        reply = "Voici: " + data.address + " @ " + "[lat.: " + data.location.lat + "; long.: " + data.location.lng + "]";
        map_url = data.map

    } else {
        reply = data.address_reply;
        isfound = false;
    }

    // console.log('isdone =' + isDone);
    // await setTimeout(function() {
    //     isDone = true;
    //     console.log('trigger timeout');
    // }, 3000);
    // console.log('isdone =' + isDone);
    // isDone = false;

    addReply(reply, isfound, map_url);

    if (data.description) {
        addReply("Mais laisse moi te parler d'une chose assez étonnante non loin de là", false, "");
        addReply(data.description, false, "");
    }

    setTimeout(function() {
        dialog_auto_scroll()
    }, 750);
    // dialog_auto_scroll();
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

        dialog_auto_scroll();

        let data = new FormData(userInput_form);

        zajaxPost(parse_url, data, getAddress, remove_maps_loader, false);

        userText_form.value = "";
    }
});

const dialog_auto_scroll = () => {
    console.log("auto-scroll");
    var dialog = document.getElementById('dialog');
    console.log(dialog.scrollTop);
    console.log(dialog.scrollHeight);
    console.log(dialog.clientHeight);

    dialog.scrollTop = dialog.scrollHeight - dialog.clientHeight;
    console.log(dialog.scrollTop);

}


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