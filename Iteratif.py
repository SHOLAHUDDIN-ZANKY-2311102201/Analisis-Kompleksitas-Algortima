def reverse_word(word):
    # Base case: kata kosong atau satu huruf
    if len(word) <= 1:
        return word

    # Rekursif: ambil huruf pertama dan panggil fungsi untuk sisa kata
    return reverse_word(word[1:]) + word[0]

def split_first_word(sentence):
    # Base case: tidak ada spasi
    words = sentence.split(' ', 1)
    if len(words) > 1:
        return words[0], words[1]
    return words[0], ""

def reverse_words_and_order(sentence):
    # Base case: kalimat kosong
    if len(sentence) == 0:
        return ""

    # Base case: hanya satu kata
    if ' ' not in sentence:
        return reverse_word(sentence)

    # Rekursif:
    # 1. Ambil kata pertama dan sisa kalimat
    first_word, remaining = split_first_word(sentence)

    # 2. Proses sisa kalimat dulu (untuk membalik urutan)
    # lalu tambahkan kata pertama yang sudah dibalik
    if remaining == "":
        return reverse_word(first_word)
    return reverse_words_and_order(remaining) + " " + reverse_word(first_word)

def main():
    print("Program Pembalik Kata dan Urutan Kata dalam Paragraf")
    print("=================================================")

    print("Masukkan paragraf (ketik 'akhir' untuk mengakhiri):")
    paragraphs = []

    while True:
        line = input()
        if line == "akhir":
            break
        paragraphs.append(line)

    all_text = "\n".join(paragraphs)

    if all_text:
        result = reverse_words_and_order(all_text)
        print("\nHasil pembalikan kata dan urutan:")
        print(result)
    else:
        print("Tidak ada input yang dimasukkan.")

if __name__ == "__main__":
    main()
