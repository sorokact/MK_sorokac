clc
clear
format long g

%Parameters
proj = @gnom;
s0 = 0;
Du = 10 * pi/180;
Dv = Du;
du = pi/180;
dv = du;
steps = [Du, Dv, du, dv];

M = 50000000;
R = 6380 * 1000;
R = R / M;

%Paths to continents
conts = { '/MATLAB Drive/matkarto/uloha_2/sorokac_u2/eur.txt',  ...
          '/MATLAB Drive/matkarto/uloha_2/sorokac_u2/austr.txt', ...
          '/MATLAB Drive/matkarto/uloha_2/sorokac_u2/anta.txt', ...
          '/MATLAB Drive/matkarto/uloha_2/sorokac_u2/amer.txt'};

%Boundary points
alpha_n = 26.5651 * pi/180;
alpha_s = - alpha_n;
gamma_n = 52.6226 * pi/180;
gamma_s = - gamma_n;
delta_n = 10.8123 * pi/180;
delta_s = - delta_n;

%NORTHERN HEMISPHERE

%Face 1
% subplot(2, 3, 1);
figure (1)
uk = pi/2; 
vk = 0;
uv = [40*pi/180, pi/2, -pi, pi];

%Boundary points
ub = [gamma_n, gamma_n, gamma_n, gamma_n, gamma_n, gamma_n];
vb = [36*pi/180, 108*pi/180, pi, 252*pi/180, 324*pi/180, 36*pi/180];

%Globe face
GlobeFace(uv, steps, R, uk, vk, s0, proj, conts, ub, vb);

%Face 2
% subplot(2, 3, 2);
figure (2)
uk = alpha_n; vk = 0;
uv = [-20*pi/180, 70*pi/180, -40*pi/180, 40*pi/180];

%Boundary points
ub = [delta_s, delta_n, gamma_n, gamma_n, delta_n, delta_s];
vb = [0, 36*pi/180, 36*pi/180, 324*pi/180, 324*pi/180, 0];

%Globe face
GlobeFace(uv, steps, R, uk, vk, s0, proj, conts, ub, vb);


%Face 3
% subplot(2, 3, 3);
figure (3)
uk = alpha_n; vk = 72*pi/180;
uv = [-20*pi/180, 70*pi/180, 30*pi/180, 120*pi/180];

%Boundary points
ub = [delta_s, delta_n, gamma_n, gamma_n, delta_n, delta_s];
vb = [72*pi/180, 108*pi/180, 108*pi/180, 36*pi/180, 36*pi/180, 72*pi/180];

%Globe face
GlobeFace(uv, steps, R, uk, vk, s0, proj, conts, ub, vb);

%Face 4
% subplot(2, 3, 4);
figure (4)
uk = alpha_n; vk = 144*pi/180;
uv = [-20*pi/180, 70*pi/180, 100*pi/180, 190*pi/180];

%Boundary points
ub = [delta_s, delta_n, gamma_n, gamma_n, delta_n, delta_s];
vb = [144*pi/180, pi, pi, 108*pi/180, 108*pi/180, 144*pi/180];

%Globe face
GlobeFace(uv, steps, R, uk, vk, s0, proj, conts, ub, vb);

%Face 5
% subplot(2, 3, 5);
figure (5)
uk = alpha_n; vk = 216*pi/180;
uv = [-20*pi/180, 70*pi/180, 170*pi/180, 260*pi/180];

%Boundary points
ub = [delta_s, delta_n, gamma_n, gamma_n, delta_n, delta_s];
vb = [216*pi/180, 252*pi/180, 252*pi/180, pi, pi, 216*pi/180];

%Globe face
GlobeFace(uv, steps, R, uk, vk, s0, proj, conts, ub, vb);

%Face 6
% subplot(2, 3, 6);
figure (6)
uk = alpha_n; vk = 288*pi/180;
uv = [-20*pi/180, 70*pi/180, 240*pi/180, 330*pi/180];

%Boundary points
ub = [delta_s, delta_n, gamma_n, gamma_n, delta_n, delta_s];
vb = [288*pi/180, 324*pi/180, 324*pi/180, 252*pi/180, 252*pi/180, 288*pi/180];

%Globe face
GlobeFace(uv, steps, R, uk, vk, s0, proj, conts, ub, vb);