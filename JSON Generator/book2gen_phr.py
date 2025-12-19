import os
import json
import re
from collections import defaultdict

def extract_lang_code(filename):
    """Извлекает код языка из имени файла"""
    lang_part = filename.replace("_Book2_RU_", "")
    return lang_part[:2]

def process_files_optimized(folder_path):
    """Обрабатывает файлы в оптимизированной структуре {индекс: {язык: данные}}"""
    
    data = defaultdict(dict)
    index_pattern = re.compile(r'(\d+|[x]\d+)')
    files = [f for f in os.listdir(folder_path) 
             if f.startswith("_Book2_RU_") and f.endswith("_phr.txt")]
    
    print(f"Найдено файлов: {len(files)}")
    
    for filename in files:
        lang_code = extract_lang_code(filename)
        filepath = os.path.join(folder_path, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()[6:]
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                columns = line.split('\t')
                if len(columns) < 14:
                    continue
                
                word = columns[3].strip()
                pronunciation = columns[4].strip()
                index_str = columns[13].strip()
                
                match = index_pattern.search(index_str)
                index_key = match.group(1) if match else index_str
                
                data[index_key][lang_code] = {
                    "w": word,
                    "p": pronunciation
                }
                
        except Exception as e:
            print(f"Ошибка в {filename}: {e}")
    
    return dict(data)

def save_readable_json(data, output_filename="_book2_note_p.json"):
    """Сохраняет JSON с читаемой структурой и переносами строк"""
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write('{\n')  # Открывающая скобка
        
        indices = list(data.keys())
        
        for i, index in enumerate(indices):
            # Записываем индекс и открывающую скобку для языков
            f.write(f'  "{index}": {{\n')
            
            langs = list(data[index].keys())
            
            for j, lang in enumerate(langs):
                entry = data[index][lang]
                # Форматируем запись с экранированием кавычек
                word_escaped = json.dumps(entry['w'], ensure_ascii=False)[1:-1]
                pron_escaped = json.dumps(entry['p'], ensure_ascii=False)[1:-1]
                
                # Запись в компактном формате, но с переносом
                entry_str = f'    "{lang}": {{"w":"{word_escaped}","p":"{pron_escaped}"}}'
                
                # Добавляем запятую, если не последний язык
                if j < len(langs) - 1:
                    entry_str += ','
                
                f.write(entry_str + '\n')
            
            # Закрывающая скобка для этого индекса
            f.write('  }')
            
            # Добавляем запятую, если не последний индекс
            if i < len(indices) - 1:
                f.write(',')
            
            f.write('\n')  # Перенос строки после каждой записи
        
        f.write('}\n')  # Закрывающая скобка
    
    # Анализ размера
    size = os.path.getsize(output_filename)
    print(f"Сохранено в: {output_filename}")
    print(f"Размер файла: {size / 1024:.1f} KB")
    print(f"Количество индексов: {len(data)}")

def save_compact_but_readable(data, output_filename="phr_compact.json"):
    """Альтернатива: компактный но читаемый JSON"""
    
    class ReadableJSONEncoder(json.JSONEncoder):
        def encode(self, obj):
            # Кастомный энкодер для красивых переносов
            if isinstance(obj, dict):
                items = []
                for key, value in obj.items():
                    if isinstance(value, dict) and all(
                        isinstance(v, dict) and 'w' in v and 'p' in v 
                        for v in value.values()
                    ):
                        # Для вложенных словарей языков делаем компактно
                        lang_items = []
                        for lang, lang_data in value.items():
                            word_escaped = json.dumps(lang_data['w'], ensure_ascii=False)
                            pron_escaped = json.dumps(lang_data['p'], ensure_ascii=False)
                            lang_items.append(f'"{lang}":{{"w":{word_escaped},"p":{pron_escaped}}}')
                        
                        items.append(f'"{key}":{{{",".join(lang_items)}}}')
                    else:
                        items.append(f'"{key}":{json.dumps(value, ensure_ascii=False)}')
                
                return '{\n  ' + ',\n  '.join(items) + '\n}'
            return super().encode(obj)
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, cls=ReadableJSONEncoder, ensure_ascii=False)
    
    size = os.path.getsize(output_filename)
    print(f"\nАльтернативный файл: {output_filename}")
    print(f"Размер: {size / 1024:.1f} KB")

def main():
    """Основная функция"""
    print("="*50)
    print("СОЗДАНИЕ ЧИТАЕМОГО JSON ДЛЯ ANKI")
    print("="*50)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data = process_files_optimized(current_dir)
    
    if data:
        # 1. Полностью читаемая версия (лучше для отладки)
        save_readable_json(data, "_book2_note_p.json")
        
        # 2. Более компактная но все еще читаемая версия
        save_compact_but_readable(data, "phr_compact.json")
        
        # 3. Минимальная версия для сравнения
        with open("phr_minimal.json", 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, separators=(',', ':'))
        
        # Сравнение размеров
        print("\n" + "="*50)
        print("СРАВНЕНИЕ ФАЙЛОВ:")
        print("="*50)
        
        for filename in ["_book2_note_p.json", "phr_compact.json", "phr_minimal.json"]:
            if os.path.exists(filename):
                size = os.path.getsize(filename)
                print(f"{filename}: {size / 1024:.1f} KB ({size:,} bytes)")
        
        print("\n" + "="*50)
        print("РЕКОМЕНДАЦИЯ ДЛЯ ANKI:")
        print("="*50)
        print("""
1. Для Anki используйте 'phr_compact.json' - он читаемый и не слишком большой
2. Пример структуры файла:
   {
     "x01": {"AR":{"w":"مشاعر","p":"elmashaaeaer"},"DE":{"w":"Gefühle","p":"gefühlle"}},
     "x02": {"AR":{"w":"كلمة","p":"kalima"},"DE":{"w":"Wort","p":"vort"}}
   }
3. В Anki загружайте через:
   import json
   with open('phr_compact.json', 'r', encoding='utf-8') as f:
       data = json.load(f)
   
   # Доступ
   if 'x01' in data and 'AR' in data['x01']:
       word = data['x01']['AR']['w']
""")

if __name__ == "__main__":
    main()