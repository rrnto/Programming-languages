

Ne = 1000 ; fe = 10000 ; F = 100; a= 5 ;
t = (1:Ne)/fe ;
%t = (0:1);
x = a*sin(2*pi*F*t);
figure (1)
plot (t,x) ; title ('Signal sinusoïdal')
xlabel('temps en s') ; ylabel('amplitude en V');
%xlim([-500 10500]); 
ylim([-5.5 5.5]);

f = fe * ( 1:Ne) /Ne ;
X = fft (x) ; aX = 2*abs(X)/Ne;
figure (2)
plot(f,aX) ; title ('Spectre du signal sinusoïdal');
xlabel('Fréquence Hz'); ylabel('Amplitude V');
xlim([-135 10135]); ylim([-0.5 5.5]);

