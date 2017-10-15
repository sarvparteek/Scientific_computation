clear;
clc;

x = -3:3; 
y = [-1 -1 -1 0 1 1 1]; 
xq1 = -3:.01:3;
p = pchip(x,y,xq1);
s = spline(x,y,xq1);
figure(1)
plot(x,y,'o',xq1,p,'-',xq1,s,'-.')
legend('Sample Points','pchip','spline','Location','SouthEast')

x = 0:25;
y = besselj(1,x);
xq2 = 0:0.01:25;
p = pchip(x,y,xq2);
s = spline(x,y,xq2);
figure(2)
plot(x,y,'o',xq2,p,'-',xq2,s,'-.')
legend('Sample Points','pchip','spline')

