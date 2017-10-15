clear;
clc;

x = 1:1000;
y = sin(x);
xt = 1:0.01:1000;

times = zeros(4,1);

tic
for i = 1:1000
    yn = interp1(x,y,xt,'nearest');
end
times(1) = toc;

tic
for i = 1:1000
    yl = interp1(x,y,xt,'linear');
end
times(2) = toc;

tic
for i = 1:1000
    yp = interp1(x,y,xt,'pchip');
end
times(3) = toc;

tic
for i = 1:1000
    ys = interp1(x,y,xt,'spline');
end
times(4) = toc;

times