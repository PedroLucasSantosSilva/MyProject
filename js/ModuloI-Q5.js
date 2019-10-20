const aluno = {
    nome: 'iago',
    notas: [
        { nome: 'fisica', valor: 5 },
        { nome: 'estatistica', valor: 4 },
        {nome: 'probabilidade', valor: 1 }
    ]
}

notas = aluno.notas
console.log([notas[0].valor, notas[1].valor, notas[2].valor])
//console.log(aluno.notas[0].valor)