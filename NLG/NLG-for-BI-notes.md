# Natural Language Generation (NLG) for Business Intelligence (BI) Notes

There are several products that enable users to leverage NLG in their dashboards. Many NLG products are available as plug-ins for Business-Intelligence (BI) tools. Generating written narratives from a dataset, and providing written answers to questions asked by users, are two ways in which dashboards can incorporate NLG. A few examples of NLG products available for BI tools include:
- Arria for BI and Arria NLG Studio by Arria NLG
- Wordsmith by Automated Insights  
- Quill by Narrative Science, A Salesforce Company
- Augmented Business Intelligence by Yseop

Organizations leveraging NLG in their dashboards can experience several benefits such as: 
- <b>Time and Cost Reduction</b> - Developers can spend a significant amount of time sharing dashboard insights to various groups. NLG can help developers and end users save time. Developers can reduce the time it takes to share updates and dashboard insights. While end users can gain quality and easy-to-understand insights with minimal guidance.
- <b>Increased User Adoption</b> - One reason dashboards aren't used is because users have trouble retrieving insights immediately. NLG can help users gain context, key insights, and a high-level summary of the data quickly through text.
- <b>Enable Data Driven Decision Making</b> -Dashboards leveraging NLG capabilities empower users to make decisions with their data. Users are able to gain tailored insights based on their view, and in real-time as the data is updated.


## Example 
<i>Note: The following steps show how Tableau Public, a free software, can be used in combination with Arria's free 14-day trial. Tableau Public can be used to see how the extension works within your workbook; however, if you try to publish a workbook to the Tableau Public server you'll find the extension is currently not supported. These steps can also be followed using Tableau Desktop.</i>

### Download Tableau Public 
Tableau Public is a free tool available to develop and share visualizations on the web. Tableau Public can be downloaded here: https://medium.com/r/?url=https%3A%2F%2Fpublic.tableau.com%2Fen-us%2Fs%2Fdownload.

### Download Arria
Arria provides a 14-day free trial - sign up for a free trial here: https://medium.com/r/?url=https%3A%2F%2Flogin.arria.com%2Fsignin. The below examples uses Standard Arria for BI, included in the free trial.

### Download Extension 
Log into your Arria account, and download the extension. In this case we'll be downloading the <i>Arria for Tableau</i> extension.

