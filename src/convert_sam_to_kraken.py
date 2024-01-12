import sys

ref_to_taxId = {"NZ_CP139575": ["1579", 0], "NZ_CP110619": ["1773", 0], "OP326284": ["10244", 0]}

# Dieses Skript dient zur Konvertierung von SAM-Dateidaten in ein Format, das einem Kraken-Bericht ähnelt.
# Der Schwerpunkt liegt auf der Zählung der Anzahl von Reads, die an verschiedenen Referenzsequenzen ausgerichtet sind.


def process_sam_file(sam_file_path, output_file_path):
    # Function to process the SAM file and create a mock Kraken report
    with open(sam_file_path, 'r') as sam_file, open(output_file_path, 'w') as output_file:
        for line in sam_file:
            if line.startswith('@'):
                # Skip header lines
                continue
            fields = line.strip().split('\t')
            read_name = fields[0]
            reference_name = fields[2]
            if reference_name not in ref_to_taxId:
                continue
            ref_to_taxId[reference_name][1] += 1
        for name in ref_to_taxId.keys():
            output_file.write(
                "0\t%d\t%d\t0\t%s\t%s\n" % (ref_to_taxId[name][1], ref_to_taxId[name][1], ref_to_taxId[name][0], name))


def main():
    if len(sys.argv) != 3:
        print("Usage: python convert_sam_to_kraken.py <input_sam_file> <output_file>")
        sys.exit(1)
    sam_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    process_sam_file(sam_file_path, output_file_path)


if __name__ == "__main__":
    main()
