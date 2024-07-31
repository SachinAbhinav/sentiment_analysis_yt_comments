import joblib
import regex as re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

sw = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

#  Load the model
model = joblib.load('utils/saved_models/saved_svm_full.pkl')
vectorizer = joblib.load('utils/saved_models/saved_count_vectorizer_full.pkl')

def clean(s):
    s = re.sub("[^a-zA-Z]", " ", s)
    words = s.split()
    rem_sw = [word for word in words if word not in sw]
    lemm_words = [lemmatizer.lemmatize(word) for word in rem_sw]
    return ' '.join(lemm_words)


def compute_results(comments):
    positive, negative, neutral = (0, 0, 0)
    for comment in comments:
        comment = clean(comment)
        output = model.predict(vectorizer.transform([comment]))[0]
        if output == 0:
            neutral += 1
        elif output == 1:
            positive += 1
        else:
            negative += 1
    return (positive, negative, neutral)
    
    