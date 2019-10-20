const joao = {
    nome: 'João',
    saudacao() {
        console.log(`Olá ${this.nome}`)
    }
}

falar = {nome: 'Maria'}
const saudacoaMaria = joao.saudacao.bind(falar)
saudacoaMaria()