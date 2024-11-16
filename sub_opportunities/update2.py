import requests
import os

# Configura il tuo token API

def get_api():
    os.chdir('../')
    a = open("api_raindrop.txt",'r').read()
    os.chdir('./webpage')
    return a

# Funzione per ottenere le collezioni
def get_collections():
    headers = {"Authorization": f"Bearer {get_api()}"}
    url = "https://api.raindrop.io/rest/v1/collections"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["items"]

# Funzione per ottenere i segnalibri di una collezione
def get_bookmarks(collection_id):
    headers = {"Authorization": f"Bearer {get_api()}"}
    url = f"https://api.raindrop.io/rest/v1/raindrops/{collection_id}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["items"]

# Funzione per scrivere un file HTML
def write_html_file(collection_name, bookmarks):
    filename = f"./sub_opportunities/{collection_name}.html"
    if collection_name=='Articles':
        filename = f"./articles/{collection_name}.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html lang='en'>\n<head>\n")
        f.write(f"    <meta charset='UTF-8'>\n")
        f.write(f"    <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n")
        f.write(f"    <title>{collection_name}</title>\n")
        f.write("</head>\n<body>\n")
        f.write(f"    <h1>Collezione: {collection_name}</h1>\n")
        f.write("    <ul>\n")
        for bookmark in bookmarks:
            f.write(f"        <li><a href='{bookmark['link']}' target="_blank">{bookmark['title']}</a></li>\n")
        f.write("    </ul>\n")
        f.write("</body>\n</html>")
    print(f"File creato: {filename}")

# Funzione principale
def main():
    collections = get_collections()
    for collection in collections:
        print(collection)
        collection_name = collection["title"]
        collection_id = collection["_id"]
        bookmarks = get_bookmarks(collection_id)
        write_html_file(collection_name, bookmarks)

if __name__ == "__main__":
    main()