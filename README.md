# TumorMapProject

## Source Data
[BRCA TGCA Data from UCSC Xena](https://xenabrowser.net/datapages/?dataset=TCGA.BRCA.sampleMap/mutation_curated_wustl&host=https://tcga.xenahubs.net)

Contains data from 982 samples.  Focusing on **effect** and **gene** columns.

```{python}
import pandas as pd

brca = pd.read_table('mutation_curated_wustl.txt')

```
