

% Définition du temps d'échantillonnage
Fs = 1000 ; % Hz
t = 0:1/Fs:0.1 ; % 100 ms
Ne = 200;

% Caractéristiques du signal
a = 1 ; T = 0.02 ; rc = 0.5;

% Rampe comprise entre 0 et T
tm = mod(t,T) ;

% Création des triangles
% création du signal x = 0
x = zeros(size(t)) ;

% rampe positive de 0 à rc/2
k1 = find(tm/T<=rc/2) ; x(k1) = tm(k1)/T ;

% rampe négative de rc/2 à rc
k2 = find((tm/T>=rc/2)&(tm/T<rc)) ; x(k2) = rc - tm(k2)/T ;

% Normalisation
x = x/max(x) ;

% Tracé du signal
figure(12)
plot(t,x)
ylim([-0.1 1.1]);
xlabel('Temps (s)')
ylabel('Amplitude')
title('Signal d''impulsion triangulaire')


% Calcul de la FFT
X = fft(x) ;
L = length(x) ;
P2 = abs(X/L) ;
P1 = P2(1:L/2+1) ;
P1(2:end-1) = 2*P1(2:end-1) ;
f = Fs*(0:(L/2))/L ;
Xs = fftshift(X);

% Tracé du spectre
figure(13)
plot(f,P1) ;

xlabel('Fréquence (Hz)')
ylabel('Amplitude')
title('Spectre du signal d''impulsion triangulaire')

figure(14)
plot(f,abs(Xs)) ;

 









