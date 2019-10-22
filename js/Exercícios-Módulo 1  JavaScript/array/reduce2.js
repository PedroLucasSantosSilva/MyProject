const alunos = [
    { nome: 'João', nota: 7.3, bolsilta: false },
    { nome: 'Maria', nota: 9.2, bolsilta: true },
    { nome: 'Pedro', nota: 9.8, bolsilta: false },
    { nome: 'Ana', nota: 8.7, bolsilta: true }
]

// Desafio 1: Todos os alunos são bolsistas?
const todosBolsistas = (resultado, bolsilta) => resultado && bolsilta
console.log(alunos.map(a => a.bolsilta).reduce(todosBolsistas))

// Desafio 2: Algum aluno é bolsista?
const algumBolsistas = (resultado, bolsilta) => resultado || bolsilta
console.log(alunos.map(a => a.bolsilta).reduce(algumBolsistas))