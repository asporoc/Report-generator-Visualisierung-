# Report-generator-Visualisierung-

Basis:
- scheinbar mit Bioconda arbeiten
- Name der Knoten und Struktur des Baumes sind in den Dateien nodes.dmp und names.dmp
- die Zuordnung von GenBank Accessions können durch Extraktion des DB-Dumps oder durch die
REST-API bei NCBI anfragen
- wenn ein Read etwas uneindeutig ist, also z.B. auf zwei Unterarten mappt, dann sollten einfach
beide hochgezählt werden anstatt das Ergebnis zu verwerfen

Kraken2:
- Zuordnung von Readanteilen zu taxonomy-IDs
- tadanomy-ID = eindeutige Bezeichnung für die unterschiedlichen Einträge im Tree of Life

Bowtie2:
- Zuordnung von Reads zu Referenzsequenz
- häufigste Formate sind SAM (Sequence Alignment/Map) und BAM (Binary Alignment/Map), wobei
BAM eine binäre Version einer SAM-Datei ist
- zur Analyse/Anzeige einer BAM-Datei kann man samtools verwenden:
"samtools view -h example.bam > example.sam"

GenBank Accession:
- kurz "Accession-Nummer"
- ist eine eindeutige ID, die einem Sequenzdatensatz in der GenBank-Datenbank zugeordnet ist
- die GenBank ist die größte Nukleotidsequenzen-Datenbank
- ist eine alphanumerische Zeichenkette
- Beispiel: NM_0543325343.4 (NM_ = mRNA; .4 = Version)

Probleme:
- Unterschiedliche Formate der Input-Files

Aufgabe:
- Umwandlung der Bowtie2-Files in das gleiche Format wie Kraken2-Files durch Zuordnung der Sequenznamen 
(GenBank-Accession steht in Seq.-Namen) zu einer TaxID im Baum
- Kora-Plots verstehen und mit Python erstellen

Bearbeitung 
- Um die Bowtie2-File in das gleiche Format wie einen Kraken2-Report zu bringen wurde das convert_sam_to_kraken.py script geschrieben. Es befindet sich im Source Ordner. 