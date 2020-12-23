# word-password-generator

![xkcd password strength](https://imgs.xkcd.com/comics/password_strength.png)

My attempt to make password generating software, that would be using given words (thus making it multilangual).  
There are a lot of programs of that type, but all I found was using english dictionary and I wanted womething that would make passwords from Polish words.  
  
## how to use it
currently you can use program only by CLI with syntax given below
```
python ./main.py NO_OF_WORDS WORDS_SEPARATOR CAPITALIZE_WORDS RANDOM_NUMBERS_TO_PUT
```
- NO_OF_WORDS <- you can specify how many words do you want your password to have  
- WORDS_SEPARATOR <- specify with what character do you want wards to me separated (dash is most common I think). Put it in quotes to avoid errors  
- CAPITALIZE_WORDS <- you can make your password words to be capitalized (first letters big). Put only "True" or "False" there (quotes arent necessary)  
- RANDOM_NUMBERS_TO_PUT <- program can append random digits after every word (and before separator). You can specify how many digits do you want (you can specify more digits than words.  
  
**Example**:
```
python ./main.py 5 '-' True 17
```
using given dictionary with randomly generated words (see my simple-apps-for-testing-purposes repository) could make something below:
```
Ebolohi197494-Ikyd8247-Budo93-Aciwas95-Teti061
```

### TODO
- let user specify the dictionary
- tests
- GUI with chriskiehl/Gooey 
- option do specify max word length
