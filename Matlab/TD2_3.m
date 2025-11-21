
%close all, clear all, clc
Ne = 1000 ; fe = 1e6 ;
t = 1/fe*(0:Ne-1) ; f = fe*(0:Ne-1);
a = [ 2, 1, 1.5] ; fo = [2e3; 4e3; 5e3];
x = a*sin(2*pi*fo*t);
figure(3) ;
subplot(211) ; plot(t,x)
title('Allure temporelle du produit matriciel')
xlabel('Temps en s'); ylabel('Amplitude en V');
X = 2*abs(fft(x))/Ne ;
subplot(212) ;
plot( f(1 :Ne/2),X(1 :Ne/2)) ;
title('Allure fréquentielle du produit matriciel')
xlabel('Fréquence en Hz'); ylabel('Amplitude en V');
xlim([-5e6 2e8]);
ylim([-0.2 2.3]);