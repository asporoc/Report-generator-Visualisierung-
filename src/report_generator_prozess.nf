#!/usr/bin/env nextflow

nextflow.enable.dsl = 2
params.kraken2_report = "$baseDir/report.txt"
params.sam_file = "$baseDir/result.sam"

process VisualizeKraken2Report {
    container '/var/share/krona.sif'
    input:
    path kraken2_report

    output:
    path "kraken_report.html"

    script:
    """
    /usr/local/opt/krona/scripts/ImportTaxonomy.pl -tax /home/Annalena.Stamp/work/taxonomy -m 3 -t 5 $kraken2_report kraken_report.html
    """
}

process ConvertSamToKraken {
    input:
    path sam_file

    output:
    path "sam_to_kraken.txt"

    script:
    """
    python ${baseDir}/convert_sam_to_kraken.py $sam_file sam_to_kraken.txt
    """
}

process VisualizeConvertedSam {
    container '/var/share/krona.sif'
    input:
    path sam_to_kraken_txt

    output:
    path "sam.html"

    script:
    """
    /usr/local/opt/krona/scripts/ImportTaxonomy.pl -tax /home/Annalena.Stamp/work/taxonomy -m 3 -t 5 $sam_to_kraken_txt sam.html
    """
}

workflow KronaVisualization {
    take:
    kraken2_report
    sam_file

    main:
    kraken_html = VisualizeKraken2Report(kraken2_report)
    sam_to_kraken_txt = ConvertSamToKraken(sam_file)
    sam_html = VisualizeConvertedSam(sam_to_kraken_txt)

    emit:
    kraken_html
    sam_to_kraken_txt
    sam_html
}

workflow {
  KronaVisualization(Channel.fromPath(params.kraken2_report), Channel.fromPath(params.sam_file))
}