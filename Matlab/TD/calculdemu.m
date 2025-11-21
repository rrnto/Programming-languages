clc; clear; close all;

%%PROGRAMME POUR CALCULER ?

% Données
x = [0.18, -1.54, 0.42, 0.95];
omega = [2, 1, 3, 1];

% Calcul de mu
mu = sum(omega .* x) / sum(omega);

fprintf('La valeur de mu obtenue par la méthode des moindres carrées est : %f\n', mu);
