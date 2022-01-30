import unicodedata
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

def read_in_chunks(file_object, chunk_size=1024):
    """Lazy function (generator) to read a file piece by piece.
    Default chunk size: 1k."""
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data


with open('dictionary.txt') as f:
    for line in f.readlines():
        line = strip_accents(u''+line+'')
        if len(str(line)) == 6:
            with open('dictionary_5_letters_words.txt', 'a') as f_2:
                f_2.write(line)

