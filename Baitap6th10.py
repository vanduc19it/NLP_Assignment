from underthesea import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

f = open("file002.txt", "r", encoding="utf-8")
text = str(f.read())


documents = word_tokenize(text)
processed_docs = [doc.lower().replace(".","") for doc in documents]
print(processed_docs)

# xay dung bo tu vung
vocab = {}
count = 0
for doc in processed_docs:
    for word in doc.split():
        if word not in vocab:
            count = count +1
            vocab[word] = count
print(vocab)

#One-hot Vector (One-Hot Encoding)
def get_onehot_vector(somestring):
    onehot_encoded = []
    for word in somestring.split():
        temp = [0]*len(vocab)
        if word in vocab:
            temp[vocab[word]-1] = 1 
        onehot_encoded.append(temp)
    return onehot_encoded

print(processed_docs[1])
print(get_onehot_vector(processed_docs[1]))

# Bag of Words
count_vect = CountVectorizer()
bow_rep = count_vect.fit_transform(processed_docs)

print("Vocabulary: ", count_vect.vocabulary_)

print(bow_rep[0].toarray())
print(bow_rep[1].toarray())

# Bag of n-grams
count_vect = CountVectorizer(ngram_range=(1,3))

bow_rep = count_vect.fit_transform(processed_docs)

print("Our vocabulary: ", count_vect.vocabulary_)
print(bow_rep[0].toarray())
print(bow_rep[1].toarray())

# TF-IDF
tfidf = TfidfVectorizer()
bow_rep_tfidf = tfidf.fit_transform(processed_docs)

print("IDF for all words in the vocabulary",tfidf.idf_)
print("-"*10)
print("All words in the vocabulary",tfidf.get_feature_names_out())
print("-"*10)
print("TFIDF representation for all documents in our corpus\n",bow_rep_tfidf.toarray()) 
print("-"*10)