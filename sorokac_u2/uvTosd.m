function [s, d] = uvTosd(u, v, uk, vk)
    %Convert u, v to oblique aspect
    
    % Compute coordinate differences
    dv = vk - v;
    
    %Latitude
    sarg = sin(u) * sin(uk) + cos(u) * cos(uk) .* cos(dv);
    s = asin(sarg);
    
    %Longitude   
    num = -(sin(dv) .* cos(u));
    denom = cos(u) .* sin(uk) .* cos(dv) - sin(u) .* cos(uk);
    
    d = atan2(num, denom);
end