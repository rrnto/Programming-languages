var prenoms = [], prenom;

while(prenom = prompt('Entrez un prénom : '))
{
    prenoms.push(prenom);
}

if(prenoms.length > 0)
{
    alert(prenoms.join(' '));
}

else
{
    alert('Il n\'y a aucun prénom en mémoire');
}