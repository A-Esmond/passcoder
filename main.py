def Vowel(c):
  if c in ['a','e','i','o','u']:
    return True
  else:
    return False

def Encrypter(c):
  match c:
    case 'a':
      return '1'
    case 'e':
      return '2'
    case 'i':
      return '3'
    case 'o':
      return '4'
    case 'u':
      return '5'

def countVowels(plaintext):
  vowelCount = 0
  
  for i in range(len(plaintext)):
    if Vowel(plaintext[i]):
      vowelCount += 1
  return vowelCount

def Passcoder(Plaintext):
  
  Cyphertext = []
  Plaintext = Plaintext.lower()
  
  for i in range(len(Plaintext)):
    if Vowel(Plaintext[i]):
      Cyphertext.append(Encrypter(Plaintext[i]))
    else:
      continue  
  
  Cyphertext = "".join(Cyphertext)
  print(Cyphertext)

Passcoder("aeiou")
Passcoder("computer science")
    