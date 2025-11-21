clc; clear; close all;
% Ouvrir le fichier
fid = fopen('votes.txt', 'r');

% Lire les données du fichier
a = fscanf(fid, '%c');

% Fermer le fichier
fclose(fid);

disp(a);