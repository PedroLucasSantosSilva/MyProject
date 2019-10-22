const obj = { a: 1, b: 2, c: 3, soma(a) { return a + b + c } }
console.log(JSON.stringify(obj)) //objeto para json

//console.log(JSON.parse("{ a: 1, b: 2, c: 3 }"))
//console.log(JSON.parse("{ 'a': 1, 'b': 2, 'c': 3 }"))
console.log(JSON.parse('{ "a": 1, "b": 2, "c": 3 }')) //objeto criado a partir de json
console.log(JSON.parse('{ "a": 1, "b": "string", "c":true, "d": {}, "e":[] }'))