

%close all, clear all, clc;
Ne = 1000 ; fe = 1e6 ;
t = 1/fe*(0:Ne-1); f = fe*(0:Ne-1)/Ne;
fo = 1e3 ; fp = fo*ones(1,Ne);
for i =1:Ne
    theta(i) = 2*pi/fe*sum(fp(1:i));
end
x = sin(theta);
figure(1) ;
subplot(211) ; plot(t,x)
title('Signal sinusoïdal')
xlabel('Temps en s'); ylabel('Amplitude en V');
ylim([-1.2 1.2]);
X = 2*abs(fft(x))/Ne ;
subplot(212) ;
plot( f(1 :Ne/2),X(1 :Ne/2));
title('Spectre du signal sinusoïdal')
xlabel('Fréquence en Hz'); ylabel('Amplitude en V');
xlim([-3500 2e5]);
ylim([-0.1 1.2]);





