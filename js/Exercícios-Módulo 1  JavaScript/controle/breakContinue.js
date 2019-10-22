const nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for (x in nums) {
    if(x == 5) {
        break // está associado a for
    }
    console.log(`índice ${x} = ${nums[x]}`)
}

for (y in nums) {
    if(y == 5) {
        continue
    }
    console.log(`índice ${y} = ${nums[y]}`)
}

externo:
for(a in nums) {
    for(b in nums) {
        if(a == 2 && b == 3) break externo
        console.log(`Par = ${a},${b}`)
    }
}