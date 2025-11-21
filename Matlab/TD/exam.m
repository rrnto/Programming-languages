clc; clear; close all;

%%%2 Programme matlab pour résoudre cette équation matricielle

x1 = 1; y1 = 2; x2 = 3.5; y2 = 1; x3 = 5; y3 = 4; R1 = 1.94; R2 = 1; R3 = 3;
a = 2 * (x3 - x1);
b = 2 * (y3 - y1);
c = 2 * (x3 - x2);
d = 2 * (y3 - y2);

B1 = R1^2 - R3^2 + x3^2 - x1^2 + y3^2 - y1^2;
B2 = R2^2 - R3^2 + x3^2 - x2^2 + y3^2 - y2^2;

A = [a, b; c, d]; B = [B1; B2];
X = inv(A)* B;

disp(['xI= ',num2str(X(1))]);
disp(['yI= ',num2str(X(2))]);

%%%3 Representation des centres ainsi que le point I
xI=X(1); yI=X(2);
plot(x1,y1, '*b'); hold on;
plot(x2,y2, '*y');
plot(x3,y3, '*g');
plot(xI,yI, '*r');
legend('R1', 'R2', 'R3', 'I', 'Location', 'best');
xlim('auto'); ylim('auto');

%%%4 Traçage des trois cerles
t=0:pi/500:2*pi;
x = x1 + R1*cos(t);
y = y1 + R1*sin(t);
plot(x,y,'-b');

xx = x2 + R2*cos(t);
yy = y2 + R2*sin(t);
plot(xx,yy,'-y');

xxx = x3 + R3*cos(t);
yyy = y3 + R3*sin(t);
plot(xxx,yyy,'-g');
