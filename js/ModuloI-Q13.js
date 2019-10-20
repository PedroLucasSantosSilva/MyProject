const obj = {
    temp: 0,
    get temperatura() { return this.temp++ },
    set temperatura(temperatura) {
        if(temperatura > this.temp) {
            this.temp = temperatura            
        }
    }
}