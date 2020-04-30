% A vector with all x values for our plotting function
x = 0.0:0.01:1.0;

% The function for each Gaussian
function ret=y(i, h, m, w)
ret = h*exp((-(i-m).^2) / (2*w^2));
endfunction

plot(x, y(x,1.2, 0.52, 0.12),'LineWidth',2)

hold on % To plot all functions on one axis

plot(x, y(x,-1.4, 0.50, 0.07),'LineWidth',2)
plot(x, y(x, 0.30, 0.80, 0.03),'LineWidth',2)

legend("h = 1.20, m = 0.52, w = 0.12", "h = -1.40, m = 0.50, w = 0.07", "h = 0.30, m = 0.80, w = 0.03");

title("Environmental Target Functions")