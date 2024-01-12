#!/usr/bin/env nextflow

params.kraken2_report = "$baseDir/kraken2_report.txt"
params.sam_file = "$baseDir/sample.sam"

process VisualizeKraken2Report {
    input:
    path kraken2_report

    output:
    path "kraken_report.html"

    script:
    """
    python visualize_kraken2Report.py $kraken2_report
    """
}

process ConvertSamToKraken {
    input:
    path sam_file

    output:
    path "sam_to_kraken.txt"

    script:
    """
    python convert_sam_to_kraken.py $sam_file sam_to_kraken.txt
    """
}

process VisualizeConvertedSam {
    input:
    path sam_to_kraken_txt

    output:
    path "sam.html"

    script:
    """
    python visualize_kraken2Report.py $sam_to_kraken_txt
    """
}

workflow KronaVisualization {
    

    main:
    kraken_html = VisualizeKraken2Report(kraken2_report)
    sam_to_kraken_txt = ConvertSamToKraken(sam_file)
    sam_html = VisualizeConvertedSam(sam_to_kraken_txt)

    emit:
    kraken_html
    sam_to_kraken_txt
    sam_html
}
