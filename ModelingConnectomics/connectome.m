classdef connectome < handle
    %CONNECTOME Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        cells = []; % list of "cell" class
        dimensions = []; % size of simulation space
        gradient = []; % matrix defining the conc of chem signaling gradient
        idSoFar = 0;
        
        D = [     0, (2/3), (1/3),    0,    0,    0;
                  0,     0,     0,  0.5,  0.5,    0;
                  0,     0,     0,    0,    0,    1;
                  0,     0,     0,    1,    0,    0;
                  0,     0,     0,    0,    1,    0;
                  0,     0,     0,    0,    0,    1];
          
%         P = [     2,     2,     2,    0,    0,    0;
%                   1,     1,     1,    0,    0,    0;
%                   0,     2,     2,    0,    0,    1;
%                   0,     0,     0,    0,    1,    1;
%                   0,     0,     0,    0,    0,    0;
%                   1,     1,     1,    0,    0,    0];
%               
        B = [   1/2,     0,     0,    0,    0,    0;
                1/4,   1/4,     0,    0,  1/4,    0;
                  0,     0,   1/2,  1/4,    0,  1/2;
                  0,     0,   1/4,    0,  1/4,  1/2;
                  0,   1/4,     0,  1/4,    0,  1/4;
                1/4,   1/2,   1/2,  1/2,  1/2,  1/2];
              
          P = ones(6,6);

        M = [     0,     5,     5,    0,    0,    1;
                  0,     0,     0,    2,    2,    1];
        
    end

    properties (Dependent = true)
        numberCells % number of cells in connectome
        cellBinCount % histogram of cells in each dimension
        
    end
    
    methods
        % initialize method
        function c = connectome(cells,dimensions)
            c.cells = cells;
            c.dimensions = dimensions;
        end
        
        % maintenance methods
        function addNode(obj, position, type)
            obj.cells = [obj.cells node(position, obj.P(:,type), type, obj.idSoFar + 1)];
            obj.idSoFar = obj.idSoFar + 1;
        end
        function number = get.numberCells(obj)
            number = length(obj.cells);
        end
        function hists = get.cellBinCount(obj)
            hists = zeros(obj.dimensions);
            for c = 1:length(obj.cells)
                for d = 1:length(obj.dimensions)
                    bin = ceil(obj.cells(c).position(d));
                    hists(d, bin) = hists(d,bin) + 1;
                end
            end
        end
        function updateParameters(obj,index)
            obj.cells(index).parameters = obj.B * obj.cells(index).parameters;
        end
        
        % transition operations: mitosis, apoptosis, migrate,
        %                        grow, prune, differentiate
        function obj = apoptosis(obj, index)
            apoptoticCell = obj.cells(index);
            for i = 1:length(obj.cells)
                obj.cells(i).remTo(apoptoticCell);
                obj.cells(i).remFrom(apoptoticCell);
            end
            obj.cells(ismember(obj.cells,obj.cells(index))) = [];
        end
        
        function obj = mitosis(obj, index)
            newCell = node(obj.cells(index).position, obj.cells(index).parameters, obj.cells(index).type, obj.idSoFar + 1);
            obj.cells = [obj.cells newCell];
            obj.idSoFar = obj.idSoFar + 1;
        end
        
        function obj = migrate(obj, index)            
            direction = obj.M(:,obj.cells(index).type)';
            for i = 1:length(direction)                
                direction(i) = direction(i) + 2*rand - 1;
            end
            obj.cells(index).move(direction,obj.dimensions);
        end
        
        function obj = grow(obj, index)
            here = round(obj.cells(index).position);
            exp_min = Inf;
            connect = [];
            for to = 1:length(obj.cells)
                there = round(obj.cells(to).position);
                distance = norm(there - here) + 1;
                likely = exprnd(distance);
                if likely < exp_min
                    connect = to;                    
                end                
            end
            obj.cells(index).addTo(obj.cells(to));
        end
        
        function obj = prune(obj,index)
            randomAxon = ceil(rand*length(obj.cells(index).to));
            obj.cells(index).remTo(randomAxon);
        end
        
        function obj = differentiate(obj,index)
            switch (obj.cells(index).type)
                case 1
                    if rand < .5
                        obj.cells(index).type = 2;
                        obj.cells(index).parameters = obj.P(:,2);
                    else
                        obj.cells(index).type = 3;
                        obj.cells(index).parameters = obj.P(:,3);
                    end
                 case 2
                    if rand < .5
                        obj.cells(index).type = 4;
                        obj.cells(index).parameters = obj.P(:,4);
                    else
                        obj.cells(index).type = 5;
                        obj.cells(index).parameters = obj.P(:,5);
                    end
                 case 3
                        obj.cells(index).type = 6;
                        obj.cells(index).parameters = obj.P(:,6);
            end
            
        end
                
    end
    
end