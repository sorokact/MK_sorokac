function [XC,YC] = continent(file, R, uk, vk, u0, proj)
%Draw continent in selected projection
points = load(file);

%Calculate lat and lon
u = points(:,1) * pi / 180;
v = points(:,2) * pi / 180;

%Convert to oblique aspect
[s,d] = uvTosd(u, v, uk, vk);

%Select positive values
idx = find(s>0.3);
s = s(idx);
d = d(idx);

% Draw in selectedprojection 
[XC, YC] = proj(R, s, d, u0);

end
