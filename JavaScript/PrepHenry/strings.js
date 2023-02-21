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
console.log(challenge.startsWith(3))
console.log(challenge.startsWith('30'))
console.log(challenge.endsWith('t'))
console.log(challenge.endsWith('Javascript'))
console.log(challenge.match('a'))
let word = 'Javascript'
console.log('Word:', word, 'Concatenated with phrase', challenge.concat(word))
console.log('Using repeat()', challenge.repeat(2))

console.log('The quote: \'There is no exercise better for the heart than reaching down and lifting people up\' John Holmes teaches us to help one another')
let numberstr = '10'
let strtonumber = parseInt(numberstr)
console.log(typeof(strtonumber))
let list2 = 'Python, Argon'
console.log(list2.search('on'))

let randomnumber = Math.random(50,100)
let random2= randomnumber * 100
console.log(random2)
console.log('1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27')
let new_phrase = 'You cannot end a sentence with because because because is a conjunction'
console.log(new_phrase.indexOf('because'))
console.log(new_phrase.substr(31, 7))
let phrasetocount = 'love is the best thing in this world. Some found their love and some are still looking for their love'
let matches = phrasetocount.match(pattern)
console.log(matches)



