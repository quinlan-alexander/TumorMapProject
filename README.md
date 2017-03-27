# TumorMapProject

## Source Data
[BRCA TGCA Data from UCSC Xena](BRCA TGCA Data from UCSC Xena)

Contains data from 982 samples.  Focusing on **effect** and **gene** columns.

```{python}
import pandas as pd

brca = pd.read_table('mutation_curated_wustl.txt')

```
