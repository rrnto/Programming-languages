var paragraph = document.getElementById('myP');
var child = paragraph.lastChild;

while(child) {
    if(child.nodeType===1) {
        console.log(child.firstChild.data);
    }
    else {
        console.log(child);
    }
}