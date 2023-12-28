//This file is not used at the moment 
const bibtexDataAttribute = 'data-bibtex';

function copyReferenceToClipBoard(element) {
  let bibtexRef = element.getAttribute(bibtexDataAttribute);
  navigator.clipboard.writeText(bibtexRef).then(
    () => {
      console.log("reference copied to clipboard successful")
    },
    () => {
      console.log("reference copied to clipboard failed")
    }
  );
}

var publicationList = document.getElementsByTagName('publication');
for (let publication of publicationList) {
  var parentNode = publication.parentNode;

  var title = document.createElement('pub-title');
  title.innerText = publication.getAttribute('title');
  parentNode.appendChild(title)
  var break1 = document.createElement('br');
  parentNode.appendChild(break1);

  var authors = document.createElement('pub-authors');
  authors.innerText = publication.getAttribute('authors');
  parentNode.appendChild(authors);
  var break2 = document.createElement('br');
  parentNode.appendChild(break2);

  var lang = document.createElement('lang');
  lang.innerText = publication.getAttribute('lang');
  parentNode.appendChild(lang);

  if (!Object.is(publication.getAttribute('entry-type'), null) &&
    !Object.is(publication.getAttribute('entry-type'), '')) {
    var entryType = document.createElement('entry-type');
    entryType.innerText = publication.getAttribute('entry-type');
    parentNode.appendChild(entryType);
  }

  if (!Object.is(publication.getAttribute('paper-link'), null) &&
    !Object.is(publication.getAttribute('paper-link'), '')) {
    var linkToPaper = document.createElement('a');
    linkToPaper.className = 'pub-paper-link';
    linkToPaper.innerHTML = 'link to paper';
    linkToPaper.href = publication.getAttribute('paper-link');
    parentNode.appendChild(linkToPaper);
  }

  if (!Object.is(publication.getAttribute('bibtex'), null) &&
    !Object.is(publication.getAttribute('bibtex'), '') &&
    !Object.is(publication.getAttribute('bibtex'), ' ')) {
    let bibtex = document.createElement('bibtex');
    bibtex.setAttribute('data-bibtex', publication.getAttribute('bibtex'));
    bibtex.addEventListener('click', copyReferenceToClipBoard);
    parentNode.appendChild(bibtex);
  }


  parentNode.removeChild(publication);
}