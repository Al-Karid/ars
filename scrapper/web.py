import requests
from bs4 import BeautifulSoup
from movie import Movie
import pandas as pd

# Online resources accessor
links = "http://www.allocine.fr/films/?page="
dots = "*************************************"

def get_movies_list(m_list):
    """
    Converts a list of BS4 Tag object to Movie objects
    :param m_list: list of Tag objects
    :returns: Movie : list of Movie objects
    """
    m_infos_list = list()
    for m in m_list:
        movie = Movie(m)
        m_infos_list.append(movie)
    return m_infos_list


def save_movies_to_db(m_list, movies):

        """
        Saves list of Movie into database
        :param m_list:
        """
    
        id = 1
        m_to_csv = []

        for m in m_list:
            title = m.get_title()
            date = m.get_date()
            prod = m.get_producers()
            actors = m.get_actors()
            desc = m.get_description()
            genres = m.get_genres()
            thumb = m.get_thumbnail()

            single_m = [title,date,prod,actors,desc,genres,thumb]
            m_to_csv.append(single_m)
            id = id+1
        d = pd.DataFrame(m_to_csv)
        return d
        #movies.to_csv("m.csv", mode="a")


def scrap(s=1,n=5,file="allo_movies"):

    #m_headers = ["id","title","released","producer","actor","genre","plot","thumbnail"]
    movies = pd.DataFrame()
    file = file+".csv"

    for i in range(s,s+n):

        # Loading link
        lnk = ""
        lnk = links+str(i)
        print(dots+"\nProcessing: "+lnk)
        page = requests.get(lnk)
        soup = BeautifulSoup(page.content, "html.parser")

        # List of Tag objects each representing a movie data
        m_list = list(soup.findChildren(class_="mdl"))
        m_data = get_movies_list(m_list)
        d = save_movies_to_db(m_data, movies)
        movies = movies.append(d, ignore_index=True)
        print(movies)
        print("Done: "+lnk+"\n")

    movies.to_csv(file, mode="a", header=False)

last_scrap = 16