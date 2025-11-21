clc; clear; close all;

% Saisie des dimensions de A
N = input('Entrez le nombre de lignes de A : ');
M = input('Entrez le nombre de colonnes de A : ');

% Initialisation des matrices A, B et C
A = zeros(N, M);
B = zeros(N, 1);
C = zeros(M, N);

% Saisie des éléments de A
disp('Entrez les éléments de la matrice A :');
for i = 1:N
    for j = 1:M
        A(i, j) = input(sprintf('A(%d,%d) = ', i, j));
    end
end

% Saisie des éléments de B
disp('Entrez les éléments de la matrice B :');
for i = 1:N
    B(i) = input(sprintf('B(%d) = ', i));
end

% Calcul de la matrice C (transposée de A)
for i = 1:M
    for j = 1:N
        C(i, j) = A(j, i);
    end
end

disp('La matrice C (transposée de A) est :');
disp(C);

% Calcul de la matrice D (produit de C et B)
D = zeros(M, 1);
for i = 1:M
    for k = 1:N
        D(i) = D(i) + C(i, k) * B(k);
    end
end

disp('La matrice D est :');
disp(D);
