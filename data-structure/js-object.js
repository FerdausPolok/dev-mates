const person = {
    firstName: "Ferduas",
    age: 25,
    lastName: "Polok",
    hobbies: ["Code", "Games"],
    age: 26,
    greet() {
        console.log("Hi! I'm ", this.firstName)
    }
};

console.log(person.age); //overwritten that why last one

//Add new property
person.height = "100cm";

//Delete property
delete person.age;

person.greet(); //Hi! I'm Ferdaus
