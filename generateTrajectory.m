function generateTrajectory(waypts,figureHandles)

%Set of data points
x = waypts(1:end,1);
y = waypts(1:end,2);
n_interpolated_pts = 1000;

%Interpolation techniques: linear, spline, Hermite
x_linear = linspace(x(1),x(end),n_interpolated_pts);
% y_linear = transpose(interp1q(x,y,transpose(x_linear)));
y_linear = interp1(x,y,x_linear,'linear'); % C0 continuity
x_spline = x_linear;
y_spline = interp1(x,y,x_spline,'spline'); % C2 continuity
x_pchip = x_linear;
y_pchip = interp1(x,y,x_pchip,'pchip'); % C1 continuity
x_nearest = x_linear;
y_nearest = interp1(x,y,x_nearest,'nearest'); % Discontinous

figure(figureHandles(1))
plot(x,y,'o',x_linear,y_linear,'-',x_spline,y_spline,'-',...
     x_pchip, y_pchip, '-.',x_nearest, y_nearest, ':','LineWidth',2)
legend('Waypoints','Linear','Cubic Spline','Pchip','Nearest')
xlabel('x')
ylabel('y')
title('Trajectory generated by various interpolation methods')
grid on

% Velocity computation. Assumption: dx/dt = 1. So, in 1 dt,
% the robot moves 1 unit in x. Thus, dy/dt = f'(x).dx/dt = f'(x), 
% where y = f(x)
dx_linear = ones(1,length(x_linear)-1);
dy_linear = deriv(y_linear,1);
dx_spline = ones(1,length(x_spline)-1);
dy_spline = deriv(y_spline,1);
dx_pchip = ones(1,length(x_pchip)-1);
dy_pchip = deriv(y_pchip,1);
dx_nearest = ones(1,length(x_nearest)-1);
dy_nearest = deriv(y_nearest,1);

figure(figureHandles(2))
t_vel = 1:length(dy_linear);
plot(t_vel,dy_linear,'-',t_vel,dy_spline,'-',t_vel,dy_pchip, '-.',...
     t_vel,dy_nearest,':','LineWidth',2)
legend('Linear','Cubic Spline','Pchip','Nearest')
xlabel('t')
ylabel('dy/dt')
title('Velocity of trajectory generated by various interpolation methods')
grid on

% Acceleration computation.
ddx_linear = ones(1,length(dx_linear)-1);
ddy_linear = deriv(dy_linear,1);
ddx_spline = ones(1,length(dx_spline)-1);
ddy_spline = deriv(dy_spline,1);
ddx_pchip = ones(1,length(dx_pchip)-1);
ddy_pchip = deriv(dy_pchip,1);
ddx_nearest = ones(1,length(dx_nearest)-1);
ddy_nearest = deriv(dx_nearest,1);

figure(figureHandles(3))
t_accel = 1:length(ddy_linear);
plot(t_accel,ddy_linear,'-',t_accel,ddy_spline,'-',t_accel,ddy_pchip,'-.',...
    t_accel,ddy_nearest,':','LineWidth',2)
legend('Linear','Cubic spline','Pchip','Nearest')
xlabel('t')
ylabel('d2y/dt2')
title('Acceleration of trajectory generated by various interpolation methods')
grid on
end
