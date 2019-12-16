const dialog = document.getElementById('dialog');
console.log(dialog);

const nDialog = 10;

const addReply = (_strReply, _idx) => {
    
    div = addTextDiv();
    time = localTime();

    div.innerHTML = "<p>" + time + " - " + _strReply + " #" + _idx + "</p>";
    div.classList.add("reply_style");
}

const addQuery = (_strUserQuery, _idx) => {
    
    div = addTextDiv();
    time = localTime();

    div.innerHTML = "<p>" + _strUserQuery + " #" + _idx + " - " + time + "</p>";
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


for (let i = 0; i < nDialog; i++) {
    addQuery("my new query", i);
    addReply("my new reply", i);
}

//elt.removeChild(newElt);    // Supprime l'élément newElt de l'élément elt
//elt.replaceChild(document.createElement("article"), newElt);    // Remplace l'élément newElt par un nouvel élément de type article



