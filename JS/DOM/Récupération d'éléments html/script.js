/*
    parentNode : accéder à l'élément parent d'un élément
      nodeType : vérifie le type d'un noeud
      nodeNama : vérifie le nom d'un noeud

    firstChild : accéder au 1er élément d'un noeud
     lastChild : accéder au dernier élément d'un noeud
*/

var paragraph = document.getElementById('myP');
var blockquote = paragraph.parentNode;

var paragraph2 = document.getElementById('myP2');
var first = paragraph2.firstChild;
var last = paragraph2.lastChild;

console.log(blockquote);
console.log(paragraph.innerHTML);
console.log(paragraph.nodeType + '\n\n' + paragraph.nodeName.toLowerCase());

console.log(first.nodeType);
console.log(last.nodeName.toLowerCase);

