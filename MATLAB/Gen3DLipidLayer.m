%=============================================
%DESQ (Dry Eyes Syndrome Quantifier)
%=============================================
%AUTHOR: Karthika Kamath
%30-06-2017
%Engineering the Eye 5
%SRUJANA Center for Innovation
%---------------------------------------------
%MATLAB Code to Generate 3D Lipid layer 
%from a Image containing Region of interest
%in order to understand the abnormality in 
%the Lipid Layer surface.
%----------------------------------------------
%The resultant Image is attached in the 
%Documentation identified as Fig. 
%----------------------------------------------

close all;clear all;clc;

img=imread('img.jpg'); %Pass Image Path after ROI detection 
figure; imshow(img) %display the image

hsvimage = rgb2hsv(img); %convert to hsv
hsvimage=imresize(hsvimage,0.2); %resize for proper scaling
figure;imshow(hsvimage);

hueimage=hsvimage(:,:,1); %extract the hue values

%blue color pattern projected to 0.91 
%that corresponds to 163.8nm
hueimage(hueimage<0.70 & hueimage>0.60)=0.91; 

%greyish color pattern projected to 0.29 
%that corresponds to 52.2nm
hueimage(hueimage<0.51 & hueimage>0.30)=0.29; 

%brownish color pattern projected to 0.625 
%that corresponds to 112.5nm
hueimage(hueimage<0.20 & hueimage>0.10)=0.625; 

%applied Savitzky-Golay smoothening filter
order = 7;
framelen = 11;
sgf = sgolayfilt(hueimage,order,framelen);

%project the mesh giving the irregular thickness of lipid layer
[X,Y]= meshgrid(1:205,1:154);
Z=sgf;
figure; surf(X,Y,Z)

xlabel('y axis of resized image')
ylabel('x axis of resized image')
zlabel('thickness of lipid layer mapped to 0 to 1 range')
%colormap('hot')%yellow gives highest thickness then orange and least by brown
view([150.5 66]);
grid('on');
hold('all');
screenSize = get(0,'Screensize');
set(gcf, 'Position', screenSize); % Maximize figure

