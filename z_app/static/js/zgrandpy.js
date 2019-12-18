import {data_1, data_2} from './utils.js';


const my_const = 10;
let sum = 0;

let myBook = {
    title: 'The Story of Tau',
    author: 'Will Alexander',
    numberOfPages: 250,
    isAvailable: true
};

class Book {
    constructor(title, author, pages) {
        this.title = title;
        this.author = author;
        this.pages = pages;
    }
}

let myBook = new Book("L'Histoire de Tao", "Will Alexander", 250);


let guests = ["Sarah Kate", "Audrey Simon", "Will Alexander"];

let firstGuest = guests[0]; // "Sarah Kate"
let thirdGuest = guests[2]; // "Will Alexander"
let undefinedGuest = guests[12]; // undefined


let userLoggedIn = true;

if (userLoggedIn === true) {
    console.log("Utilisateur connecté!");
} else {
    console.log("Alerte, intrus!");
}

switch (firstUser.accountLevel) {
    case 'normal':
        console.log('You have a normal account!');
        break;
    case 'premium':
        console.log('You have a premium account!');
        break;
    case 'mega-premium':
        console.log('You have a mega premium account!');
        break;
    default:
        console.log('Unknown account type!');
}

sum = (data_1 + data_2)*my_const;


const add = (firstVal, secondVal) => {
    return (firstVal + secondVal);
}


const dialog = document.getElementById('dialog');
dialog.innerHTML = "<p>nw dialog</p>";

