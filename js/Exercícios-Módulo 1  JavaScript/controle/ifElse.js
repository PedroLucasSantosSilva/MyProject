const imprimirRessultado = function(nota) {
    if(nota >= 7){
        console.log('Aprovado!')
    }else {
        console.log('Reprovado!')
    }
}

imprimirRessultado(10)
imprimirRessultado(4)
imprimirRessultado('Epa!') // Linguagem fracamente tipada, cuidado!!!
imprimirRessultado('10')