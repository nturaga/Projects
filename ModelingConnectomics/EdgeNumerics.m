function [sum, num] = EdgeNumerics(cm)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
sum = 0;
num = 0;
for i = cm.cells
    for j = i.to
        num = num +1;
        sum = sum + sqrt((i.position(1)-j.position(1))^2 + (i.position(2)-j.position(2))^2);
    end
end

end

