def create_krona_plot(data, output_file):
    # Hier Daten verarbeiten und in das Krona-Format umwandeln

    # Beispiel: Datenformat für Krona
    krona_data = """\
    <node name="Root">
        <node name="Domain">
            <node name="Kingdom">
                <node name="Phylum">
                    <node name="Class">
                        <node name="Order">
                            <node name="Family">
                                <node name="Genus">
                                    <node name="Species" magnitude="100"/>
                                </node>
                            </node>
                        </node>
                    </node>
                </node>
            </node>
        </node>
    </node>
    """

    # Schreiben Sie die Daten in eine HTML-Datei
    with open(output_file, 'w') as f:
        f.write(f'<html><head></head><body>{krona_data}</body></html>')

# Beispielaufruf
create_krona_plot(data={}, output_file='output.html')