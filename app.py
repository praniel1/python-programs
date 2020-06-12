# from sklearn.externals import joblib
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder


data = pd.read_csv('book32-listing.csv',encoding = "ISO-8859-1")

columns = ['Id', 'Image', 'Image_link', 'Title', 'Author', 'Class', 'Genre']
data.columns = columns

books = pd.DataFrame(data['Title'])
author = pd.DataFrame(data['Author'])
genre = pd.DataFrame(data['Genre'])

data['Author'] = data['Author'].fillna('No Book')
data['Title'] = data['Title'].fillna('No Book')

feat = ['Genre']
for x in feat:
    le = LabelEncoder()
    le.fit(list(genre[x].values))
    genre[x] = le.transform(list(genre[x]))
    
data['everything'] = pd.DataFrame(data['Title'] + ' ' + data['Author'])

vectorizer = TfidfVectorizer(min_df=2, max_features=70000, strip_accents='unicode',lowercase =True,
                            analyzer='word', token_pattern=r'\w+', use_idf=True, 
                            smooth_idf=True, sublinear_tf=True, stop_words = 'english')
vectors = vectorizer.fit_transform(data['everything'])   

def predict(title):
	s = title
	text = []
	text.append(s)
	text[0] = text[0].lower()
	arr = (vectorizer.transform(text))
	clf = joblib.load('best.pkl')
	prediction = (clf.predict(arr))
	prediction = le.inverse_transform(prediction)[0]
	return prediction