![image](https://user-images.githubusercontent.com/35014868/179086569-eb46d0e5-a854-4994-873a-1f1c6f875b6c.png)

### Add Extension to Dashboard
Once the extension has been downloaded, it can be added to a Tableau workbook. 
This example shows how to add the Arria extension to the Tableau dashboard, <b>Amazon's Bestselling Books from 2009 to 2019</b>. The sample Tableau dashboard can be downloaded here: https://medium.com/r/?url=https%3A%2F%2Fpublic.tableau.com%2Fshared%2F7QCP7NGKJ%3F%3Adisplay_count%3Dn%26%3Aorigin%3Dviz_share_link.

![image](https://user-images.githubusercontent.com/35014868/179087853-ecd86ab5-11de-4c2d-a202-93fd7b24240f.png)

To add an extension to the dashboard, select <i>Extension</i> from the <i>Objects</i> pane on the bottom left of the workbook.
![image](https://user-images.githubusercontent.com/35014868/179087959-9f1ae09c-fbb3-407b-a026-4348671c6af8.png)


Select <i>Access Local Extensions</i>, then select the <i>Arria for Tableau</i> extension. Note, the extension is saved as a .trex file when downloaded.
![image](https://user-images.githubusercontent.com/35014868/179088031-3bf134b8-4483-4cce-be57-50a641953183.png)

Enter your Arria username and password to get started using the extension.

![image](https://user-images.githubusercontent.com/35014868/179088048-6c1ffcb5-6806-4f01-b616-57cd52d2a7dd.png)

### Configure Your Data 
After the extension has been added to the workbook, the data needs to be configured. 
Within the Tableau object, select <i>Configure your data</i>

![image](https://user-images.githubusercontent.com/35014868/179122067-12e053bf-2d1e-47fe-8a79-ba48eec77cff.png)


<i>Tip: If the object containing the extension is not expanded, make sure to scroll down to the bottom to find the "Configure your data" button.</i>

Select the sheet that you want to use as the source for this NLG extension. In this case we are selecting the visualization, <i>Bestselling Books by Genre and Year</i>.

![image](https://user-images.githubusercontent.com/35014868/179122118-1cf18601-71dc-418d-915b-c14dbd0d1fae.png)

Select the <i>Dimensions</i> and <i>Measures</i> to include in the NLG analysis, and then press <i>Save</i>.

![image](https://user-images.githubusercontent.com/35014868/179122160-ebbba721-d8de-424d-8f26-3d1acc9fc009.png)

Once the data has been configured, there are 3 options to select from: NLG Apps, Arria Answers, and Custom Narratives. 

The following two examples show how to configure <b>NLG Apps</b> and <b>Arria Answers</b>.

### NLG Apps Example 
<i>NLG Apps</i> are templates that allow users to perform NLG analysis on a variety of use cases.

There are several NLG Apps available including <i>Descriptive Statistics</i>, <i>Trend Analysis</i>, and <i>Anomalies</i>.

![image](https://user-images.githubusercontent.com/35014868/179122260-095437f2-d7c9-4d5b-89c8-11f55f72e220.png)

Select <i>Describe a Line Chart</i>, and the relevant <i>Dimensions</i> and <i>Measures</i> for analysis.

![image](https://user-images.githubusercontent.com/35014868/179122365-7faa697a-6e60-4ee0-9642-caf30ade9ea0.png)


To add an alias, select an <i>Entity Type</i>, or specify the units, use the drop-down menu next to a <i>Dimension</i> or <i>Measure</i>. Here we are adding an alias to the <b>CNT(bestsellers with categories)</b> measure.


![image](https://user-images.githubusercontent.com/35014868/179122432-083fee84-d202-4285-8c6e-cbb12054cc9b.png)


Select <i>Important Things</i> as the <i>Narrative Option</i>, and then select <i>Generate</i>.


![image](https://user-images.githubusercontent.com/35014868/179122499-fd946d20-a24d-4d6a-843a-1720def5e1ed.png)


Once the NLG App has been created, you can add it to the dashboard as you would add any other Tableau object.

![image](https://user-images.githubusercontent.com/35014868/179122515-f1b05ffe-b6c2-401c-a7ab-7648b0508d15.png)

Each NLG App has various input parameters required to generate a narrative. The below image shows the same dashboard, but with the <i>Descriptive Statistics</i> NLG App.

## Arria Answers Example 

<i>Arria Answers</i> enables users to ask a question in natural language, and receive written insights from the underlying data.

To utilize <i>Arria Answers</i> within a dashboard, ensure the data has been configured. Then select <i>Arria Answers</i> from the options available. Specify the <i>Dimensions</i> and <i>Measures</i> to use, then select <i>Start</i>.


![image](https://user-images.githubusercontent.com/35014868/179122637-16232288-902b-4676-91d7-96163e86d835.png)


Once configured, the user can ask a question, or select one of the suggestions provided.

![image](https://user-images.githubusercontent.com/35014868/179122663-6f0ee206-d8ef-4a40-8952-26ae5b3637d4.png)

The following image shows <i>Arria Answers</i> configured for the line chart, <i>Bestselling Books by Genre and Year</i>. In this case, the user asked <i>"What year had the most number of fiction books?"</i>. From the output, we can see the year with the most and least bestselling fiction books.

![image](https://user-images.githubusercontent.com/35014868/179122747-2db8e8d8-c696-49f9-9c95-82a6035385c4.png)


The dashboard used in the above example is available on Tableau Public: https://public.tableau.com/shared/T9WS73WTD?:display_count=n&:origin=viz_share_link
