clc; clear; close all;

% Saisie de x et n au clavier
x = input('Entrez la valeur de x : ');
n = input('Entrez le nombre de termes de la série (n) : ');

% Initialisation de la somme
resultat = 0;

% Calcul de la série de Taylor pour exp(x)
for k = 0:n
    % Calcul du k-ème terme de la série
    terme = x^k / factor(k);
    resultat = resultat + terme;
end

% Affichage du résultat
fprintf('exp(%f) = %f\n', x, resultat);




