% Définir les paramètres du signal
A = 1; % Amplitude
f = 10; % Fréquence en Hz
Ne = 1000; % Nombre d'échantillons
fe = 1000; % Fréquence d'échantillonnage
t = (1:Ne)/fe; % Vecteur temps

% Calculer le signal
x = A * sin(2*pi*f*t);

% Appliquer une moyenne mobile pour adoucir le signal
x_smooth = smooth(x, 10, 'moving');

% Tracer les signaux original et adouci
figure;
subplot(2,1,1);
plot(t, x);
xlabel('Temps (s)');
ylabel('Amplitude');
title('Signal original');
subplot(2,1,2);
plot(t, x_smooth);
xlabel('Temps (s)');
ylabel('Amplitude');
title('Signal adouci');
