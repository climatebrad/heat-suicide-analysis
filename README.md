# A Statistical Analysis of the Relationship Between Heat and Suicide Rates in the U.S.
This project is a part of the Flatiron School Data Science Fellowship requirements.

## Project Objective
The purpose of this project is to examine whether unusual rise in temperature increases suicide rates.

### Collaborators
* Brad Johnson
  * Github (https://github.com/climatebrad)
* Seoho Hahm
  * Github (https://github.com/seoho926)

### Methods Used
* paired sample t-test
* independent sample t-test

### Technologies
* Python
  * Scipy Stats
  * Matplotlib/Seaborn
  * Pandas
  * Numpy
  * Sklearn

## Project Description
This project tests the following hypotheses with t-tests
  * Ho: Suicide rates are higher in the winter than in the summer (paired)
  * Ho: Suicide rates during unusually hot summer months are the same as the other summer months (independent)

## Sources
* Suicides:
  * `suicides.txt` from https://wonder.cdc.gov/wonder/help/mcd.html, restricted to suicides
  * https://wonder.cdc.gov/mcd-icd10.html
  * Click Agree
  * Group results by State, Year, Month
  * Ages exclude "Not stated"; Hispanic Origin exclude "Not stated"
  * Underlying cause of death: X60-X84 (Intentional self-harm)
* Temperatures & Heat Index:
  * `________.txt` from https://wonder.cdc.gov/wonder/help/nldas.html
  * https://wonder.cdc.gov/nasa-nldas.html
  * Group results by State, Year, Month
  
## Featured Notebooks/Analysis/Deliverables
* Please See the MASTER Jupyter notebook above for the main analysis
> _Note: Visualizations may not render if notebook is loaded in browser. For best viewing results, clone project to local machine._
