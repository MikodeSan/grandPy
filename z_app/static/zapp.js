const dialog = document.getElementById('dialog');
console.log(dialog);


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


const elt = document.getElementById('user_input_form');
elt.addEventListener('submit', function(event) {

    event.preventDefault();
    event.stopPropagation();

    const userText_form = document.getElementById('query_text');

    strUserText = userText_form.value;
    if (strUserText) {

        addQuery(strUserText);
        addReply(strUserText);
    }
    userText_form.value = "";
});

//elt.removeChild(newElt);    // Supprime l'élément newElt de l'élément elt
//elt.replaceChild(document.createElement("article"), newElt);    // Remplace l'élément newElt par un nouvel élément de type article