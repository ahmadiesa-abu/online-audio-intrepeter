import os

import click
import playsound
import speech_recognition as sr

from gtts import gTTS
from googletrans import Translator


languages = [
    'Afrikaans', 'Albanian', 'Amharic', 'Arabic', 'Armenian', 'Azerbaijani',
    'Basque', 'Belarusian', 'Bengali', 'Bosnian', 'Bulgarian', 'Catalan',
    'Cebuano', 'Chinese', 'Corsican','Croatian', 'Czech', 'Danish', 'Dutch',
    'English', 'Esperanto', 'Estonian', 'Finnish', 'French', 'Frisian',
    'Galician', 'Georgian', 'German', 'Greek', 'Gujarati', 'Haitian Creole',
    'Hausa', 'Hawaiian', 'Hebrew', 'Hindi', 'Hmong', 'Hungarian',
    'Icelandic', 'Igbo', 'Indonesian', 'Irish', 'Italian', 'Japanese',
    'Javanese', 'Kannada', 'Kazakh', 'Khmer', 'Kinyarwanda', 'Korean',
    'Kurdish', 'Kyrgyz', 'Lao', 'Latin', 'Latvian', 'Lithuanian',
    'Luxembourgish', 'Macedonian', 'Malagasy', 'Malay', 'Malayalam', 'Maltese',
    'Maori', 'Marathi', 'Mongolian', 'Myanmar', 'Nepali', 'Norwegian',
    'Nyanja', 'Odia', 'Pashto', 'Persian', 'Polish', 'Portuguese', 'Punjabi',
    'Romanian', 'Russian', 'Samoan', 'Scots Gaelic', 'Serbian', 'Sesotho',
    'Shona', 'Sindhi', 'Sinhala', 'Slovak', 'Slovenian', 'Somali', 'Spanish',
    'Sundanese', 'Swahili', 'Swedish', 'Tagalog', 'Tajik', 'Tamil', 'Tatar',
    'Telugu', 'Thai', 'Turkish', 'Turkmen', 'Ukrainian', 'Urdu', 'Uyghur',
    'Uzbek', 'Vietnamese', 'Welsh', 'Xhosa', 'Yiddish', 'Yoruba', 'Zulu']
languages_mapping = {
    "Afrikaans": "af",
    "Albanian": "sq",
    "Amharic": "am",
    "Arabic": "ar",
    "Armenian": "hy",
    "Azerbaijani": "az",
    "Basque": "eu",
    "Belarusian": "be",
    "Bengali": "bn",
    "Bosnian": "bs",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Cebuano": "ceb (ISO-639-2)",
    "Chinese": "zh-CN",
    "Corsican": "co",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Esperanto": "eo",
    "Estonian": "et",
    "Finnish": "fi",
    "French": "fr",
    "Frisian": "fy",
    "Galician": "gl",
    "Georgian": "ka",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Haitian Creole": "ht",
    "Hausa": "ha",
    "Hawaiian": "haw (ISO-639-2)",
    "Hebrew": "iw",
    "Hindi": "hi",
    "Hmong": "hmn (ISO-639-2)",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Igbo": "ig",
    "Indonesian": "id",
    "Irish": "ga",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jv",
    "Kannada": "kn",
    "Kazakh": "kk",
    "Khmer": "km",
    "Kinyarwanda": "rw",
    "Korean": "ko",
    "Kurdish": "ku",
    "Kyrgyz": "ky",
    "Lao": "lo",
    "Latin": "la",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Luxembourgish": "lb",
    "Macedonian": "mk",
    "Malagasy": "mg",
    "Malay": "ms",
    "Malayalam": "ml",
    "Maltese": "mt",
    "Maori": "mi",
    "Marathi": "mr",
    "Mongolian": "mn",
    "Myanmar": "my",
    "Nepali": "ne",
    "Norwegian": "no",
    "Nyanja": "ny",
    "Odia": "or",
    "Pashto": "ps",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Samoan": "sm",
    "Scots Gaelic": "gd",
    "Serbian": "sr",
    "Sesotho": "st",
    "Shona": "sn",
    "Sindhi": "sd",
    "Sinhala": "si",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Somali": "so",
    "Spanish": "es",
    "Sundanese": "su",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tagalog": "tl",
    "Tajik": "tg",
    "Tamil": "ta",
    "Tatar": "tt",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Turkmen": "tk",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Uyghur": "ug",
    "Uzbek": "uz",
    "Vietnamese": "vi",
    "Welsh": "cy",
    "Xhosa": "xh",
    "Yiddish": "yi",
    "Yoruba": "yo",
    "Zulu": "zu"}
translator = None


def get_lang_mapping(lang):
    mapping =  {k.lower(): v for k, v in languages_mapping.items()}
    if lang.lower() in mapping:
        return mapping.get(lang.lower())
    return None


def translate_text(input, src, dst):
    global translator
    return translator.translate(input, src=src, dest=dst)


@click.command()
@click.option('--src',  prompt='Source Language', default='english',
              type=click.Choice(languages, case_sensitive=False),
              help='Source language for user audio-input.')
@click.option('--dst', prompt='Destination Language',
              type=click.Choice(languages, case_sensitive=False),
              help='Destination language to translate input then print it.')
@click.option('--phrase-time-limit', prompt='Phrase Time Limit for audio-input',
              default=5,
              help='Maximum time for the audio recorder.')
def main(src, dst, phrase_time_limit):
    """Main function to start the infinite loop for user audio-input.
    The function expects an audio from microphone it will record up-to
    phrase time limit in seconds if there are frames coming from microphone,
    then recognize the audio and translate then print it to screen.
    """
    global translator
    src_lang_code = get_lang_mapping(src)
    dst_lang_code = get_lang_mapping(dst)

    click.echo(f'User Input Language: {src} with code {src_lang_code}')
    click.echo(f'Translate to Language: {dst} with code {dst_lang_code}')
    translator = Translator()

    while True:
        try:
            rec = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                rec.pause_threshold = 1
                audio = rec.listen(source, phrase_time_limit=phrase_time_limit)
            input_to_translate = rec.recognize_google(audio,
                                                      language=src_lang_code)
            translated_input = translate_text(input_to_translate,
                                              src_lang_code,
                                              dst_lang_code)
            click.echo(f'Translated Audio Input {translated_input.text}')
        except:
            pass


if __name__ == '__main__':
    main()
