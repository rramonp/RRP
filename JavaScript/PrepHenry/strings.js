let challenge = '30 Days of Javascript'

console.log("STRING:", challenge)
console.log(`Total characters: ${challenge.length}`)
console.log(`Now in uppercase --> ${challenge.toUpperCase()}`)
console.log(`Now in lowercase --> ${challenge.toLowerCase()}`)
console.log('Slice first word with substring (0,2):', challenge.substring(0,2))
console.log('Slice the rest with substring(2):', challenge.substring(2))
console.log('Check if \'Days\' is included:', challenge.includes('Days')) 
console.log(challenge.split())
console.log(challenge.split(' '))

let companies = 'IBM, Microsoft, Apple, Huawei, Sony, Facebook, Google'
let companies2 = companies.split(', ')
console.log(companies2)

console.log("Replace Javascript with Python with .replace() ---> ", challenge.replace('Javascript', 'Python'))
console.log("Position 15 with .charAt()", challenge.charAt(15))
console.log("Code J with .charCodeAt()", challenge.charCodeAt('s'))
console.log("Find position of first \'a\' with .indexOf()", challenge.indexOf('a'))
console.log("Find position of last \'a\' with .lastIndexOf()", challenge.lastIndexOf('a'))

let sentence = 'You cannot end a sencence with because, because because is a conjunction'
console.log('SENTENCE: ', sentence)
console.log('Last position of \'because\' with lastIndexOf()', sentence.lastIndexOf('because'))
console.log('Using search() for first ocurrence of \'because\' ', sentence.search('because'))

let challenge_spaced = '        30 Days of Javascript  '
console.log(`[${challenge_spaced}] now trimmed with trim()--> [${challenge_spaced.trim()}]`)