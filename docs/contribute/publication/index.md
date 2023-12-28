---
icon: material/book-plus
---

# Contributing to research publications 

To add a new entry to the [Research Publications](../publication/index.md) section add a new markdown file with the extension `.md` to the `publication/paper/` folder. A markdown template to add a publication entry is available at `publication/paper/0-publication-template.md`. The file contains the following html tag structure: 

```
.
└── publication
    ├── pub-title           - title of the publication
    ├── pub-authors         - authors of the publication
    ├── pub-year            - publication year
    ├── lang                - relevant languages
    ├── entry-type          - type of publication
    ├── http link**         - http link to publication website
    ├── bibtex file link**  - link to .bib file in publication/bib
    └── bibtex-copy         - add the bibtex string in here to enable click to copy
```
In each tag has the following placeholder `<<-- text -->>` added denoting where the relevant information should be added. Replace the placeholder with the information of the new publication. 

- **pub-title, pub-authors, pub-year** are mandatory and information should be populated for those tags.
- **Link to the paper** is also mandatory and is expected to be present. 
- Information to the rest of the tags can be omitted only if the data to those are **impossible** to be added. If a tag is not populated it should be removed from the markdown file.

### Adding BibTeX file 

Add complete references to the publication entry in the BibTeX format. Save the reference in `publication/bib` folder as a `.bib ` file. More info on BibTeX [here](https://www.bibtex.org/). An online bibtex converter can be used to generate reference in bibtex for the publication. 