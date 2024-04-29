import os
import pandas as pd
import xml.etree.ElementTree as ET
from rdkit import Chem, RDLogger


import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)
warnings.filterwarnings('ignore', category=UserWarning)
RDLogger.DisableLog('rdApp.*')

if not os.path.isfile('fda.csv'):
    # Parse DrugBank XML file.
    ns = '{http://www.drugbank.ca}'
    tree = ET.parse('drugbank_database.xml')
    rows = [(drug.findtext(ns + 'drugbank-id[@primary="true"]'),
             drug.findtext(ns + 'name'),
             '|'.join([group.text for group in
                       drug.findall(f'{ns}groups/{ns}group')]),
             '|'.join([code.get('code') for code in
                       drug.findall(f'{ns}atc-codes/{ns}atc-code')]),
             drug.findtext(f'{ns}calculated-properties/'
                           f'{ns}property[{ns}kind="SMILES"]/{ns}value'),
             drug.findtext(f'{ns}experimental-properties/'
                           f'{ns}property[{ns}kind="logP"]/{ns}value'))
            for drug in tree.getroot()]

    illicit_drugs = (pd.DataFrame(rows, columns=['drugbank_id', 'name',
                                                  'groups', 'atc_codes',
                                                  'smiles', 'logP'])
                     .dropna(subset=['smiles']))
    # Filter on FDA approved drugs.
    approved_drugs = illicit_drugs[illicit_drugs['groups']
                                    .str.contains('illicit')]
    # Only retain drugs with valid and unique SMILES.
    smiles = []
    for drug_smiles in illicit_drugs['smiles']:
        mol = Chem.MolFromSmiles(drug_smiles)
        smiles.append(Chem.MolToSmiles(mol, False)
                      if mol is not None else None)
    illicit_drugs['smiles'] = smiles
    illicit_drugs = (illicit_drugs.dropna(subset=['smiles'])
                      .drop_duplicates('smiles')
                      .reset_index(drop=True))
    illicit_drugs.to_csv('fda.csv', index=False)
else:
    illicit_drugs = pd.read_csv('fda.csv')