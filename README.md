# Exploratory Data Analysis of the CMS Healthcare Exchange

## Description
 
  Although the ACA was passed in 2010, it was not completely implemented until January 1, 2014 due to challenges. With the implementation of the exchange,the Centers for Medicare & Medicaid Services (CMS)maintains a website with datafiles describing of all insurance programs that are eligible and/or participate. 
  
  The financial aspects of the dataset has been well documented by others.  My focus is exploring the  change social norms shown in the datasets for the first three years of their reporting existence (2014-2016). I planned to examine more factors but due to time and the size of the dataset, the emphasis was started on extended family relationships.

## Requirements

A copy of the datasets was pulled from [Kaggle] (https://www.kaggle.com/hhs/health-insurance-marketplace). The original dataset are hosted at [CMS.gov] (https://www.kaggle.com/hhs/health-insurance-marketplace).  

    
## The Data 

### Benefits and Cost Sharing 
Plan variant-level data on essential health benefits, coverage limits, and cost sharing. Files and variables related to this set are labelled **cost**.

---|2014|	2015|	2016|	Merged|	Cleaned|Sample|		
---|---|---|---|---|---|---
Rows|	1164869|2079286|1804253|5048408|---|---
Fields|32|32|30|32|---|---
Size|284.4MB|507.6MB|413MB|1.2GB|---|---

## Business Rules  
Plan-level data on rating business rules, such as allowed relationships (e.g., spouse, dependents) and tobacco use.  Files and variables related to this set are labelled **rules**.		
	Rows	2103	10095	8887	21085	20866	
	Fields	23	23	23	24	17	
	Size	378KB	1.8MB	1.6MB	4MB	2.9MB	
##### The increase in fields for the merged file is due to a change of keys

## Network	
Provides the details for each healthcare network and a url to the network's website.Files and variables related to this set are labelled **network**.		
Rows	937	1459	1426		3822	
Fields	14	14	14	15	5	
Size	102KB	160KB	156KB	478KB	149.4
	##### The increase in fields for the merged file is naming inconsistency of the Dental Only plans
						
## Plan Attributes 
Plan-level data on maximum out of pocket payments, deductibles, HSA eligibility, formulary ID, and other plan attributes.	Files and variables related to this set are labelled **attr**.		

	Rows	18719	31253	27381	77353		
	Fields	126	126	151	176		
	Size	18MB	30MB	31.5MB	104.5MB		
## Rate
Plan-level data on individual rates based on an eligible subscriber’s age, tobacco use, and geographic location, and family-tiers.Files and variables related to this set are labelled **rate**.		

	Rows	3796388	4676092	4221965	12694445		
	Fields	24	24	24	24		
	Size	695.1MB	856.2MB	773.1MB	2.4GB
	
## Area
The geographical area of each plan and whether it was offered nationally, by state, by region, by country, or by zip code.Files and variables related to this set are labelled **rate**.		
Rows	8874	17495		42247	42247		
	Fields	18	18	18	19	10	
	Size	1.2MB	2.4MB	2.2MB	6.4MB	3.2MB
#### The increase in fields for the merged file is naming inconsistency of tkeys

## Plan ID Crosswalk 
Plan-level data mapping plans offered in the previous plan year to plans offered in the current plan year.Files and variables related to this set are labelled **cross**.	
	Rows		132505	150005	282510	282510	
	Fields		21	21	31	9	
	Size		21.2MB	24MB	69MB	21.6MB
	**(keys)/year specific
	
## Machine-readable
The 2016 dataset includes a 450 row x 6 column Excel file with the urls to allow machines to pull data from the insurance providers. Files and variables related to this set are labelled **cross**

	
	

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    While the Supreme Court ruled same sex marriage must be recognized by all states, the divide in America widened in America on other issues like abortion and children's rights. I was looking for evidence of 
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  If a state chooses to offer their own healthcare exchange, they may post their data in their own repository instead of including it the summary data from CMS.
