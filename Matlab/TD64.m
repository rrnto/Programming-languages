

fe=1e3;fp=300 ;fa=500 ;
wp=fp/fe; Rp=0.3 ;
wa=fa/fe ; Ra=80 ;
[N,wn]=buttord(wp,wa,Rp,Ra);
[b,a]=butter(N,wn,'low');
[h,t]=impz(b,a,fe);
figure(6);
title('Allure de la réponse impulsionnelle du filtre');
xlabel('temps en s');
ylabel('Amplitude en V');
plot(t,h);grid on;
[H,w]=freqz(b,a);
figure(7);
title('Allure de la réponse fréquentielle du filtre');
freqzplot(H,w);grid on ;
disp('Ordre du filtre N est:');N
disp('La fréquence de coupure wn du filtre est:');wn
disp(' les coefficients [b,a] du filtre de Butterworth:');b,a