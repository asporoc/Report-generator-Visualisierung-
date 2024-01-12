import subprocess
import sys

# Es ist wichtig vor Ausführung des Skripts Krona und die benötigten Tools zu installieren.
# Um die HTML-Datei anzuzeigen, kann man einfach die Datei in einem Webbrowser öffnen.

def run_import_taxonomy(kraken_report_file):
    # ImportTaxonomy.pl wird verwendet, um taxonomische Daten zu importieren und sie für die Visualisierung mit Krona vorzubereiten.
    script_path = './scripts/ImportTaxonomy.pl'
    output_file = 'krakenreport.html'

    command = [script_path, '-m', '3', '-t', '5', kraken_report_file, '-o', output_file]

    subprocess.run(command, check=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Benutzung: python visualize_kraken2Report.py <kraken2_report.txt>")
        sys.exit(1)

    kraken_report_file = sys.argv[1]
    run_import_taxonomy(kraken_report_file)
