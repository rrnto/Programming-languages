
%Voici le listing du signal filtré :
close all,clear all,clc
a=1;T=0.02;rc=0.5;fe=1000;Ne=400;
t=1/fe*(0:Ne-1); f=fe*(0:Ne-1)/Ne ;dsp=0.5 ;
a = 1 ; T=0.02 ; rc = 0.5;
tm = mod(t,T) ;
x1 = a*(tm/T <= rc) ;
ru=rand(1,Ne)*dsp; x=x1+ru; 
fp=300 ;fa=500 ;
wp=fp/fe; Rp=0.3 ;
wa=fa/fe ; Ra=80 ;
[N,wn]=buttord(wp,wa,Rp,Ra);
[b,a]=butter(N,wn,'low');
y=filter(b,a,x);
subplot(211); plot(t,y);
title(' chronogramme du signal filtré'); 
xlabel('temps en s');ylabel('amplitude en V');
Z=2*abs(fft(y))/Ne; 
subplot(212); plot(f,Z);
title('spectre du signal filtré'); xlabel('fréquence en Hz') ;ylabel('Amplitude en V') ;
