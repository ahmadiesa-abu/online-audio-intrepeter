# Text [input from user] then to translated Audio

In this small script `run.py` the user will be asked to provide language
[source, destination]

* source: language of the user-input
* destination: language to translate the entered text and will be played

```
python run.py --help
Usage: run.py [OPTIONS]

  Main function to start the inifinte loop for user-input. The function
  expects an input if none [empty string] the function will exit other text
  will be translated to destination language and played.

Options:
  --src [Afrikaans|Albanian|Amharic|Arabic|Armenian|Azerbaijani|Basque|Belarusian|Bengali|Bosnian|Bulgarian|Catalan|Cebuano|Chinese|Corsican|Croatian|Czech|Danish|Dutch|English|Esperanto|Estonian|Finnish|French|Frisian|Galician|Georgian|German|Greek|Gujarati|Haitian Creole|Hausa|Hawaiian|Hebrew|Hindi|Hmong|Hungarian|Icelandic|Igbo|Indonesian|Irish|Italian|Japanese|Javanese|Kannada|Kazakh|Khmer|Kinyarwanda|Korean|Kurdish|Kyrgyz|Lao|Latin|Latvian|Lithuanian|Luxembourgish|Macedonian|Malagasy|Malay|Malayalam|Maltese|Maori|Marathi|Mongolian|Myanmar|Nepali|Norwegian|Nyanja|Odia|Pashto|Persian|Polish|Portuguese|Punjabi|Romanian|Russian|Samoan|Scots Gaelic|Serbian|Sesotho|Shona|Sindhi|Sinhala|Slovak|Slovenian|Somali|Spanish|Sundanese|Swahili|Swedish|Tagalog|Tajik|Tamil|Tatar|Telugu|Thai|Turkish|Turkmen|Ukrainian|Urdu|Uyghur|Uzbek|Vietnamese|Welsh|Xhosa|Yiddish|Yoruba|Zulu]
                                  Source language for user-input.
  --dst [Afrikaans|Albanian|Amharic|Arabic|Armenian|Azerbaijani|Basque|Belarusian|Bengali|Bosnian|Bulgarian|Catalan|Cebuano|Chinese|Corsican|Croatian|Czech|Danish|Dutch|English|Esperanto|Estonian|Finnish|French|Frisian|Galician|Georgian|German|Greek|Gujarati|Haitian Creole|Hausa|Hawaiian|Hebrew|Hindi|Hmong|Hungarian|Icelandic|Igbo|Indonesian|Irish|Italian|Japanese|Javanese|Kannada|Kazakh|Khmer|Kinyarwanda|Korean|Kurdish|Kyrgyz|Lao|Latin|Latvian|Lithuanian|Luxembourgish|Macedonian|Malagasy|Malay|Malayalam|Maltese|Maori|Marathi|Mongolian|Myanmar|Nepali|Norwegian|Nyanja|Odia|Pashto|Persian|Polish|Portuguese|Punjabi|Romanian|Russian|Samoan|Scots Gaelic|Serbian|Sesotho|Shona|Sindhi|Sinhala|Slovak|Slovenian|Somali|Spanish|Sundanese|Swahili|Swedish|Tagalog|Tajik|Tamil|Tatar|Telugu|Thai|Turkish|Turkmen|Ukrainian|Urdu|Uyghur|Uzbek|Vietnamese|Welsh|Xhosa|Yiddish|Yoruba|Zulu]
                                  Destination language to translate input then
                                  play it.
  --help                          Show this message and exit.
```
