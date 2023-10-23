load("ClassificationLearnerSession.mat");

newDataFile = './EvaluateOnMe.csv';

newData = readtable(newDataFile);

[yfit, scores] = trainedModel.predictFcn(newData);

outFile = 'output.txt';

fileID = fopen(outFile, 'w');

if fileID == -1
    error('Failed to open');
end

yfitCell = cellstr(yfit);

for i = 1:numel(yfitCell)
    fprintf(fileID, '%s\n', yfitCell{i});
end

fclose(fileID);
