import pandas as pd
from pyECLAT import ECLAT


def unGroupApproval(data: pd.DataFrame) -> pd.DataFrame:
    data['approved'] = data['groups'].apply(lambda x: 'approved' if 'approved' in x else 'not approved')
    data['illicit'] = data['groups'].apply(lambda x: 'illicit' if 'illicit' in x else 'not illicit')
    data['investigational'] = data['groups'].apply(lambda x: 'investigational' if 'investigational' in x else 'not investigational')
    data['withdrawn'] = data['groups'].apply(lambda x: 'withdrawn' if 'withdrawn' in x else 'not withdrawn')
    data['experimental'] = data['groups'].apply(lambda x: 'experimental' if 'experimental' in x else 'not experimental')
    data['vet_approved'] = data['groups'].apply(lambda x: 'vet_approved' if 'vet_approved' in x else 'not vet_approved')
    data['nutraceutical'] = data['groups'].apply(lambda x: 'nutraceutical' if 'nutraceutical' in x else 'not nutraceutical')
    data['informal'] = data['groups'].apply(lambda x: 'informal' if 'informal' in x else 'not informal')
    data.drop(columns=['groups'], inplace=True)
    return data


def dropUselessColumns(data: pd.DataFrame) -> pd.DataFrame:
    data.drop(columns=['drugbank_id',
                       'atc_codes',
                       'smiles',
                       'logP',
                       'inchikey',
                       'filename',
                       'ChromatographyAndPhase',
                       'ATTRIBUTE_DatasetAccession',
                       'DOIDOntologyIndex',
                       'DepthorAltitudeMeters',
                       'LatitudeandLongitude',
                       'AgeInYears',
                       'SampleCollectionDateandTime',
                       'SampleType',
                       'SubjectIdentifierAsRecorded',
                       'TermsofPosition',
                       'UBERONOntologyIndex',
                       'UniqueSubjectID',
                       'rowid',
                       'ccms_row_id',
                       'SpectrumID',
                       'PI',
                       'Data_Collector',
                       'Adduct',
                       'Precursor_MZ',
                       'ExactMass',
                       'Charge',
                       'CAS_Number',
                       'Pubmed_ID',
                       'smiles',
                       'INCHI',
                       'INCHI_AUX',
                       'Library_Class',
                       'IonMode',
                       'UpdateWorkflowName',
                       'LibraryQualityString',
                       '#Scan#',
                       'SpectrumFile',
                       'MQScore',
                       'Organism', #maybe
                       'TIC_Query',
                       'RT_Query',
                       'MZErrorPPM',
                       'SharedPeaks', #maybe
                       'MassDiff',
                       'LibMZ',
                       'SpecMZ',
                       'SpecCharge',
                       'FileScanUniqueID',
                       'NumberHits',
                       'full_CCMS_path',
                       'tags', #maybe
                       'MoleculeExplorerDatasets',
                       'MoleculeExplorerFiles',
                       'InChIKey',
                       'InChIKey-Planar',
                       'npclassifier_superclass',
                       'npclassifier_pathway',
                       'internalFilename',
                       'Smiles',
                       'NCBITaxonomy',
                       'UBERONBodyPartName',
                       'class',
                       'subclass',
                       'superclass',
                       'npclassifier_class',
                       'YearOfAnalysis',
                       'LibraryName',
                       'ComorbidityListDOIDIndex'
                       ], inplace=True)
    return data

if __name__ == "__main__":
    data: pd.DataFrame = pd.read_csv('join/finaloutput.tsv', sep='\\t', engine='python')
    data = unGroupApproval(data)
    data = dropUselessColumns(data)
    data = pd.DataFrame(data.values)
    data = data.map(str)

    eclat_inst = ECLAT(data, verbose=True)
    get_idk, get_eclat = eclat_inst.fit(min_support=0.08, min_combination=2, max_combination=2, verbose=True)
    open('ECLAT.txt', 'w').write(str(get_eclat))


