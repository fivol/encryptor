ENCRYPTOR PROJECT

NOVICHKOV BORIS
B05-924


Шифратор

1.1. Шифрование
./encryptor.py encode --cipher {caesar|vigenere} --key {<number>|<word>} [--input-file input.txt] [--output-file output.txt]
Зашифровать входное сообщение. 
Аргументы: 
* --cipher - тип шифра: caesar (Шифр Цезаря) или vigenere (Шифр Виженера). 
* --key - ключ шифра. Для шифра Цезаря - число, соответствующее сдвигу, для шифра Виженера - слово, которое задает сдвиги.
* --input-file (необязательный аргумент) - путь ко входному файлу с текстом. Если не указан, текст вводится с клавиатуры.
* --output-file (необязательный аргумент) - путь ко входному файлу с текстом. Если не указан, текст выводится в консоль.
Пример:
* ./encryptor.py encode --cipher caesar --key 23 --input-file text_files/file.txt --output-file text_files/output.txt

1.2. Дешифрование
./encryptor.py decode --cipher {caesar|vigenere} --key {<number>|<word>} [--input-file input.txt] [--output-file output.txt]
Расшифровать входное сообщение, зная шифр и ключ, с которым оно было зашифровано. 
Аргументы: 
* --cipher - тип шифра: caesar (Шифр Цезаря) или vigenere (Шифр Виженера). 
* --key - ключ шифра. Для шифра Цезаря - число, соответствующее сдвигу, для шифра Виженера - слово, которое задает сдвиги.
* --input-file (необязательный аргумент) - путь ко входному файлу с текстом. Если не указан, текст вводится с клавиатуры.
* --output-file (необязательный аргумент) - путь ко входному файлу с текстом. Если не указан, расшифрованное сообщение выводится в консоль.
Пример:
* ./encryptor.py decode --cipher caesar --key 23 --input-file text_files/output.txt --output-file text_files/decoded.txt

1.3. Взлом
Команды для обучения и взлома имеют следующий вид:
./encryptor.py train --text-file {input.txt} --model-file {model}
Проанализировать текст и построить языковую модель 
Аргументы:
* --text-file (необязательный аргумент) - путь ко входному файлу с текстом. Если не указан, текст вводится с клавиатуры.
* --model-file - путь к файлу модели, куда будет записана вся та статистика, которую вы собрали по тексту. Содержимое этого файла можно формировать руками, можно использовать представление json (и одноименный модуль питона), либо модуль pickle
Пример:
 * ./encryptor.py train --text-file text_files/shakespeare_sonnets.txt --model-file text_files/model.json

./encryptor.py hack [--input-file input.txt] [--output-file output.txt] --model-file {model}
Попытаться расшифровать текст. 
Аргументы:
* --input-file (необязательный аргумент) - путь ко входному файлу с текстом. Если не указан, текст вводится с клавиатуры.
* --output-file (необязательный аргумент) - путь ко входному файлу с текстом. Если не указан, расшифрованное сообщение выводится в консоль.
* --model-file - путь к файлу модели, которая будет использоваться.
Пример:
* ./encryptor.py hack --input-file text_files/output.txt --output-file text_files/hacked.txt --model-file text_files/model.json
