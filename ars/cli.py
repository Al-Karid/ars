import click

@click.group(name="ars", help="CLI for a basic recommander system around AlloCine.fr")
def ars():
    pass

# Scrapping group
@ars.group(name="scrapper", help="CLI to scrap movies lists from AlloCine.fr")
def scrapper():
    pass

@scrapper.command(name="scrap", help="Scrap a list of movies in csv format")
@click.option("--start-page","-s", default=1, help="Page to start scrapping from")
@click.option("--num-pages","-n", default=5, help="Number of pages to scrap")
@click.option("--dest-file","-d", default="movies", help="Destination file name")
def scrap(start_page:int, num_pages:int, dest_file:str):
    from ars.scrapper.web import scrap
    scrap(s=start_page, n=num_pages, file=dest_file)

# Web serving
@ars.group(name="web", help="CLI to serve web API interface of the recommander system")
def web():
    pass

@web.command(name="serve", help="Serve the API interface")
@click.option("--data-path", "-d", default="data/big.csv", help="Path of AlloCine.fr movies database")
def serve(data_path:str):
    from ars.api.api import run
    run()

if __name__ == "__main__":
    ars()