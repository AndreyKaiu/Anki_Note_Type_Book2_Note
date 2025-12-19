import time
import requests
import genanki
import os.path
import random
from argparse import ArgumentParser
from urllib.parse import urljoin, urlparse

from get_soup import get_soup
from remove_prefix import remove_prefix
from anki_card_model2 import anki_card_model_Ph

# Dictionary mapping Goethe Verlag language names to the format used in their URLs
LANGUAGE_MAPPING = {'Adyghe': 'AD', 'Afrikaans': 'AF', 'Amharic': 'AM', 'Arabic': 'AR', 'Belarusian': 'BE', 'Bulgarian': 'BG', 'Bengali': 'BN', 'Bosnian': 'BS', 'Catalan': 'CA', 'Czech': 'CS', 'Danish': 'DA', 'German': 'DE', 'Greek': 'EL', 'English UK': 'EN', 'Esperanto': 'EO', 'Spanish': 'ES', 'Estonian': 'ET', 'Persian': 'FA', 'Finnish': 'FI', 'French': 'FR', 'Hebrew': 'HE', 'Hindi': 'HI', 'Croatian': 'HR', 'Hungarian': 'HU', 'Armenian': 'HY', 'Indonesian': 'ID', 'Italian': 'IT', 'Japanese': 'JA', 'Georgian': 'KA',
                    'Kazakh': 'KK', 'Kannada': 'KN', 'Korean': 'KO', 'Lithuanian': 'LT', 'Latvian': 'LV', 'Macedonian': 'MK', 'Marathi': 'MR', 'Dutch': 'NL', 'Norwegian - Nynorsk': 'NN', 'Norwegian': 'NO', 'Punjabi': 'PA', 'Polish': 'PL', 'Portuguese PT': 'PT', 'Portuguese BR': 'PX', 'Romanian': 'RO', 'Russian': 'RU', 'Slovak': 'SK', 'Slovene': 'SL', 'Albanian': 'SQ', 'Serbian': 'SR', 'Swedish': 'SV', 'Tamil': 'TA', 'Telugu': 'TE', 'Thai': 'TH', 'Tigrinya': 'TI', 'Turkish': 'TR', 'Ukrainian': 'UK', 'Urdu': 'UR', 'Vietnamese': 'VI', 'Chinese': 'ZH'}
SITE_ROOT = "https://www.goethe-verlag.com/"


    
def str4_id_number(n: int) -> str:    
    if n < 10:
        retN = f"000{n}"
    elif n < 100:
        retN = f"00{n}"
    elif n < 1000:
        retN = f"0{n}"
    else:
        retN = f"{n}"
    return retN
    
def audio_base_name(url: str) -> str:
    """Returns the name of the audio file without extension"""
    filename = os.path.basename(urlparse(url).path)  # example: "0001.mp3"
    base, _ = os.path.splitext(filename)             # ("0001", ".mp3")
    return base    

