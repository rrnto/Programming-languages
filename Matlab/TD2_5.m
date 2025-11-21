
Ne = 1024;
ru = rand(1,Ne) ;
figure(5) ;
%subplot(221) ;
plot(ru);
ylim([-0.09 1.1]); xlim([-25 1100]);
title('Allure temporelle du bruit uniforme')
xlabel('Temps en s'); ylabel('Amplitude en V');
Ru = 2*abs(fft(ru))/Ne;
%subplot(222) ;
figure(6)
plot(Ru);
ylim([-0.04 1.1]); xlim([-25 1100]);
title('Allure fréquentielle du bruit uniforme')
xlabel('Fréquence en Hz'); ylabel('Amplitude en V');
figure(7)
subplot(212); plot(histogram(ru));

