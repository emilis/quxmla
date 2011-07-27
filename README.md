
# QuXmlA <small>-- Quick Xml Analyzer</small>

This script produces simple stats about _tag paths_ in the given XML files:

- the total occurance of a tag path
- the minimum number it appears in the parent tag path
- the maximum number it appears in the parent tag path

_Tag paths_ are tag names prefixed by parent tag names, e.g.: `/html/head/title`

## Usage

    $ python quxmla.py FILE [FILE] [FILE] ...

## Example output

This is an output from parsing a couple of [Project Gutenberg](http://gutenberg.org/) book RDF files ([example](http://www.gutenberg.org/ebooks/2044.rdf)).

    Processing pg2044.rdf...
    Processing pg36823.rdf...

    Results:

    path    found total min(found in parent)    max(found in parent)
    /   2   None    None
    /rdf:RDF    2   1   1
    /rdf:RDF/cc:Work    2   1   1
    /rdf:RDF/cc:Work/cc:license 2   1   1
    /rdf:RDF/pgterms:agent  3   1   2
    /rdf:RDF/pgterms:agent/pgterms:alias    1   0   1
    /rdf:RDF/pgterms:agent/pgterms:birthdate    2   0   1
    /rdf:RDF/pgterms:agent/pgterms:deathdate    2   0   1
    /rdf:RDF/pgterms:agent/pgterms:name 3   1   1
    /rdf:RDF/pgterms:agent/pgterms:webpage  2   0   1
    /rdf:RDF/pgterms:ebook  2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:creator  2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:description  1   0   1
    /rdf:RDF/pgterms:ebook/dcterms:hasFormat    23  9   14
    /rdf:RDF/pgterms:ebook/dcterms:issued   2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:language 2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:license  2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:publisher    2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:rights   2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:subject  2   0   2
    /rdf:RDF/pgterms:ebook/dcterms:subject/rdf:Description  2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:subject/rdf:Description/dcam:memberOf    2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:subject/rdf:Description/rdf:value    3   1   2
    /rdf:RDF/pgterms:ebook/dcterms:title    2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:type 2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:type/rdf:Description 2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:type/rdf:Description/dcam:memberOf   2   1   1
    /rdf:RDF/pgterms:ebook/dcterms:type/rdf:Description/rdf:value   2   1   1
    /rdf:RDF/pgterms:ebook/marcrel:edt  1   0   1
    /rdf:RDF/pgterms:file   23  9   14
    /rdf:RDF/pgterms:file/dcterms:extent    23  1   1
    /rdf:RDF/pgterms:file/dcterms:format    23  1   1
    /rdf:RDF/pgterms:file/dcterms:format/rdf:Description    23  1   1
    /rdf:RDF/pgterms:file/dcterms:format/rdf:Description/dcam:memberOf  23  1   1
    /rdf:RDF/pgterms:file/dcterms:format/rdf:Description/rdf:value  29  1   2
    /rdf:RDF/pgterms:file/dcterms:isFormatOf    23  1   1
    /rdf:RDF/pgterms:file/dcterms:modified  23  1   1
    /rdf:RDF/rdf:Description    2   0   2
    /rdf:RDF/rdf:Description/dcterms:description    2   1   1

Output is tab-delimited so you can easily copy-paste it into your spreadsheet for easier analysis:

![QuXmlA output in a spreadsheet](http://emilis.info/other/quxmla-spreadsheet.png)


## Requirements

Python >= 2.6 with xml.sax


## License

This is free software, and you are welcome to redistribute it under certain conditions; see LICENSE.txt for details.


## Contact

Emilis Dambauskas <emilis.d@gmail.com>


