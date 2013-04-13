clear all

initial = connectome([],[100, 100]);


for spacing = 1:49
    initial.addNode([1,spacing*2], 1);
end

final = ctmm(initial,5);

initial2 = connectome([],[100, 100]);

for spacing = 1:49
    initial2.addNode([1,spacing*2], 1);
end

final2 = ctmm(initial2,5);

GraphConnectome(final)
GraphConnectome(final2)
GraphConnectome(final3)