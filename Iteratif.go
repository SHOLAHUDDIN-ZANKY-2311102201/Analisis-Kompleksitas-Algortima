def reverse_word(word):
    # Konversi string ke list karakter
    chars = list(word)

    # Iterasi untuk menukar karakter dari depan dan belakang
    for i in range(len(chars) // 2):
        chars[i], chars[len(chars)-1-i] = chars[len(chars)-1-i], chars[i]

    return ''.join(chars)

def reverse_words_and_order(sentence):
    words = []
    current_word = ""

    # Iterasi per karakter untuk membuat array kata
    for char in sentence:
        if char == ' ':
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char

    # Menambahkan kata terakhir jika ada
    if current_word:
        words.append(current_word)

    # Membalik urutan kata dan membalik setiap kata
    result = []
    for i in range(len(words)-1, -1, -1):
        result.append(reverse_word(words[i]))

    return ' '.join(result)

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

    # Menggabungkan semua paragraf menjadi satu string
    all_text = '\n'.join(paragraphs)

    # Proses pembalikan hanya jika ada input
    if all_text:
        result = reverse_words_and_order(all_text)
        print("\nHasil pembalikan kata dan urutan:")
        print(result)
    else:
        print("Tidak ada input yang dimasukkan.")

if __name__ == "__main__":
    main()
