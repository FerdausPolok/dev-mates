//initialize
let ids = new Set()

//adding data

ids.add(1)
ids.add(1) //wont send error there there will be only 1 set
ids.add("test")
ids.add(4)
ids.add(5)

console.log(ids) //{1, 'test', 4, 5}

// delete data
ids.delete(4)

console.log(ids) //{1, 'test', 5}

// Iterate through array
// only of works since index are not always same
for (let value of ids) {
    console.log(value) //"Polok" "zaman" "ferdaus"
}

//finding any unique value on the set, true or false
console.log(ids.has(5)) //true
console.log(ids.has(100)) //false 


//convert array into set
let myArray = ["polok", 1, 2, 1, "zaman", "polok"]
let mySet = new Set(myArray)

console.log(mySet) //{'polok', 1, 2, 'zaman'}
