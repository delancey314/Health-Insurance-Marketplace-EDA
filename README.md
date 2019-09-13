# Exploratory Data Analysis of the CMS Healthcare Exchange

## Description
 
  Although the ACA was passed in 2010, it was not completely implemented until January 1, 2014 due to challenges. With the implementation of the exchange,the Centers for Medicare & Medicaid Services (CMS)maintains a website with datafiles describing of all insurance programs that are eligible and/or participate. 
  
  The financial aspects of the dataset has been well documented by others.  My focus is exploring the  change social norms shown in the datasets for the first three years of their reporting existence (2014-2016). I planned to examine more factors but due to time and the size of the dataset, the emphasis was started on extended family relationships.

## Requirements

A copy of the datasets was pulled from [Kaggle](https://www.kaggle.com/hhs/health-insurance-marketplace). The original dataset are hosted at [CMS.gov](https://www.kaggle.com/hhs/health-insurance-marketplace).  

## Goals
Primary goal is to practice working with big data
#### Condense/consolidate/catalog the dat from 18 files and 4.1GB to something more user friendly
#### Locate data to graph and test

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
	
	

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    While the Supreme Court ruled same sex marriage must be recognized by all states, the divide in America widened in America on other issues like abortion and children's rights. I was looking for evidence of 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  If a state chooses to offer their own healthcare exchange, they may post their data in their own repository instead of including it the summary data from CMS.
