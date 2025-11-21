
%close all, clear all, clc
Ne = 1000 ; fe = 1e6 ;
t = 1/fe*(0:Ne-1) ; f = fe*(0:Ne-1);
a1 = 2 ; f1 = 2e3; x1 = a1*sin(2*pi*f1*t);
a2 = 1 ; f2 = 4e3; x2 = a2*sin(2*pi*f2*t);
a3 = 2 ; f3 = 2e3; x3 = a3*sin(2*pi*f3*t);
x = x1 + x2 + x3;
figure(2) ;
subplot(211) ; plot(t,x)
title('Somme de trois sinusoïdes')
xlabel('Temps en s'); ylabel('Amplitude en V');
X = 2*abs(fft(x))/Ne ;
subplot(212) ;
plot( f(1 :Ne/2),X(1 :Ne/2)) ;
title('Allure fréquentielle de la somme de trois sinusoïdes')
xlabel('Fréquence en Hz'); ylabel('Amplitude en V');
xlim([-3500000 2e8]);
ylim([-0.5 5]);
