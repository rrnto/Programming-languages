clc; clear; close all;

% Conditions initiales
y0 = 1;
tspan = [0, 2]; % Plage de temps

% Définir l'équation différentielle sous forme d'une fonction inline
diff_eq = @(t, y) -2*y + 3*exp(-4*t);

% Résolution avec ode23
[t1, y1] = ode23(diff_eq, tspan, y0);

% Résolution avec ode45
[t2, y2] = ode45(diff_eq, tspan, y0);

% Solution exacte
t_exact = linspace(0, 2, 100); % Plus de points pour une meilleure représentation
y_exact = (5*exp(-2*t_exact) - 3*exp(-4*t_exact))/2;

% Graphique
figure;
plot(t1, y1, 'r-', t2, y2, 'b--', t_exact, y_exact, 'g-.', 'LineWidth', 1.5);
xlabel('t');
ylabel('y');
title('Comparaison des solutions numériques et exacte');
legend('ode23', 'ode45', 'SolutionExacte', 'Location', 'best');
grid on;
