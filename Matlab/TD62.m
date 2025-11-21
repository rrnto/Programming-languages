
clear all, close all, clc

fe = 50 ; % fréquences d'échantillonnage
wp = 0.2 ; Rp = 0.3 ;% bande passante
wa = 0.8 ; Ra = 80 ;% bande d'arrêt
% Estimation de l'ordre et bande du filtre
[N,wn] = buttord(wp,wa,Rp,Ra) ;
% Coefficients du Filtre de Butterworth
[b,a] = butter(N,wn,'high') ;
% graphe de la réponse impulsionnelle
[h,t] = impz(b,a,fe) ; figure(1);plot(t,h);grid ;
title('Réponse Impulsionnelle');
xlabel('Temps en s'); ylabel('Amplitude en V');

% Allure de la réponse fréquentielles
[H,w]=freqz(b,a);figure(2);freqzplot(H,w) ;
%[H,w]=freqz(b,a);figure(2);FVTOOL(H,w) ;
title('Réponse Fréquentielle');