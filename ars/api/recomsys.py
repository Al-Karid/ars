from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import os

try:
    nltk.download("stopwords")
except Exception:
    pass

# Vectorizer
cv = CountVectorizer(ngram_range=(1,1), strip_accents="unicode",stop_words=stopwords.words("french"))

# Load data table
# d = pd.read_csv("filmsallo_films.csv")
dirname = "/".join(os.path.abspath(__file__).split("/")[:-1])
dirname = dirname+"/data/big.csv"

d = pd.read_csv("big.csv")
d.columns = ["id","title","released","producer","actor","plot","genre","thumbnail"]
d = d.replace(np.nan, "NaN", regex=True)

# Feature ingeneering
df = d[["title","genre","producer","actor","plot"]].applymap(lambda x: str(x).lstrip().rstrip())
df[["genre","producer","actor"]] = df[["genre","producer","actor"]].applymap(lambda x: x.lower().split(","))
df["title"] = df["title"].map(lambda x: x.lower())
for idx, row in df.iterrows():
    v_txt = cv.fit_transform([row["plot"]])
    row["plot"] = [w.replace(" ","") for w in cv.vocabulary_]
for idx, row in df.iterrows():
    row["producer"] = [w.replace(" ","") for w in row["producer"]]
    row["actor"] = [w.replace(" ","") for w in row["actor"]]
    row["genre"] = [w.replace(" ","") for w in row["genre"]]
df = df.set_index("title")

df["bow"] = ""
col = df.columns

for idx, row in df.iterrows():
    word = ""
    for c in col:
        word = word + " ".join(row[c])+" "
    row["bow"] = word
df = df.drop(columns = [col for col in df.columns if col!= 'bow'])

# Fitting
cv_txt = cv.fit_transform(df["bow"])

# Similarity
cos_sim = cosine_similarity(cv_txt.toarray(),cv_txt.toarray())

# Recommendation
indices = pd.Series(df.index)
def recommendations(title, cosine_sim = cos_sim):
    try:
        # recommended_movies = []
        idx = indices[indices == title].index[0]
        score_series = pd.Series(cosine_sim[idx]).sort_values(ascending = False)
        top_10_indexes = list(score_series.iloc[1:11].index)
        recommended_movies = d.iloc[top_10_indexes].to_json()
        # for i in top_10_indexes:
            # recommended_movies.append(list(df.index)[i])
        return [recommended_movies,list(d.iloc[idx][["title","released","genre","producer","actor","plot","thumbnail"]])]
        
    except IndexError:
        return 0

def get_8_random_movies():
    dj = d.iloc[list(map(lambda x: int(x),np.random.uniform(0,len(d),8)))]
    return dj.to_json()