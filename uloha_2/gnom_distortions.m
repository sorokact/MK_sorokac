clc
clear
format long g

% Define symbolic variables
syms R u v

% Projection equations
x = R*tan(pi/2 - u)*cos(v);
y = R*tan(pi/2 - u)*sin(v);

% Partial derivatives
fu = diff(x, u);
fv = diff(x, v);
gu = diff(y, u);
gv = diff(y, v);

% Simplify equations with varying intensities
fu = simplify(fu, 'Steps', 30);
gu = simplify(gu, 'Steps', 30);
fv = simplify(fv, 'Steps', 30);
gv = simplify(gv, 'Steps', 30);

% Local linear scale
mp2 = (fu^2 + gu^2)/R^2;
mp2 = simplify(mp2, 'Steps', 30);
mr2 = (fv^2 + gv^2)/(R^2 * cos(u)^2);
mr2 = simplify(mr2); 

% Meridian/Parallel intersection parameter
p = 2*(fu*fv + gu*gv);

% Angle between meridian and parallel
omega = atan2((gu*fv - fu*gv), (fu*fv + gu*gv));
omega = simplify(omega, 'Steps', 20);

% Area scale
P = (gu*fv - fu*gv)/(R^2 * cos(u));
P = simplify(P, 'Steps', 40);

% Meridian convergence
f_ratio = gu/fu;
sigma = atan(simplify(f_ratio, 'Steps', 20));
conv = pi/2 - sigma;

% Extreme azimuths
A = 0.5 * atan2(p, (mp2 - mr2));
A = simplify(A, 'Steps', 30);

% Numeric computations
un = 52.6226 * pi/180;
vn = 36 * pi/180;
Rn = 6380 * 1000 / 1000000;

% Coordinates
xn = double(subs(x, {R, u, v}, {Rn, un, vn}));
yn = double(subs(y, {R, u, v}, {Rn, un, vn}));

% Local linear scales
mpn = sqrt(double(subs(mp2, {R, u, v}, {Rn, un, vn})))
mrn = sqrt(double(subs(mr2, {R, u, v}, {Rn, un, vn})))
pn = double(subs(p, {R, u, v}, {Rn, un, vn}))

% Extreme azimuth for the point
A1ne = double(subs(A, {R, u, v}, {Rn, un, vn}));
A2ne = A1ne + pi/2;

% Scale in extreme directions (semi-axes a, b)
calc_M = @(az) sqrt(mpn^2 * cos(az)^2 + mrn^2 * sin(az)^2 + pn * sin(az) * cos(az));
an = calc_M(A1ne);
bn = calc_M(A2ne);

% Maximum angular distortion
mad_deg = (2 * asin(abs(an - bn) / (an + bn))) * 180/pi;

% Tissot ellipse preparation
sigman = double(subs(sigma, {R, u, v}, {Rn, un, vn}));
[xt, yt] = build_tissot(an, bn, xn, yn, sigman - A1ne);

%Graticule
umin = -pi/2;
umax = -40*pi/180;
vmin = -pi;
vmax = pi;
Du = 10 * pi/180; Dv = Du;
du = pi/180; dv = du;
uk = pi/2; vk = 0;
proj = @gnom;
u0 = 0;

% Create and Plot graticule
[XM, YM, XP, YP] = graticule(umin, umax, vmin, vmax, Du, Dv, du, dv, Rn, uk, vk, u0, proj);

hold on;
plot(XM', YM', 'k');
plot(XP', YP', 'k');

% Plotting the Tissot indicatrix in red
plot(xt, yt, 'r', 'LineWidth', 1.5);
axis equal;
grid on;

function [tx, ty] = build_tissot(a, b, offset_x, offset_y, angle)
    % Generate and transform ellipse points
    t = linspace(0, 2*pi, 100);
    % Scaling and rotation logic
    base_x = a * cos(t);
    base_y = b * sin(t);
    
    tx = offset_x + base_x*cos(angle) - base_y*sin(angle);
    ty = offset_y + base_x*sin(angle) + base_y*cos(angle);
end