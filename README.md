# Exploratory Data Analysis of the CMS Healthcare Exchange

## Description
 
  Although the ACA was passed in 2010, it was not completely implemented until January 1, 2014 due to challenges. With the implementation of the exchange,the Centers for Medicare & Medicaid Services (CMS)maintains a website with datafiles describing of all insurance programs that are eligible and/or participate. 
  
  The financial aspects of the dataset has been well documented by others.  My focus is exploring the  change social norms shown in the datasets for the first three years of their reporting existence (2014-2016). I planned to examine more factors but due to time and the size of the dataset, the emphasis was started on extended family relationships.

## Requirements

A copy of the datasets was pulled from [Kaggle](https://www.kaggle.com/hhs/health-insurance-marketplace). The original dataset are hosted at [CMS.gov](https://www.kaggle.com/hhs/health-insurance-marketplace).  

## Goals
Primary goal is to practice working with big data
##### Condense/consolidate/catalog the data from 18 files and 4.1GB to something more user friendly
#####  Locate data to graph and test
#####  Tocomplete a map reduce of characters using Spark

## The Data 

### Benefits and Cost Sharing 
Plan variant-level data on essential health benefits, coverage limits, and cost sharing. Files and variables related to this set are labelled **cost**.

## Business Rules  
Plan-level data on rating business rules, such as allowed relationships (e.g., spouse, dependents) 
###### The increase in fields for the merged file is due to a change of keys

## Network	
Provides the details for each healthcare network and a url to the network's website.Files and variables related to this set are labelled **network**.	
###### The increase in fields for the merged file is naming inconsistency of the Dental Only plans
						
## Plan Attributes 
Plan-level data on maximum out of pocket payments, deductibles, HSA eligibility, formulary ID, and other plan attributes. Files and variables related to this set are labelled **attribute**.	

## Rate
Plan-level data on individual rates based on an eligible subscriber’s age, tobacco use, and geographic location, and family-tiers.Files and variables related to this set are labelled **rate**.	

## Area
The geographical area of each plan and whether it was offered nationally, by state, by region, by country, or by zip code.Files and variables related to this set are labelled **area**.
#### The increase in fields for the merged file is naming inconsistency of the keys

## Plan ID Crosswalk 
Plan-level data mapping plans offered in the previous plan year to plans offered in the current plan year.Files and variables related to this set are labelled **cross**.	

## Machine-readable
The 2016 dataset includes a 450 row x 6 column Excel file with the urls to allow machines to pull data from the insurance providers. Files and variables related to this set are labelled **cross**
![data_table](https://github.com/delancey314/Health-Insurance-Marketplace-EDA/blob/master/images/data_table.png)
	
# Data Exploration
### Loading the initial files
Due to the large size of the files, it took some effort getting them to load. In addition, Python could not read a series of non-UTF characters as well. The following tools were used/attempted trying to find an loader that would work  decode correctly and read the large datafiles.
Python defaults
Pandas
Numpy
SciPy
spark.read.load
bota3
csv
codecs
pickle
### I am a latin1 lover
The keybreakthrough was finding 'latin1' encoding for Pandas. This was the standard script used to load the initial files:

rules2014=pd.read_csv('data/2014/Business_Rules_PUF.csv',low_memory=False,encoding='latin1')

 I recommend the following parameters  for Pandas.read_csv to deal with size.
 **chunksize**
 Allows you to load the large file in chunks of set sizes and then manipulate the chunk
 **low_memory = False**
 Tells pandas to use all your memory trying to load.
 **usecols =[List]**
 Only load the columns in the list
 **nrows**
 Select only a set number of rows. Slower than chunksize and does not allow manipulation.
 ***memory_map**
 data is loaded directly into memory, skipping the IO interface.
 
 ### Reduce and Reload
  Loading all the files at once caused both major lags. In addition, many of the files were too big to be able to use .unique(),  .info() and .describe().  Python would leave out null values, counts, or fields completely.  To get around these blocks I wrote a series of scripts.
  
  **pipeline.py** - This script read in all of the files for a given group, merged them into summary file, deleted the old files from memory, and wrote a copy of the merged file to disk.  It then manually created unique for each field as exported all columns to an Excel file. 
  **clean_encode_and_map.py** This script loaded the summary file and unique files from disk to allow data exploration.  In addition, it hot encoded Cohabitation into 129 hot categories and then mapped the new hot categories.
  
 **make_samples.py**  Pulled a random sample of 10,000 rows for each group to allow the previous script to investigate the data more easily.
 
 ### Manual exploration of the data
 Since my focus was to find changes in how society has changed their views, I searched for anything that ever had a stigma or controvery (abortion, weight, same sex marriage, female alopecia, etc)  anything related to demographic criteria (women, children, elderly, familial relationship, etc). This was very time intensive. 
 
 For instance, the Benefits dataset had a field with 10316 unique values that I was able to identify 916 different ones that met my criteria.  Only one dataset (rates) turned out to not have data that met my criteria. A field in the rules dataset has a field called **CohabitationRules** that lists whether a non-policyholder must cohabitate with the holder to be covered by the plan.  This field was valuable because by inference, if the relationship is listed, it is covered under plan. Second, it shows whether they have to stay under the same roof.  Third, you could infer versus the overall dataset whether something was specifically excluded.   
 
 I performed a hot encoding of the 381 different combinations to produce 129 separate  0/1 fields for each type of cohabitation category.  I then produced maps to show the differences.
 
 ## Georgia and Iowa allow annulled
 
 ![Georgia and Iowa allow annulled](https://github.com/delancey314/Health-Insurance-Marketplace-EDA/blob/master/annulment.png)
 
## Montana allows in-laws not living with you
 ![Montana allows in-laws not living with you](https://github.com/delancey314/Health-Insurance-Marketplace-EDA/blob/master/brother%20or%20sister%20in%20Law.png)
 
 ## Texas doesn't make you live with yourself
 ![Texas existentialism](https://github.com/delancey314/Health-Insurance-Marketplace-EDA/blob/master/images/live%20with%20yourself.png)
 
 ## Suprises
 There is at least one plan that has coverage for incest services.
 
 Many states are very tolerant of extended relatives on insurance.
 
 Many states provide a pre-payment for coverage of Native Americans to ensure service is available.
 
 There are multiple plans that require a referral for labor and delivery unless its an emergency.
 
 Future Exploration
 
 #1   Normalize my maps for population
 
 #2.  Hot encode medical and socialogical variables
 
 #3.  Include the state sponsored exchanges
 
 #4   Convert python scripts to classes. Particularly the hot encoding script so I can generalize it for any inputted list.
 
#5	Get the data into Spark to get it to do the heavy lifting.
 
 
  
  
## Thanks
Frank Burkholder for providing 'latin1'  to get over my loading error
Fred Berendse for his assistance in converting the hot encoding function to a lambda function.
Nicolas Jacobsohn for sharing his pickle function


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
 
