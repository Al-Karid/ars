# Helper functions
def strip(txt):
    txt = txt.rstrip().lstrip()
    return txt


def get_duration(m):
    try:
        duration = list(m.findChild(class_="meta-body-info").children)[4]
        duration = duration.replace(" ", "")
        return strip(duration)
    except AttributeError:
        return ""


def get_actors(m):
    names = []
    try:
        actors = m.findChild(class_="meta-body-actor")
        actors = actors.findChildren(class_="blue-link")
        for actor in actors:
            name = strip(actor.text)
            names.append(name)
        names_str = ", ".join(names)
        return names_str
    except AttributeError:
        return ""


def get_producers(m):
    names = []
    try:
        producers = m.findChild(class_="meta-body-direction")
        producers = producers.findChildren(class_="blue-link")
        for prod in producers:
            name = strip(prod.text)
            names.append(name)
        names_str = ", ".join(names)
        return names_str
    except AttributeError:
        return ""


def get_genres(m):
    classes = ["date", "spacer"]
    try:
        mb_info = m.findChildren(class_="meta-body-info")
        mb_info = mb_info[0].findChildren("span")
        l = list()
        for m in mb_info:
            for c in m.attrs["class"]:
                if c not in classes:
                    l.append(m)
        genres = ", ".join([g.text for g in l])
        return genres
    except (AttributeError, IndexError):
        return ""

# Movie class
class Movie:

    def __init__(self, m_data):
        self.movie = m_data

    # Attributes queries

    def get_title(self):
        try:
            title = self.movie.findChild(class_="meta-title").text
            return strip(title)
        except AttributeError:
            return ""

    def get_date(self):
        try:
            date = self.movie.findChild(class_="date").text
            return strip(date)
        except AttributeError:
            return ""

    def get_duration(self):
        duration = get_duration(self.movie)
        return duration

    def get_producers(self):
        producer = get_producers(self.movie)
        return strip(producer)

    def get_actors(self):
        actors = get_actors(self.movie)
        return actors

    def get_description(self):
        try:
            desc = self.movie.findChild(class_="content-txt").text
            return strip(desc)
        except AttributeError:
            return ""

    def get_genres(self):
        genres = get_genres(self.movie)
        return genres
        

    def get_thumbnail(self):
        ext = ["jpg","jpeg","png"]
        try:
            thumb = self.movie.find(class_="thumbnail-container").find("img")["src"]
            if thumb.split(".")[-1] not in ext:
                thumb = self.movie.find(class_="thumbnail-container").find("img")["data-src"]
                return thumb
            else:
                return thumb
        except (AttributeError, KeyError):
            return ""