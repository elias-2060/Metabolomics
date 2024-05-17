import json
import os
import pandas as pd

annotatieFiles: [str] = os.listdir('spectrum_annotaties')
sampleInfoFile: str = 'all_sampleinformation.tsv'

annotaties0: pd.DataFrame = pd.read_csv('spectrum_annotaties/' + annotatieFiles[0], sep='\t')
sampleInfo: pd.DataFrame = pd.read_csv(sampleInfoFile, sep='\t')

info = []

def findSampleInfoByDatasetAccession(datasetAccession: str) -> pd.DataFrame:
    for eeki in range(sampleInfo['ATTRIBUTE_DatasetAccession'].size-1):
        eek = sampleInfo['ATTRIBUTE_DatasetAccession'][eeki]
        if eek == datasetAccession:
            print('hit on ' + str(eeki))
            return sampleInfo.iloc[eeki]

    return sampleInfo[sampleInfo['ATTRIBUTE_DatasetAccession'] == datasetAccession]

print('Starting')
for ann_i in range(annotaties0['full_CCMS_path'].size-1):
    datasetAssession = annotaties0['full_CCMS_path'][ann_i].split('/')[0]
    sampleInfoRow = findSampleInfoByDatasetAccession(datasetAssession)
    info.append(sampleInfoRow)

file = open('info.json', 'w')
file.write(json.dumps(info))

print('oops')
