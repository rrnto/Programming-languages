
clear all, close all, clc

Ne = 4096; xdc = 2; Pac = 0.5 ;
bruit = sqrt(Pac)*randn(1,Ne) + xdc ;
dsp = 1/Ne*(abs(fft(bruit))) .^2;
figure(4) ;
subplot(211) ; plot(bruit)
xlabel('Temps en s'); ylabel('Amplitude en V');
title('Allure temporelle du bruit normal')
xlim([-100 4300]);
subplot(212) ; plot(10*log10(abs(dsp)));
xlabel('Fréquence en Hz'); ylabel('Amplitude en V');
title('Allure fréquentielle du bruit normal')
xlim([-100 4300]);