// initiate array
const names = ["Polok", "zaman", "ferdaus"];
const namesUsingContractor = new Array("Polok", "zaman", "ferdaus", "Polok");

// Iterate through array
// of -> value in -> index
for (let name of names) {
    console.log(name) //"Polok" "zaman" "ferdaus"
}

for (let index in names) {
    console.log(index) //0 1 2
}

//inserting
names.push("newname") // add to the end
names.unshift("start") // add to the beginning

// Finding in array
// O(n)
let isMatchName = names.find(name => name == "Polok") //RETURN the main finding value if found else undefined
let isMatchIndex = names.findIndex(name => name == "ferdaus") //RETURN the first index found for given value


// Deleting Array element
let position = 2
let numElementsToDelete = 1
names.splice(position, numElementsToDelete);