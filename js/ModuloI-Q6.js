try{
    if (Math.random() > 0.5) throw new Error('Erro:' + e.message)
}catch(e){
    throw new Error('Erro:' + e.message)
}