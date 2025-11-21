% Define the differential equation: dy/dt = -y
ode = @(t, y) -y;

% Define the time span
tspan = [0 5]; % from t=0 to t=5

% Define the initial condition
y0 = 1; % initial value of y at t=0

% Solve the differential equation using ode45
[t45, y45] = ode45(ode, tspan, y0);

% Solve the same differential equation using ode23
[t23, y23] = ode23(ode, tspan, y0);

% Plot the results
figure;
%plot(t45, y45, 'r-', t23, y23, 'b--', t45, exp(t45));
plot(t45, y45, 'r-', t23, y23, 'b--');
legend('ode45', 'ode23');
xlabel('Time');
ylabel('Solution (y)');
title('Comparison of ode45 and ode23 Solutions');
