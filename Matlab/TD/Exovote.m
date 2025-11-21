clc; clear; close all;

%%PROGRAMME DE COMPTAGE DE VOTE

% Ouvrir le fichier
fid = fopen('votes.txt', 'r');

% Lire les données du fichier
Vote = fscanf(fid, '%f');

% Fermer le fichier
fclose(fid);
%Vote = [1 3 3 2 3 1 3 2 1 3]

% Initialisation des compteurs
nb_votes_1 = 0;
nb_votes_2 = 0;
nb_votes_3 = 0;

% Compter les votes pour chaque option
for i = 1:length(Vote)
    if Vote(i) == 1
        nb_votes_1 = nb_votes_1 + 1;
    elseif Vote(i) == 2
        nb_votes_2 = nb_votes_2 + 1;
    elseif Vote(i) == 3
        nb_votes_3 = nb_votes_3 + 1;
    end
end

% Afficher les résultats
fprintf('Nombre de votes pour option 1 : %d\n', nb_votes_1);
fprintf('Nombre de votes pour option 2 : %d\n', nb_votes_2);
fprintf('Nombre de votes pour option 3 : %d\n', nb_votes_3);
