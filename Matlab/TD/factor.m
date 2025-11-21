% Fonction pour calculer factorielle de n
function fact = factor(n)
    if n == 0
        fact = 1;
    else
        fact = n * factor(n - 1);
    end
end