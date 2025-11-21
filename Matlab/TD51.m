

clear all, close all, clc

% Paramètres du signal
B = 62.4; % bande passante en Hz
A = 1; % amplitude maximale du signal
sigma = 0.08; % amplitude du bruit gaussien

% Temps d'échantillonnage
Te = 1e-3; % 1 kHz

% Temps et échantillons
t = -0.1:Te:0.1;
N = length(t);

% Signal u(t)
u = A*sinc(B*t);

% Signal bruité x(t)
b = sigma*randn(1,N); % bruit gaussien
x = u + b;

% Tracé du signal u(t)
figure(1);
plot(t, u);
title('Signal u(t)');
xlabel('Temps (s)'); 
ylabel('Amplitude (V)'); ylim([-0.4 1.1]);

% Tracé du signal bruité x(t)
figure(2);
plot(t, x, 'r');
title('Signal bruité x(t)');
xlabel('Temps (s)'); 
ylabel('Amplitude (V)'); ylim([-0.4 1.2]);


% Durée du lobe principal et amplitudes des lobes secondaires
n = 1:5;
duree_lobe = 1/(2*B);
amplitudes = sin(n*pi/2)./(n*pi/2);

% Affichage des résultats
fprintf('Durée du lobe principal : %.4f s\n', duree_lobe);
fprintf('Amplitudes des lobes secondaires : \n');
fprintf('a2 = %.2f\n', amplitudes(2));
fprintf('a3 = %.2f\n', amplitudes(3));
fprintf('a4 = %.2f\n', amplitudes(4));

% Caractéristiques temporelles du signal u(t)
xdc = mean(u); % valeur moyenne
P_norm = trapz(t, abs(u).^2)/duree_lobe; % puissance normalisée
P = P_norm * A^2; % puissance
xac = sqrt(P_norm) * A; % valeur efficace de la composante alternative

% Affichage des résultats
fprintf('Valeur moyenne : %f\n', xdc);
fprintf('Puissance normalisée : %f\n', P_norm);
fprintf('Puissance : %f\n', P);
fprintf('Valeur efficace de la composante alternative : %.4f\n', xac);

% Tracer l'histogramme
figure(3)
hist(b, 50);

