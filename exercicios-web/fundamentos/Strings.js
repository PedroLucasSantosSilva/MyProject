const escola = "Cod3r"

console.log(escola.charAt(4))
console.log(escola.charAt(5)) // não encontra um char nesse índice
console.log(escola.charCodeAt(3)) // valor na tabela ASCII ou unicode
console.log(escola.indexOf('3')) // procura o índice associado ao dígito

console.log(escola.substring(1)) // vai iniciar a partir do índice 1
console.log(escola.substring(0, 3)) // vai do índice 0 ao 3 sem incluir o índice 3

console.log('Escola '.concat(escola).concat ("!"))
console.log('Escola ' + escola + "!") // também é uma concatenação
console.log(escola.replace(3, 'e')) // substitui, ver regex

console.log('Ana,Maria,Pedro'.split(','))