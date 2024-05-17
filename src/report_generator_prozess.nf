#!/usr/bin/env nextflow

nextflow.enable.dsl = 2
params.kraken2_report = "$baseDir/report.txt"
params.sam_file = "$baseDir/result.sam"

process Krona {
    container '/var/share/krona.sif'
    publishDir "/tmp/", mode: "copy", overwrite: true
    input:
    path report

    output:
    path "${report.getBaseName()}.html"

    script:
    """
    /usr/local/opt/krona/scripts/ImportTaxonomy.pl -tax /home/Annalena.Stamp/work/taxonomy -m 3 -t 5 ${report} -o ${report.getBaseName()}.html
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
workflow KronaVisualization {
    take:
    kraken2_report
    sam_file

    main:
    sam_to_kraken_txt = ConvertSamToKraken(sam_file)
    kronas = Krona(kraken2_report.concat(sam_to_kraken_txt))

    emit:
    kronas
}

workflow krona_workflow {
  KronaVisualization(Channel.fromPath(params.kraken2_report), Channel.fromPath(params.sam_file))
}
