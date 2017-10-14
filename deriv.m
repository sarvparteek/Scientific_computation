function dy = deriv(y,k)
dy = zeros(1,length(y)-1);    
for i = 1:length(y)-1
        dy(i) = (y(i+1) - y(i))*k;
end

        