function try_catch() {
    try {
        if (Math.random() > 0.3)
            throw new Error('Erro')
            return
    }catch(e){
        console.log(e.message)
    }finally{
        console.log('Será executada sem exceção')
    }
}