# ARS

AlloCine.fr web movie list scrapper with basic recommender system

<hr>

### How it works

```
git clone https://github.com/Al-Karid/recomsys.git
cd recomsys
```

Two steps to get it working properly

##### 1 Launch the recommender system server

Run the server

```python
python3 -m pip install .
```
Before you run the server you will need to install the stopwords from <br>Ipython</b> or as it pleases you
```
import ntlk
nltk.download("stopwords")
```

The <b>ars</b> CLI will be installed and ready to use, just like normal pip package (it actually is one now)

```
ars web serve
```

Above command open an API interface at <b>localhost:5000</b>

##### 2 Launch the UI

Enter UI directory and install the dependencies

```
cd ui
npm install
```

Run the UI

```
npm start
```

