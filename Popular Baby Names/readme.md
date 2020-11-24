## Popular Baby Names Analysis


### Project Overview
This project looks at popular baby names across the United States from 1880 to 2019, at both the National and State level. Data was retrieved from the US SSA website, and analysis was conducted using Python and Tableau Public. 


### Data Overview
Data was retrieved from the US Social Security Administration website, for both the National level and the State level.

- National-level data: consisted of text files of popular baby names in the US, for each year between 1880 and 2019.
- State-specific data: consisted of text files of popular baby names for each state, between 1910 and 2019.

The text files available on the US SSA website were used to create 3 datasets, 2 of which were used in the final analysis.

1. popularBabyNames_National.csv : Popular baby names across the US from 1880 - 2019
2. popularBabyNames_State.csv : Popular baby names by state from 1910 - 2019
3. popularBabyNames.csv : Combines National dataset (#1) and State dataset (#2) into a single dataset containing most popular baby names.

'popularBabyNames_State.csv' and 'popularBabyNames.csv' were the 2 main datasets used in this project. Full information on these datasets and the attributes available are listed on the [Data Dictionary](DataDictionary.md). 

### Tools Used

Python and Tableau Public were the two primary tools used for this analysis. Python was used to create a script to clean and merge the datasets from the US SSA website. Once the datasets were created, Tableau Public was then used to visualize the most popular baby names in the United States, at both a national and state level.

### Tableau Dashboard
 Link to dashboard on Tableau Public: 
 [Popular Baby Names Analysis](https://public.tableau.com/views/PopularBabyNamesAnalysis/PopularBabyNamesAnalysis?:language=en&:display_count=y&publish=yes&:origin=viz_share_link)

Static image of dashboard below (to view full interactive features, including filters and views in tooltips, view dashboard on Tableau Public): 

<div class='tableauPlaceholder' id='viz1606181838474' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PopularBabyNamesAnalysis&#47;PopularBabyNamesAnalysis&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='PopularBabyNamesAnalysis&#47;PopularBabyNamesAnalysis' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Po&#47;PopularBabyNamesAnalysis&#47;PopularBabyNamesAnalysis&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en' /></object></div>                
