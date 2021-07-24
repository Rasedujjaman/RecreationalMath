% %%% This matlab script will generate the heart shape and cupid 
%%% Arrow 

clear all 
close all

%% The parametric equation to generate the heart shape
t = linspace(0, 2*pi, 1000);
x = 16*(sin(t)).^3;
y = 13*cos(t) - 5*cos(2*t) -2*cos(3*t) - cos(4*t);

x = 1.5*(x./(max(abs(x))));
y = 1.5*(y./max(abs(y)));



%% to generate different color for different plot
myColor = {'#F00','#F80','#FF0','#0B0','#00F','#50F','#A0F'};
colororder(fliplr(myColor))

%% The concentric heart
numOfHeart = 7;
step = 1/numOfHeart;
for ii = 1:numOfHeart
    plot(ii*step*x, ii*step*y, 'LineWidth', 2) ,axis square
    hold on
end
hold on




%% The cupid arrow
ta = annotation('arrow', [0.76 0.83], [0.71 0.71]);
ta.Position = [0.25,0.25,0.55,0.55];
ta.LineWidth = 2;
ta.Color  = 'k';
 


%% the title 
txt = 'Beauty of Math';
text(-.8, 1.3, txt,'FontSize',14);
set(gca, 'LineWidth', 2);
set(gca, 'XTick', []);
set(gca, 'YTick', []);
