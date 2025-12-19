# Anki Deck Generator
(Based on code: https://github.com/matt-hendrick/Anki-Deck-Creator)

This is a repo that generates language Anki decks from publicly available source(s) that provide audio and/or visual in addition to the English and other language text.

Currently, the repo contains script (generate_goethe_verlag_deck.py) that can generate Anki decks for 50 languages using the content from [Goethe-Verlag.com](https://www.goethe-verlag.com/book2/_VOCAB/).
Currently, the repo contains script (generate_goethe_verlag_deck2.py) that can generate Anki decks for 50 languages using the content from [Goethe-Verlag.com](https://www.goethe-verlag.com/book2/).

To run the script and generate a deck, you must specify a 2-character language name. Available languages:

'Adyghe': 'AD', 'Afrikaans': 'AF', 'Amharic': 'AM', 'Arabic': 'AR', 'Belarusian': 'BE', 'Bulgarian': 'BG', 'Bengali': 'BN', 'Bosnian': 'BS', 'Catalan': 'CA', 'Czech': 'CS', 'Danish': 'DA', 'German': 'DE', 'Greek': 'EL', 'English UK': 'EN', 'Esperanto': 'EO', 'Spanish': 'ES', 'Estonian': 'ET', 'Persian': 'FA', 'Finnish': 'FI', 'French': 'FR', 'Hebrew': 'HE', 'Hindi': 'HI', 'Croatian': 'HR', 'Hungarian': 'HU', 'Armenian': 'HY', 'Indonesian': 'ID', 'Italian': 'IT', 'Japanese': 'JA', 'Georgian': 'KA', 'Kazakh': 'KK', 'Kannada': 'KN', 'Korean': 'KO', 'Lithuanian': 'LT', 'Latvian': 'LV', 'Macedonian': 'MK', 'Marathi': 'MR', 'Dutch': 'NL', 'Norwegian - Nynorsk': 'NN', 'Norwegian': 'NO', 'Punjabi': 'PA', 'Polish': 'PL', 'Portuguese PT': 'PT', 'Portuguese BR': 'PX', 'Romanian': 'RO', 'Russian': 'RU', 'Slovak': 'SK', 'Slovene': 'SL', 'Albanian': 'SQ', 'Serbian': 'SR', 'Swedish': 'SV', 'Tamil': 'TA', 'Telugu': 'TE', 'Thai': 'TH', 'Tigrinya': 'TI', 'Turkish': 'TR', 'Ukrainian': 'UK', 'Urdu': 'UR', 'Vietnamese': 'VI', 'Chinese': 'ZH'

An example command is:

    python generate_goethe_verlag_deck.py -ls RU -ll DE
		
		python generate_goethe_verlag_deck2.py -ls RU -ll DE
		
Display help for commands:
		python generate_goethe_verlag_deck.py -h
		
		python generate_goethe_verlag_deck2.py -h
