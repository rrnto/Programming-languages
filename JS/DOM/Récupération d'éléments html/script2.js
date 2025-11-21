var paragraph = document.getElementById('myP');
var first = paragraph.firstChild;
var next = first.nextSibling;

console.log(next.firstChild.data);