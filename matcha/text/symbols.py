""" from https://github.com/keithito/tacotron

Defines the set of symbols used in text input to the model.
"""
_pad = "_"
_punctuation = ';:,.!?¡¿—…"«»“” ~'
_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZÂÄÉÊÈÎÏÔÖÙÛÇŒÑabcdefghijklmnopqrstuvwxyzâäéêèîïôöùûçœñ"
_letters_ipa = (
    "ɑãẽõɐɒæɓʙβɔɕçɗɖðʤəɘɚɛɜɝɞɟʄɡɠɢʛɦɧħɥʜɨɪʝɭɬɫɮʟɱɯɰŋɳɲɴøɵɸθœɶʘɹɺɾɻʀʁɽʂʃʈʧʉʊʋⱱʌɣɤʍχʎʏʑʐʒʔʡʕʢǀǁǂǃˈˌːˑʼʴʰʱʲʷˠˤ˞↓↑→↗↘ᵻ ̃"
)

#æɑãɛəeẽiɪoøɔœõuʊʌybdðdfghɥjklmnŋɲpʁɹsʃttθvwzʒ
# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters) + list(_letters_ipa)

# Remove any duplicate
symbols = list(dict.fromkeys(symbols))

# Special symbol ids
SPACE_ID = symbols.index(" ")
