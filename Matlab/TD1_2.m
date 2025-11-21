
%%  Définition des constantes : nombre d’échantillon par symbole, nombre de périodes
Nech = 50 ; Nsymb = 12;
% Nombre total de points, fréquence d’échantillonnage
Ne = Nech*Nsymb ; fe =1e3 ;
% vectorisation du temps et de la fréquence
t = (0 :Ne-1)/fe ; f = fe * ( 1:Ne) /Ne ;

% Ecriture d’un symbole +/- 5V
symb = 5*[ ones(1,Nech/2) -1*ones(1,Nech/2)] ;
% Répétition du symbole pour constituer le signal
x = reshape (symb' * ones (1, Nsymb), [1, Ne]) ;
% Visualisation du signal et son spectre
% Initialisation de l’affichage
figure(3)
% Affichage du signal
%subplot(211) ; plot(t,x) ;
plot(t,x) ;
title( 'Signal rectangulaire') ; xlabel ('temps en s') ; ylabel ('amplitude en V') ;
xlim([0 0.15]); 
ylim([-6 6]);

% Calcul du spectre et affichage
X = 2*abs(fft(x))/Ne;
figure(4)
%subplot(212) ;
plot(f(1 :Ne/2), X(1 :Ne/2))
title ('Spectre du signal rectangulaire');
ylim([-0.5 7])


