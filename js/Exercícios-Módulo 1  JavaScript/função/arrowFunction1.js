let dobro = function (a) {
    return 2 * a
}

dobro = (a) => {
    return 2 * a
}

dobro = a => 2 * a  // quando tem um único parâmetro // return implícito
console.log(Math.PI)

let ola = function () {
    return 'Olá'
}

ola = () => {
    return 'Olá'
}

ola = () => 'Olá'
ola = _ => 'Olá' //possui um param
console.log(ola())