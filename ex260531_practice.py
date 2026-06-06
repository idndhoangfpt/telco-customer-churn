# vietnam machine learning deep learning book
# moi chữ xuất hiện bao nhiêu lần = boW
# Tạo Bag-OF-Word chọ tập dataset sau corpus = "Tôi thích môn toán", Tôi thích AI", , Tôi thích xxx"]
# sau đó tạo list có tên vector de luu vector sau khi thuc hiện bước Tokenziaztion sau "TOi thich AI thich xxx" biet BOW duoc sap theo thu tu tang dan

# lambda tham_so: gia_tri_tra_ve
# add = lambda a, b: a + b
# print(add(2, 3))


docs = ["toi thich ai", "toi thich lap trinh ai"]

word_count = {}

for sentence in docs:
    words = sentence.split()

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

# Sắp xếp theo số lần xuất hiện giảm dần
sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)

for word, count in sorted_words:
    print(f"{word}: {count}")
