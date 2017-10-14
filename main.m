clear;
clc;

% Case-1
waypts = [0,0; 2,1; 3,3; 4,2; 5,3];
figureHandles = [1,2,3];
generateTrajectory(waypts,figureHandles)

% Case-2
waypts = [-3,2; -1,0; 0,0; -4,-3; 5,2];
figureHandles = [4,5,6];
generateTrajectory(waypts,figureHandles)