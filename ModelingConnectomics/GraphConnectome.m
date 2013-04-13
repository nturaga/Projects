function [] = GraphConnectome(cm, title)
%GRAPHCONNECTOME Graphs the connectome. each node is a blue asterisk
%each edge is a red line. title is the title of the graph.
figure
size = length(cm.cells);
axis([0,cm.dimensions(1),0,cm.dimensions(2)]);
hold all;


for t = cm.cells()
    for i = t.to()
        plot([t.position(1),i.position(1)],[t.position(2),i.position(2)],'r')
    end
end

for t = cm.cells
    plot(t.position(1),t.position(2),'b*')
end
% title(title);