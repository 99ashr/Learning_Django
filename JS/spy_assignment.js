var first_name = prompt("Enter your First Name here!: ");
var last_name = prompt("Enter your Last Name here!: ");
var age = prompt("How old are you?: ");
var height = prompt("How tall are you?: ");
var pet_name = prompt("What is the name of your pet?: ");


var namecond = null;
var agecond = null;
var heightcond = null;
var petcond = null;

// Name Condition!!!
if (first_name[0] === last_name[0]) {
    namecond = true;
} else {
    namecond = false;
}
// Age Condition!!!
if (age >= 21 && age <= 29) {
    agecond = true;
} else {
    agecond = false;
}
// Height Condition!!!
if (height >= 170) {
    heightcond = true;
} else {
    heightcond = false;
}
// Pet Name Condition!!!
if (pet_name[pet_name.length - 1] === 'y') {
    petcond = true;
} else {
    petcond = false;
}

if (namecond && agecond && heightcond && pet cond) {
    console.log("You got it!!!hehehehehe....");
} else {
    console.log("Fuck Off!");
}