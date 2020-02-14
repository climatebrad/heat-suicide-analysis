# A Statistical Analysis of the Relationship Between Heat and Suicide Rates in the U.S.
This project is a part of the Flatiron School Data Science Fellowship requirements.

## Project Objective
The purpose of this project is to examine whether unusual rise in temperature increases suicide rates.

### Collaborators
* Brad Johnson
  * [Github](https://github.com/climatebrad)
* Seoho Hahm
  * [Github](https://github.com/seoho926)

### Methods Used
* paired sample t-test
* independent sample t-test

### Technologies
* Python
  * Scipy Stats
  * Matplotlib/Seaborn
  * Pandas
  * Numpy
  * Statsmodels

## Project Description
This project tests the following hypotheses with t-tests
  * Ha: Suicide rates are higher in the winter than in the summer (paired)
  * Ha: Suicide rates during unusually hot summer months are higher than the other summer months (independent)

## Featured Notebooks/Analysis/Deliverables
* [notebooks/MASTER.ipynb](notebooks/MASTER.ipynb)
* [Heat & Suicide.pdf](https://github.com/climatebrad/heat-suicide-analysis/blob/master/Heat%20%26%20Suicide.pdf)

## Sources

### Suicides:
Reference: [Multiple Cause of Death 1999 - 2017](https://wonder.cdc.gov/wonder/help/mcd.html)

To acquire raw suicide data:
* go to [About Multiple Cause of Death, 1999-2017](https://wonder.cdc.gov/mcd-icd10.html)
* click "I Agree"
* In _1. Organize table layout:_
  * Group Results By: State, Year, Month
* In _3. Select demographics:_
  * exclude Ten-Year Age Groups _Not stated_; exclude Hispanic Origin _Not stated_
* In _6. Underlying cause of death:_ 
  * select _X60-X84 (Intentional self-harm)_
* In _8. Other options:_
  * select _Export Results_
  * deselect _Show Totals_
* click "Send"

### Temperatures & Heat Index:
Reference [North America Land Data Assimilation System (NLDAS) Daily Air Temperatures and Heat Index 1979 - 2011](https://wonder.cdc.gov/wonder/help/nldas.html)

To acquire raw temperature data:
* Go to [North America Land Data Assimilation System (NLDAS) Daily Air Temperatures and Heat Index (1979-2011) Request](https://wonder.cdc.gov/nasa-nldas.html)
* In _1. Organize table layout:_
  * Group results by State, Year, Month
* In _5. Other options:_
  * select _Export Results_
  * deselect _Show Totals_
* click "Send"
  


