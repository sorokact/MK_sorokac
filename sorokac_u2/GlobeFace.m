function [] = GlobeFace(uv, steps, R, uk, vk, u0, proj, conts, ub, vb)
hold on;
axis equal
xlim([-1.2*R, 1.2*R]);
ylim([-1.2*R, 1.2*R]);

% umin, umax, vmin, vmax = uv
% Du, Dv, du, dv = steps
% c1, c2, c3, c4 = cont (continents)

% Extract coordinates and step sizes
umin = uv(1,1);
umax = uv(1,2);
vmin = uv(1,3);
vmax = uv(1,4);

Du = steps(1,1);
Dv = steps(1,2);
du = steps(1,3);
dv = steps(1,4);

% Draw background
backgroundColor = [0.15, 0.60, 0.83];
fill([-2*R, 2*R, 2*R, -2*R], [-2*R, -2*R, 2*R, 2*R], backgroundColor, 'EdgeColor', 'none', 'FaceAlpha', 0.15);

% Draw continents
for i = 1:length(conts)
    [XC, YC] = continent(conts{i}, R, uk, vk, u0, proj);
    landColor = [0.46, 0.67, 0.18];
    edgeColor = [0.1, 0.2, 0.05]
    transpValue = 0.35
    fill(XC, YC, landColor, 'EdgeColor', edgeColor, 'LineWidth', 0.35, 'FaceAlpha', transpValue);
end

% Draw boundary
[XB, YB] = boundary(R, uk, vk, u0, proj, ub, vb);

% Create graticule
[XM, YM, XP, YP] = graticule(umin, umax, vmin, vmax, Du, Dv, du, dv, R, uk, vk, u0, proj);

% Draw graticule
hold on;
axis equal;
plot(XM', YM', 'k');
plot(XP', YP', 'k');
plot(XB, YB, 'r', 'LineWidth', 3);

end