
%%  Définition des constantes : nombre d’échantillon par symbole, nombre de périodes
Nech = 80 ; Nsymb = 12;
% Nombre total de points, fréquence d’échantillonnage
Ne = Nech*Nsymb ; fe =1e3 ;
% vectorisation du temps et de la fréquence
t = (0 :Ne-1)/fe ; f = fe * ( 1:Ne) /Ne ;

% % Caractéristiques du signal
% amplitude, période et rapport cyclique
a = 1 ; T=0.02 ; rc = 0.5;
% Rampe comprise entre 0 et T
tm = mod(t,T) ;
% Création du signal rectangulaire
x = a*(tm/T <= rc) ;
figure (1)
%plot(x, 'linewidth', 1.5);
plot(x); grid on
%xlim([0 200]);
ylim([-0.01 1.01]);
x_fft = fft(x);
%X = 2*abs(x_fft)/Ne; test sans fftshift
X = 2*abs(fftshift(x_fft))/Ne;
figure(2)
plot(f, X);
%axis([300 700 0 1.2])
grid on
