%Author : Nitesh Turagafunction result = generalMoranProcess(trans, popSize, initialDistribution, numIter)%UNTITLED2 Summary of this function goes here%   Detailed explanation goes here A modified Moran processresult = zeros(popSize, numIter);%Samplingstate_counts = mnrnd(popSize, initialDistribution);cumulative_state_counts = [0, cumsum(state_counts)];for state = 1:length(initialDistribution)        result(cumulative_state_counts(state)+1:cumulative_state_counts(state+1))= state;end%for each iteration pick an indifor iter = 2:numIter        individual = randint(1,1,popSize)+1;        next_state = mnrnd(1,trans(...            result(individual, iter-1),:));        next_state = find( next_state );                result(:,iter) = result(:,iter-1);                result(individual,iter) = next_state;end