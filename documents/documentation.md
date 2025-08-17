# Cognate Identification

You can enter a word like `cable`, select `English` as the language and the app will check if the word is a cognate or not and return this output:
```
{
  "lang": "ENGLISH",
  "match": {
    "word": "cable"
  },
  "message": "Cognate found.",
  "result_type": "COGNATE",
  "word": "cable"
}
```

The app can also check if a word is not a cognate. Such as the case of the word `doll`:
```
{
  "lang": "ENGLISH",
  "match": null,
  "message": "This is not a cognate.",
  "result_type": "NO_MATCH",
  "word": "doll"
}
```
Or, if a word is a false cognate or false friend, as in the case of `diversión`, here `Spanish` has been selected as the language. 

```
{
  "lang": "SPANISH",
  "match": null,
  "message": "This is a false cognate.",
  "result_type": "FALSE_FRIEND",
  "word": "diversión"
}
```

The API can be called without using a UI by using a GET request on Postman by using this link: http://localhost:5050/cognate-check?word=cable&lang=ENGLISH.
You would switch the word for the word you wish to search for and the language for either SPANISH or ENGLISH.

Also, you can go to http://127.0.0.1:5050 or http://192.168.1.24:5050 and input the word to get the same information for the word entered.