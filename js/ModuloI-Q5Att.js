const aluno = {
    nome: 'iago',
    notas: [
        { nome: 'fisica', valor: 5 },
        { nome: 'estatistica', valor: 4 },
        {nome: 'probabilidade', valor: 1 }
    ]
}

const apenasValor = num => num.valor

const resultado = aluno.notas.map(apenasValor)
console.log(resultado)