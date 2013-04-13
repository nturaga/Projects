function q = ctmm(initState, maxTime)

t = 0;
q = initState; % input connectome

while t < maxTime
    t_min = Inf;
    
    for cell = q.cells;
        index = find(q.cells == cell);        
        for ij = 1:6
            t_ij = (-1/(cell.parameters(ij)))*log(rand);
            
            if t_ij < t_min                
                t_min = t_ij;
                cellChanged = index;
                change = ij;
            end        
        end        
    end

    if change == 1
        q.mitosis(cellChanged);
    elseif change == 2
        q.apoptosis(cellChanged);
    elseif change == 3
        q.migrate(cellChanged);
    elseif change == 4
        q.grow(cellChanged);
    elseif change == 5
        q.prune(cellChanged);
    elseif change == 6
        q.differentiate(cellChanged);
    end
    
    t = t + t_min

end


end