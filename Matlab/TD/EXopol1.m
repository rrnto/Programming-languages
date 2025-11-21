clc; clear; close all;

%%1
% Données
x = 1:10;

%y = [-0.7 1.7 1.9 6.2 54 7.1 9.6 10.1 11.4 6.1];
% Ouvrir le fichier1
fid = fopen('fichier1.txt', 'r');
y = (fscanf(fid, '%f'))';
% Fermer le fichier1
fclose(fid);

z = 1:0.2:20;

%M = [1 2 3 4; 5 6 7 8;9 10 11 12;13 14 15 16];
M = load('fichier2.txt');


% Déterminer un polynôme P de degré 3 pour f(x)
P_coeff = polyfit(x, y, 3);
P = polyval(P_coeff, x);

% Calculer les racines du polynôme P
r = roots(P_coeff);

% Calculer P(z)
P_z = polyval(P_coeff, z);

% Stocker les valeurs de z et P(z) dans un fichier 'resultat.txt'
resultats = [z', P_z'];
save('resultat.txt', 'resultats', '-ascii');

% Tracer les points (x,y) et la courbe P(z)
figure;
plot(x, y, '*', z, P_z, 'r');
xlabel('x');
ylabel('y / P(z)');
legend('Données (x, y)', 'P(z)', 'Location', 'best');
title('Modélisation de données et courbe P(z)');
grid on;


%%2
% Calculer l'inverse de M
I = inv(M);

% Calculer la transposée de I
T = I';

% Calculer le déterminant de T
D = det(T);

% Afficher les résultats
disp('Inverse de M :');
disp(I);
disp('Transposée de l''inverse de M :');
disp(T);
disp(['Déterminant de la transposée de l''inverse de M : ', num2str(D)]);

