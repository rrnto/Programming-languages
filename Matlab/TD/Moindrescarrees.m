clc; clear; close all;

% Données
H = [0 5000 11000 20000 47000]; % Altitude géopotentielle en m
h = [0 5004 11019 20063 47350]; % Altitude vraie en m

% Calcul des coefficients a et b
n = length(H);
a = (n*sum(H.*h) - sum(H)*sum(h)) / (n*sum(H.^2) - sum(H)^2);
b = (sum(h) - a*sum(H)) / n;

% Affichage des coefficients
fprintf('Coefficient a: %f\n', a);
fprintf('Coefficient b: %f\n', b);

% Calcul des valeurs de h prédites à partir de la formule h = aH + b
H_pred = 0:1000:50000;
h_pred = a * H_pred + b;

% Représentation graphique
figure;
plot(H, h, 'bo', 'MarkerFaceColor', 'b', 'MarkerSize', 8); % Points bleus pour les valeurs discrètes
hold on;
plot(H_pred, h_pred, 'r-', 'LineWidth', 2); % Ligne rouge pour les valeurs prédites
xlabel('Altitude géopotentielle (m)');
ylabel('Altitude vraie (m)');
title('Relation entre altitude vraie et altitude géopotentielle');
legend('Données discrètes', 'Valeurs prédites', 'Location', 'best');
grid on;

% Calcul de l'altitude vraie pour une altitude géopotentielle donnée
H_given = 8253; % Altitude géopotentielle donnée
h_given = a * H_given + b;
fprintf('Altitude vraie pour une altitude géopotentielle de %d m: %f m\n', H_given, h_given);
