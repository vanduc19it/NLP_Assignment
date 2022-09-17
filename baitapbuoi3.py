from underthesea import word_tokenize

from langdetect import detect
from nltk.corpus import stopwords
import nltk
from stop_words import get_stop_words

# stemming
from nltk.stem.porter import PorterStemmer
# lemmatization
from nltk.stem import WordNetLemmatizer

# Read data file
f = open("file042.txt", "r", encoding="utf-8")
text = str(f.read())
x = open("file002.txt", "r", encoding="utf-8")
paragraph = str(x.read())
y = open("file001.txt", "r", encoding="utf-8")
sentence = str(y.read())




# 1.Unicode Normalization
def Unicode_Normalize(text):
    return text.encode("utf-8")
print("1. Unicode Normalization")
print(Unicode_Normalize(text))

# 2.Tách thành các câu, mỗi câu lưu trên 1 dòng
def sent_tokenize(paragraph):
    return sent_tokenize(paragraph)
print("2. Tách thành các câu, mỗi câu lưu trên 1 dòng")
sents = nltk.sent_tokenize(paragraph)
for sent in sents: 
    print(sent)

# 3.Xóa các stopwords
def delete_stop_words(sentence):
    return delete_stop_words(sentence)
print("3. Xóa các stopwords")
filtered_list = []
words = word_tokenize(sentence)
for w in words:
    if w.lower() not in get_stop_words('english'):
        filtered_list.append(w)
print(filtered_list)

# 4.Tính số lần xuất hiện của mỗi từ, sắp xếp từ cao xuống thấp
def word_count(sentence):
    counts = dict()
    count_sorted = {}
    word2 = sentence.split()

    for word1 in word2:
        if word1 in counts:
            counts[word1] += 1
        else:
            counts[word1] = 1
    count_sorted = {i: j for i, j in sorted(counts.items(), key=lambda item: item[1], reverse=True)}
    return count_sorted
print("4. Tính số lần xuất hiện của mỗi từ, sắp xếp từ cao xuống thấp")
print(word_count(sentence))

# 5.Stemming và Lemmatization
# stemming
stemmer = PorterStemmer()
word1, word2 = "cars", "buildings"
print("5. Stemming và Lemmatization")
print(stemmer.stem(word1),stemmer.stem(word2))
# lemmatization
lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("better", pos="a"))


# 6.Tách từ trong 1 văn bản tiếng Việt
def words_tokenize(text):
    return word_tokenize(text)
print("6. Tách từ trong 1 văn bản tiếng Việt")
text_vn = "Chàng trai GenZ Quảng Trị là Văn Đức khởi nghiệp từ 0 đồng."
print(words_tokenize(text_vn))

# 7.Nhận dạng văn bản tiếng Anh, Việt
def reconize_language(paragraph):
    return reconize_language(paragraph)

print("7. Nhận dạng văn bản tiếng Anh, Việt")
language = detect(paragraph)
if language == "vi":
    print("Đoạn văn bản nhập vào là Tiếng Việt")
elif language == "en": 
    print("Đoạn văn bản nhập vào là Tiếng Anh")










    