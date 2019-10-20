let array = [5, 6, 10, 4, 3, 7, 1]
let total = array.reduce(function(total, numero){
    total += numero
    return total
}, 0);
media = total / array.length
console.log('média aritmética:' + media.toFixed(2))

const menoresMedia = array.filter(function(array){
    return array > media
})

console.log(`valores maiores que a média:${menoresMedia}`)