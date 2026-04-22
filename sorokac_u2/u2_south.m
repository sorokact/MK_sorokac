clc
clear
format long g

% Parameters
proj = @gnom;
u0 = 0;
Du = 10 * pi/180;
Dv = Du;
du = pi/180;
dv = du;
steps = [Du, Dv, du, dv];
M = 50000000;
R = 6380 * 1000;
R = R / M;

% Paths to continents
conts = { '/MATLAB Drive/matkarto/uloha_2/sorokac_u2/eur.txt',  ...
          '/MATLAB Drive/matkarto/uloha_2/sorokac_u2/austr.txt', ...
          '/MATLAB Drive/matkarto/uloha_2/sorokac_u2/anta.txt', ...
          '/MATLAB Drive/matkarto/uloha_2/sorokac_u2/amer.txt'};

% Boundary points
alpha_n = 26.5651 * pi/180;
alpha_s = -alpha_n;
gamma_n = 52.6226 * pi/180;
gamma_s = -gamma_n;
delta_n = 10.8123 * pi/180;
delta_s = -delta_n;

% SOUTHERN HEMISPHERE

% Face 1
% subplot(2, 3, 1);
figure (1)
uk = alpha_s; 
vk = 36 * pi/180;
uv = [-70*pi/180, 20*pi/180, -10*pi/180, 80*pi/180];

% Boundary points (corrected variables)
ub = [delta_s, gamma_s, gamma_s, delta_s, delta_n, delta_s];
vb = [0, 0, 72*pi/180, 72*pi/180, 36*pi/180, 0];

% Globe face
GlobeFace(uv, steps, R, uk, vk, u0, proj, conts, ub, vb);

% Face 2
% subplot(2, 3, 2);
figure (2)
uk = alpha_s; 
vk = 108 * pi/180;
uv = [-70*pi/180, 20*pi/180, 60*pi/180, 150*pi/180];

% Boundary points
ub = [delta_s, gamma_s, gamma_s, delta_s, delta_n, delta_s];
vb = [72*pi/180, 72*pi/180, 144*pi/180, 144*pi/180, 108*pi/180, 72*pi/180];

% Globe face
GlobeFace(uv, steps, R, uk, vk, u0, proj, conts, ub, vb);

% Face 3
% subplot(2, 3, 3);
figure (3)
uk = alpha_s; 
vk = pi;
uv = [-70*pi/180, 20*pi/180, 130*pi/180, 230*pi/180];

% Boundary points
ub = [delta_s, gamma_s, gamma_s, delta_s, delta_n, delta_s];
vb = [144*pi/180, 144*pi/180, 216*pi/180, 216*pi/180, pi, 144*pi/180];

% Globe face
GlobeFace(uv, steps, R, uk, vk, u0, proj, conts, ub, vb);

% Face 4
% subplot(2, 3, 4);
figure (4)
uk = alpha_s; 
vk = 252 * pi/180;
uv = [-70*pi/180, 20*pi/180, 200*pi/180, 300*pi/180];

% Boundary points
ub = [delta_s, gamma_s, gamma_s, delta_s, delta_n, delta_s];
vb = [216*pi/180, 216*pi/180, 288*pi/180, 288*pi/180, 252*pi/180, 216*pi/180];

% Globe face
GlobeFace(uv, steps, R, uk, vk, u0, proj, conts, ub, vb);

% Face 5
% subplot(2, 3, 5);
figure (5)
uk = alpha_s; 
vk = 324 * pi/180;
uv = [-70*pi/180, 20*pi/180, 270*pi/180, 370*pi/180];

% Boundary points
ub = [delta_s, gamma_s, gamma_s, delta_s, delta_n, delta_s];
vb = [288*pi/180, 288*pi/180, 2*pi, 2*pi, 324*pi/180, 288*pi/180];

% Globe face
GlobeFace(uv, steps, R, uk, vk, u0, proj, conts, ub, vb);

% Face 6
% subplot(2, 3, 6);
figure (6)
uk = -pi/2;
vk = 0;
uv = [-pi/2, -40*pi/180, -pi, pi];

% Boundary points
ub = [gamma_s, gamma_s, gamma_s, gamma_s, gamma_s, gamma_s];
vb = [0, 72*pi/180, 144*pi/180, 216*pi/180, 288*pi/180, 0];

% Globe face
GlobeFace(uv, steps, R, uk, vk, u0, proj, conts, ub, vb);