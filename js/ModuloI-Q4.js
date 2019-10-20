const fisica = {
    nome: 'Física',
    alunos: ['Iago', 'João'],
    localização: {
        bloco: 3,
        sala: 4
    }
}

const {localização: {sala: sala} } = fisica
console.log(sala)