function pessoa() {
    this.idade = 0

    const self = this
    setInterval(function(){       // a cada 1000 milissegundo essa função anonima do setInterval vai ser disparada
        self.idade++
        console.log(self.idade)
    }/*.bind(this)*/, 1000)
}

new pessoa