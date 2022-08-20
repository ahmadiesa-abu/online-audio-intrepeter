# Audio [input from user] then to translated Text

In this small script `run.py` the user will be asked to provide language
[source, destination]

* source: language of the user input-audio
* destination: language to translate the entered audio after recognition and will be printed to the screen

```
python run.py --help
Usage: run.py [OPTIONS]

  Main function to start the infinite loop for audio-input. The function
  expects an audio from microphone it will record up-to phrase time limit in
  seconds if there are frames coming from microphone, then recognize the audio
  and translate then print it to screen.

Options:
  --src [Afrikaans|Albanian|Amharic|Arabic|Armenian|Azerbaijani|Basque|Belarusian|Bengali|Bosnian|Bulgarian|Catalan|Cebuano|Chinese|Corsican|Croatian|Czech|Danish|Dutch|English|Esperanto|Estonian|Finnish|French|Frisian|Galician|Georgian|German|Greek|Gujarati|Haitian Creole|Hausa|Hawaiian|Hebrew|Hindi|Hmong|Hungarian|Icelandic|Igbo|Indonesian|Irish|Italian|Japanese|Javanese|Kannada|Kazakh|Khmer|Kinyarwanda|Korean|Kurdish|Kyrgyz|Lao|Latin|Latvian|Lithuanian|Luxembourgish|Macedonian|Malagasy|Malay|Malayalam|Maltese|Maori|Marathi|Mongolian|Myanmar|Nepali|Norwegian|Nyanja|Odia|Pashto|Persian|Polish|Portuguese|Punjabi|Romanian|Russian|Samoan|Scots Gaelic|Serbian|Sesotho|Shona|Sindhi|Sinhala|Slovak|Slovenian|Somali|Spanish|Sundanese|Swahili|Swedish|Tagalog|Tajik|Tamil|Tatar|Telugu|Thai|Turkish|Turkmen|Ukrainian|Urdu|Uyghur|Uzbek|Vietnamese|Welsh|Xhosa|Yiddish|Yoruba|Zulu]
                                  Source language for user audio-input.
  --dst [Afrikaans|Albanian|Amharic|Arabic|Armenian|Azerbaijani|Basque|Belarusian|Bengali|Bosnian|Bulgarian|Catalan|Cebuano|Chinese|Corsican|Croatian|Czech|Danish|Dutch|English|Esperanto|Estonian|Finnish|French|Frisian|Galician|Georgian|German|Greek|Gujarati|Haitian Creole|Hausa|Hawaiian|Hebrew|Hindi|Hmong|Hungarian|Icelandic|Igbo|Indonesian|Irish|Italian|Japanese|Javanese|Kannada|Kazakh|Khmer|Kinyarwanda|Korean|Kurdish|Kyrgyz|Lao|Latin|Latvian|Lithuanian|Luxembourgish|Macedonian|Malagasy|Malay|Malayalam|Maltese|Maori|Marathi|Mongolian|Myanmar|Nepali|Norwegian|Nyanja|Odia|Pashto|Persian|Polish|Portuguese|Punjabi|Romanian|Russian|Samoan|Scots Gaelic|Serbian|Sesotho|Shona|Sindhi|Sinhala|Slovak|Slovenian|Somali|Spanish|Sundanese|Swahili|Swedish|Tagalog|Tajik|Tamil|Tatar|Telugu|Thai|Turkish|Turkmen|Ukrainian|Urdu|Uyghur|Uzbek|Vietnamese|Welsh|Xhosa|Yiddish|Yoruba|Zulu]
                                  Destination language to translate input then
                                  print it.
  --phrase-time-limit INTEGER     Maximum time for the audio recorder.
  --help                          Show this message and exit.
```