def generate_goethe_verlag_deck(args):

    # set deck/file names to specified values or fallback to defaults
    deck_name = args.deckname or f"Book2_{args.lspeak}_{args.llearn}_phr"
    file_name = deck_name + '.apkg'
    if args.filename is not None and not args.filename.endswith(".apkg"):
        file_name = args.filename + ".apkg"

    new_deck = genanki.Deck(
        random.randrange(1 << 30, 1 << 31),
        deck_name)

    list_of_media_files = []

    
    # iterates through each category of phrases
    # for page_number in range(3, ???):
    for page_number in range(3, 103):
        time.sleep(random.randint(3, 5)) # abide by goethe-verlag robots.txt crawl delay
       
        if page_number < 10:
            page_numberStr = f"00{page_number}"
        elif page_number < 100:
            page_numberStr = f"0{page_number}"
        else:
            page_numberStr = f"{page_number}"
            
        # https://www.goethe-verlag.com/book2/EN/ENAR/ENAR003.HTM
        page_url = f"{SITE_ROOT}book2/{args.lspeak}/{args.lspeak}{args.llearn}/{args.lspeak}{args.llearn}{page_numberStr}.HTM"
                
        print("page_url=", page_url)

        # check page and throw error if page returns anything but 200
        page_status = requests.get(page_url).status_code
        if page_status != 200:
            raise Exception(
                f"HTTP error for {page_url}. Page status = {page_status}")
        
        
        ID_number = str4_id_number(2+(page_number-3)*20)
        
        soup = get_soup(page_url)
        
        voc = []
        for i in range(20):
            voc.append({
                'Speak': '',
                'Learn': '', 
                'Learn_Note': '',
                'file_audio': '',
                'Image': ''
            })
        
        # find IMG <img class="phrasebook-img" src="/assets/images/cms/phrasebook/lesson/1.webp">
        raw_img_src = soup.find("img", class_="phrasebook-img").get("src")
        img_url = urljoin(page_url, raw_img_src)
        img_filename = os.path.basename(urlparse(img_url).path)  # ex: "1628.webp"
        # image_file_name = f"book2_phr_N{ID_number}_{img_filename}"
        img_ext = os.path.splitext(img_url)[1]  # ".webp"
        image_file_name = f"book2_phr_N{ID_number}{img_ext}"
        anki_formatted_image = f'<img src="{image_file_name}">'
        
        if not os.path.isfile(image_file_name):
            time.sleep(random.uniform(0.1, 0.2))
            doc = requests.get(img_url)
            with open(image_file_name, 'wb') as f:
                f.write(doc.content)
        # add to list of media files to attach to anki package
        list_of_media_files.append(image_file_name)
        
        
        speak_learn = f"{args.lspeak}->{args.llearn}"
        
        voc[1]['Image'] = anki_formatted_image
        
        n = 1
        for findEl in soup.find_all("span", class_="Stil36"):
            if n == 1:
                voc[0]['Speak'] = findEl.get_text(strip=True)
            if n == 2:
                voc[1]['Speak'] = findEl.get_text(strip=True)
            n += 1
        
        n = 1
        for findEl in soup.find_all("span", class_="Stil46"):
            if n == 1:
                voc[0]['Learn'] = findEl.get_text(strip=True)
            if n == 2:
                voc[0]['Learn_Note'] = findEl.get_text(strip=True)
            if n == 3:
                voc[1]['Learn'] = findEl.get_text(strip=True)
            if n == 4:
                voc[1]['Learn_Note'] = findEl.get_text(strip=True)
            n += 1

        n = 0
        for findEl in soup.find_all("div", class_="Stil35"):
            if( n <= 17):
                voc[n+2]['Speak'] = findEl.get_text(strip=True)
            n += 1
            
        n = 0
        for findEl in soup.find_all("div", class_="Stil45"):
            if( n <= 17):
                Learn = ""
                Learn_Note = ""
                nn = 1
                iddiv = f"hn_{n+1}"
                for findEl2 in findEl.find("div", id=iddiv).find_all("a"):
                    if nn == 1:
                        Learn = findEl2.get_text(strip=True)
                    else:
                        Learn_Note = findEl2.get_text(strip=True)
                    nn += 1
                voc[n+2]['Learn'] = Learn
                voc[n+2]['Learn_Note'] = Learn_Note
            n += 1

        n = 0
        for findEl in soup.find_all("source"):
            if( n <= 19):
                voc[n]['file_audio'] = findEl.get("src")
            n += 1
            
        for i in range(20):
            raw_audio_src = voc[i]['file_audio']
            audio_url = urljoin(page_url, raw_audio_src)
            audio_base_ID_number = audio_base_name(audio_url)  # ← например "0001" или "ABCD"
            audio_ext = os.path.splitext(audio_url)[1]  # ".mp3"
            audio_file_name_Speak = f"book2_phr_N{audio_base_ID_number}_{args.lspeak}{audio_ext}"
            audio_file_name = f"book2_phr_N{audio_base_ID_number}_{args.llearn}{audio_ext}"
            anki_formatted_audio = f"[sound:{audio_file_name}]" 
            fileName_Audio_Learn = f"{audio_file_name}"             
            fileName_Audio_Speak = f"{audio_file_name_Speak}"  
            anki_formatted_audio_Speak = f"[sound:{audio_file_name_Speak}]"
            
            if not args.nosound:
                if not os.path.isfile(audio_file_name):
                    time.sleep(random.uniform(0.5, 0.6))
                    doc = requests.get(audio_url)
                    with open(audio_file_name, 'wb') as f:
                        f.write(doc.content)
                    # try not to clobber the server by mass downloading a bunch of files
                    # time.sleep(random.randint(1, 2))
                # add to list of media files to attach to anki package
                list_of_media_files.append(audio_file_name)
            
            
            # create card and add to deck
            new_note = genanki.Note(
                anki_card_model_Ph,
                [
                    str(voc[i]['Learn']),
                    str(voc[i]['Learn_Note']),
                    str(voc[i]['Speak']),
                    "",
                    str(anki_formatted_audio),
                    str(fileName_Audio_Learn),
                    str(anki_formatted_audio_Speak),
                    str(fileName_Audio_Speak),
                    str(voc[i]['Image']),
                    "",
                    str(audio_base_ID_number),
                    str(page_number-2),
                    str(speak_learn)
                ]
            )
            new_deck.add_note(new_note)

            if args.verbosity is not None:
                print(new_note)
                print("\n")
                print(f"{len(new_deck.notes)} cards have been added to the deck.")
            
            
            

    if args.verbosity is not None:
        print(f"Finished deck contains {len(new_deck.notes)} cards.")

    new_package = genanki.Package(new_deck)
    new_package.media_files = list_of_media_files
    new_package.write_to_file(file_name)

    return new_deck


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Scrape Goethe Verlag language learning resources to generate an Anki deck with audio/video")
    parser.add_argument("-ls", "--lspeak",
                        help="Enter the 2-character language code of the language you speak (example: 'EM' for the US)")
    parser.add_argument("-ll", "--llearn",
                        help="Enter the 2-character code of the language you are learning (example: 'DE' for the Germany)")
    parser.add_argument("-d", "--deckname",
                        help="Enter the name of the new deck'")
    parser.add_argument("-f", "--filename",
                        help="Enter the name of the new .apkg file'")
    parser.add_argument("-v", "--verbosity",
                        action="store_true",
                        help="Add this flag to print out each card as the scraper progresses")
    parser.add_argument("-ns", "--nosound",   
                        action="store_true",    
                        help="Do not save the sound file")
    
    

    args = parser.parse_args()

    if args.lspeak is None or args.llearn is None:
        raise Exception("You must provide the language as an argument (example: -ls EM -ll DE)")

    args.llearn = args.llearn.upper()
    args.lspeak = args.lspeak.upper()

    generate_goethe_verlag_deck(args)
