classdef node < handle
    %NODE Summary of this class goes here
    %   Detailed explanation goes here
    
    properties
        to = []; % list of nodes connects to
        from = []; % list of nodes connects from
        position = []; % position of cell in space
        axons = []; % list of coordinates of axonal processes
        parameters = []; % nx1 array of gene expression values
        id = 0;
        idSoFar = 0;
        type = 0;
    end
    
    properties (Dependent = true)
        numNeighbors % number of connected neighbors
        numProcesses % number of processes
        l_mitosis
        l_apoptosis
        l_migration
        l_grow
        l_prune
        l_differentiation

    end
    
    methods
        % METHODS THAT ASSIGN PROPERTIES
        function n = node(initialPosition, parameters, type, id) % initialize
            n.position = initialPosition;
            n.parameters = parameters;
            n.type = type;
            n.id = id;
        end
        function move(obj,vector, dimensions) % move cell
            obj.position = obj.position + vector;
            obj.position = min(obj.position,dimensions);
            obj.position = max(zeros(size(dimensions)),obj.position);
        end
        function addAxon(obj,position) % add axonal process
            obj.axons = [obj.axons; position];
        end
        function remAxon(obj,index)
            obj.axons(index) = [];
        end
        function addTo(obj,node) % add to downstream adjacency list
            if sum(find(obj.to == node)) == 0
                obj.to = [obj.to node];
                node.addFrom(obj);
            end
        end
        function addFrom(obj,node) % add to upstream adjacency list
            if sum(find(obj.from == node)) == 0
                obj.from = [obj.from node];
                node.addTo(obj);
            end
        end
        function remTo(obj,node) % remove from downstream adjacency list
            if sum(find(obj.to == node)) == 0
                obj.to(ismember(obj.to,node)) = [];
            end
        end
        function remFrom(obj,node) % remove from upstream adjacency list
            if sum(find(obj.from == node)) == 0
                obj.from(ismember(obj.from,node)) = [];
            end
        end
        function updateGenes(obj,node,B) % update genes
            obj.genes = B * obj.genes;
        end
        
        % get methods
        function number = get.numNeighbors(obj) % get the number neighbors
            number = length(obj.to) + length(obj.from);
        end
        function number = get.numProcesses(obj)
            number = length(obj.axons);
        end
        function lambda = get.l_mitosis(obj)
            lambda = obj.parameters(1);
        end
        function lambda = get.l_apoptosis(obj)
            lambda = obj.parameters(2);
        end
        function lambda = get.l_migration(obj)
            lambda = obj.parameters(3);
        end
        function lambda = get.l_grow(obj)
            lambda = obj.parameters(4);
        end
        function lambda = get.l_prune(obj)
            lambda = obj.parameters(5);
        end
        function lambda = get.l_differentiation(obj)
            lambda = obj.parameters(6);
        end
        
    end
    
end