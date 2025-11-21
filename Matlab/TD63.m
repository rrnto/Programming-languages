
close all,clear all,clc
a=1;T=0.02;rc=0.5;fe=1000;Ne=400;
t=1/fe*(0:Ne-1); f=fe*(0:Ne-1)/Ne ;dsp=0.5 ;
% Caractérisitiques du signal
% apmlitude, période et rapport cyclique
a = 1 ; T=0.02 ; rc = 0.5;
% Rampe comprise entre 0 et T
tm = mod(t,T) ;
% Création du signal rectangulaire
x = a*(tm/T <= rc) ;
% Création du signal bruit uniforme
ru=rand(1,Ne)*dsp; X=x+ru;
figure(5);
Ru=2*abs(fft(X))/Ne;
title('Chronogramme du signal bruité');
xlabel('temps en s'); ylabel('Amplitude en V');
subplot(211);
plot(t,X,t,x,'r');grid on ;
title('Spectre du signal bruité');
subplot(212);
plot(f(1:Ne/2),Ru(1:Ne/2));
xlabel('fréquence en Hz'); ylabel('Amplitude en V');