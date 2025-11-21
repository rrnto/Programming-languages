
Fs = 1000; % Hz
%t = 0:1/Fs:0.02;

A = 1;
alpha = 0.005;
f0 = 200;
phi = 0;

% Donnee non GPT
Ne = 200; fe = 1e3; t = (1:Ne)/fe;
tau = 0.005; Tp = 0.005; T = 0.02;
tm=mod(t, T);


%x = A * exp(-alpha*t) .* cos(2*pi*f0*t + phi);
x = A * exp(-tm/tau) .* sin(2*pi/Tp*tm);


% Tracé du chronogramme
figure(4);
plot(t, x);
xlabel('Temps (s)');
ylabel('Amplitude');
title('Signal de sinusoïdes exponentiellement amorties');

% Tracé du spectre
X = fft(x);
L = length(x);
P2 = abs(X/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);
f = Fs*(0:(L/2))/L;

figure(5);
plot(f, P1);
xlim([0 1000]);
xlabel('Fréquence (Hz)');
ylabel('Amplitude');
title('Spectre du signal de sinusoïdes exponentiellement amorties');



