
% Définition des paramètres
Fs = 20e3;              % Fréquence d'échantillonnage
t = 0:1/Fs:0.1;         % Vecteur temps
f1 = 2e3;               % Fréquence 1
f2 = 4e3;               % Fréquence 2
f3 = 5e3;               % Fréquence 3
A1 = 2;                 % Amplitude 1
A2 = 1;                 % Amplitude 2
A3 = 1.5;               % Amplitude 3
noise_power = 0.5;      % Puissance du bruit

% Création du signal
x = A1*sin(2*pi*f1*t) + A2*sin(2*pi*f2*t) + A3*sin(2*pi*f3*t) + sqrt(noise_power)*randn(size(t));

% Affichage du chronogramme
figure;
plot(t, x);
xlabel('Temps (s)');
ylabel('Amplitude');
title('Chronogramme du signal');

% Calcul de la transformée de Fourier
N = length(x);
f = Fs*(0:(N/2))/N;
X = fft(x)/N;
X = X(1:N/2+1);

% Affichage du spectre
figure;
plot(f, 2*abs(X));
xlabel('Fréquence (Hz)');
ylabel('Amplitude');
title('Spectre du signal');
