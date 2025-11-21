clc; clear; close all;

% Racine double
x1 = 1;
x2 = 1;

% Générer le polynôme à partir des racines doubles
p = poly([x1, x2]);

% Extraire les coefficients a, b et c
a = p(1);
b = p(2);
c = p(3);

% Affichage des coefficients
disp(['Coefficient a : ', num2str(a)]);
disp(['Coefficient b : ', num2str(b)]);
disp(['Coefficient c : ', num2str(c)]);

% Stockage des valeurs dans un fichier "resultat.txt"
resultats = [a, b, c];
save('resultat.txt', 'resultats', '-ascii');
