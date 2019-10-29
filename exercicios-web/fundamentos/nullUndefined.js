let valor // não inicializada
console.log(valor)
//console.log(valor2) // não foi declarado

valor = null // ausência de valor, não aponta pra nenhum local de memória
console.log(valor)
//console.log(valor.toString()) // Erro!

const produto = {}
console.log(produto.preco)
console.log(produto)

produto.preco = 3.50
console.log(produto)

produto.preco = undefined // evite atribiur undefined
console.log(!!produto.preco)
//delete produto.preco // se quiser tirar o atributo do objeto
console.log(produto)

produto.preco = null // sem preço
console.log(!!produto.preco)
console.log(produto)