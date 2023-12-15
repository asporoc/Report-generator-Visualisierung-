# Die Dateiformate SAM und Kraken2 sind sehr unterschiedlich
# hierfür muss eine Zuordnung der Sequenznamen zu einer TaxID
# erfolgen. Die Zuordnung kann durch eine REST-API bei NCBI angefragt werden.
# in nodes.dmp sieht man die Struktur des Baumes (Tree of Life) und in names.dmp
# die Namen der Knoten

# zunächst müssen die Informationen aus der SAM-Datei extrahiert werden,
# welche GenBank Accessions entsprechen. Dies sind hier die Referenzsequenzinformationen
# in der Spalte "RNAME" oder "XA"
# mit der "Esummary"-Abfrage kann man Informationen zu den GenBank Accessions abrufen
# der Vorgang muss für jede Accession in der SAM-Datei wiederholt werden
# die API gibt JSON-Daten zurück, die Informationen zum GenBank Accession enthalten,
# aus denen man dann die benötigten Daten extrahieren kann
# HINWEIS: Ein API-Schlüssel könnte nützlich sein, um Anfragebeschränkungen zu umgehen

#Lib um HTTP-Anfragen zu verwenden. Einfach per "pip install requests" installieren
import requests

def getAccession(sam_file_path):
    with open(sam_file_path, "r") as sam_file:
        for line in sam_file:
            if not line.startswith("@"):
                columns = line.split("\t")
                accession = columns[2]
                print(f"Accession: {accession}")

def get_genbank_info(accession):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    endpoint = "esummary.fcgi"
    params = {
        "db": "nuccore",
        "id": accession,
        "retmode": "json"
    }

    response = requests.get(f"{base_url}{endpoint}", params=params)

    if response.status_code == 200:
        genbank_info = response.json()
        return genbank_info
    else:
        print(f"Error: {response.status_code}")
        return None