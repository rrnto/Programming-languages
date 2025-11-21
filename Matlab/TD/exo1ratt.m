% Données expérimentales
x = [0.25, 0.50, 1.00, 2.00, 4.00];
y = [5.10, 2.80, 1.99, 1.55, 1.10];

% Calcul des éléments des matrices A et B
n = length(x);
A = zeros(2, 2);
B = zeros(2, 1);

% Calcul des éléments de A
A(1, 1) = sum(ones(1, n)); % Somme de f1(x_i) * f1(x_i) pour tous les i
A(1, 2) = sum(ones(1, n) .* (1 ./ x)); % Somme de f1(x_i) * f2(x_i) pour tous les i
A(2, 1) = A(1, 2); % Symétrie de A
A(2, 2) = sum((1 ./ x).^2); % Somme de f2(x_i) * f2(x_i) pour tous les i

% Calcul des éléments de B
B(1) = sum(y .* ones(1, n)); % Somme de y_i * f1(x_i) pour tous les i
B(2) = sum(y .* (1 ./ x)); % Somme de y_i * f2(x_i) pour tous les i

% Résolution du système d'équations linéaires
C = A \ B;

% Affichage des coefficients c1 et c2
c1 = C(1);
c2 = C(2);
fprintf('Les coefficients c1 et c2 sont : c1 = %.4f, c2 = %.4f\n', c1, c2);

% Création de la courbe ymod
x_mod = linspace(min(x), max(x), 100); % Générer des points x pour la courbe
y_mod = c1 + c2 ./ x_mod; % Calculer les valeurs correspondantes de y

% Affichage des points expérimentaux et de la courbe ymod sur le même graphique
figure;
plot(x, y, 'bo', 'MarkerSize', 8); % Points expérimentaux en bleu
hold on;
plot(x_mod, y_mod, 'r-', 'LineWidth', 2); % Courbe ymod en rouge
xlabel('x');
ylabel('y');
title('Points expérimentaux et courbe y_{mod}');
legend('Points expérimentaux', 'Courbe y_{mod}');
grid on;
