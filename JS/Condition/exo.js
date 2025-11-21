var age = parseInt(prompt('Entrez votre âge :'));

if(1 <= age && age <= 6)
   { alert('Vous êtes un jeune enfant.'); }

else if(7 <= age && age <= 11)
   { alert('Vous êtes un enfant qui a atteint l\'âge de raison.'); }

else if(12 <= age && age <= 17)
   { alert('Vous êtes un adolescent.'); }

else if(18 <= age && age <= 120)
   { alert('Vous êtes un adulte..'); }

else
   { alert('Zombie'); }