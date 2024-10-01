// It's more like database

const resultMap = new Map()

//set
resultMap.set('average', 1.53)
resultMap.set('lastResult', null)

const germany = { name: 'Germany', population: 82 }

resultMap.set(germany, 0.89)

//get
console.log(resultMap.get("average")) //1.53

//delete
resultMap.delete(germany)

// iteration of is possible
for (let item of resultMap) {
    console.log(item) // items as individual array
}
