function dy = deriv(y,k)
% y = f(x). So, y' = f'(x). (dx/dt)
%                  = (dy/dx). (dx/dt)
%                  = (dy).(1/dx).(dx/dt)
%                  = (dy).k
dy = zeros(1,length(y)-1);    
for i = 1:length(y)-1
        dy(i) = (y(i+1) - y(i))*k;
end
end

        