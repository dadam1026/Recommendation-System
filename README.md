# A Tale of Two Cities: Tier-2 & Tier-3
# Using Zomato User-Reviews to Generate Restaurant Recommednations 
![image](https://user-images.githubusercontent.com/78511177/182169566-c93f872b-daa2-469c-9f91-8e5c6c795308.png)


#### AIPI 540 Deep Learning Applications
#### Project by: Derrick Adam
#### Project Structure: Recommendation System Module
#### Category: Social Commerce
#### Themes: 4 & 6 Social Media x Food

Motivation
----------
"A charity dollar has only one life; a Social Business dollar can be invested over and over again." - Muhammad Yunus

Social x Mission-Driven Commerce


![image](https://user-images.githubusercontent.com/78511177/182501979-476cec75-e8a9-4d6d-8f70-99d6f74322f9.png)


In 2021, online retail sales in the U.S. totaled $960 Billion. China's total was $2.49 trillion and India's was 1.08 trillion. China's e-commerce market is larger than the U.S., U.K., Japan, and Germany *combined*. China has many e-commerce competitors, such as Alibaba, JD.com, Tencent, Meituan, and Pinduoduo.  Pinduoduo, for example, is successful in China because it leverages the social networks created on the ubiquitous WeChat platform (owned by Tencent). WhatsApp (owned by Meta) has similar ubiquity in India, the U.S., Africa, and South America. WhatsApp is sitting on a goldmine of social networks from which group-buying can bring affordable food, groceries and fast moving consumer goods (FMCG) to users, especially in Tier-2 and Tier-3 cities. China is  already saturated, so focusing on Tier-2 and Tier-3 cities in areas where WhatsApp is most used, offers a more compelling value proposition. 
<br>
* Social media and retail integration are here to stay and have created category defining companies and platforms, such as, Pinterest, Venmo, Instagram, and Pinduoduo 
* Engagement with consumers is key to converting into a selling opportunity
* Integrated Ecosystems should be the goal. Alibaba & Tencent combine Search x Social x Commerce x Logistics x Payments x Gaming
* Rise of the middle class & disposable income, internet connectivity, and mobile phone uses will continue to drive e-commerce

Massive Runway of E-Commerce
![image](https://user-images.githubusercontent.com/78511177/182518312-4b3746fe-5431-4192-8d05-7791e5912414.png)

(Source: convergine.com)


Problem Statement
-----------------
* The objective of this project is to generate restaurant recommendations from user reviews on the Zomato platform, an Indian restaurant aggregator and food delivery company focusing on Tier-2 and Tier-3 cities
* Tastes are unique and oftentimes representative of the area one lives in
* This project will serve as proof-of-concept for  WhatsApp to integrate with e-commerce retailers serving other Tier-2 cities, Tier-3 cities, and food deserts. Group-Buying, a concept proven by China's Pinduoduo, makes use of the WeChat platform and the rise in social commerce to drive down the costs of goods for those living in Tier-2 and Tier-3 cities. 
* The interactive Streamlit platform abstracts away the mundane and provides value to the end user in the following ways: 

    1) Users input their favorite restaurant

    2) TF-IDF is used to find similar words

    3) System will look at the reviews of other restaurants and recommend other restaurants with similar reviews sorted from highest to lowest rated





Getting Started
---------------
1. To run locally: Clone the repository, create a virtual environment, and install the requirements needed to run the application
```
pip install -r requirements.txt
```
2. Start the Streamlit app
```
streamlit run main.py
```
Here is a demo of the Streamlit app:

https://user-images.githubusercontent.com/78511177/182522439-12f4503f-34fb-4bea-babd-643905e7fa57.mp4



Data Sourcing, Processing, & Modeling
-------------------------------------
* Data is sourced from Kaggle's Zomato's Recommendation System. The data file is large, so here is the link: https://www.kaggle.com/code/chirag9073/zomato-recommendation-system/notebook

* Columns for url, address, name, online_order, book_table, rate (and more) and their unique values are used:
<img width="484" alt="image" src="https://user-images.githubusercontent.com/78511177/182971108-d2941310-0e4a-40db-99a6-47a55df8672b.png">


* When a user enters a restaurant on the Streamlit User Interface the following steps happen under the hood:

     1) Loading the Dataset
    
     2) Data Cleaning: Renaming columns, dropping duplicates, and removing NaN values from the dataset 
     
     3) Text Preprocessing: Cleaning unnecessary words in the reviews, Removing links and other unncessary items, and Removing Symbols

     4) Recommendation System

Adavantages of Deep Learning vs. Non-Deep Learning in E-Commerce
---------------
Deep Learning Recommendation Systems in E-Commerce can better capture the proprietary meaning of one's data. Past engagement data is used to make informed reommendations in the future.

Recommendation Systems enrich the buying and social aspects of e-commerce in the following ways:

   1) ???? Bespoke Recommendations: Depth over breadth. Understanding the individual is directly correlated to higher platform engagement whch yields a higher buying convert rate 
    
   2) ???? Dynamic Pricing: Influencers can use their network to generate price reductions for groups/followers of their platform 
     
   3) ???? Search and Discovery: Breadth over depth. Recommendation systems have access to engagement data within thier platform and can suggest items an individual might not have considered otherwise

Model Evaluation & Results
----------------------------
* The tool works best searching for restaurants native to Bangalore, India
* The tools is generating very??successful results because it is finding??similar type of restaurants to the input:
    
    1) If a cafe is inputted, the recommendations are cafes
       
       Example: Container Coffee 
       
       
       
       <img width="320" alt="image" src="https://user-images.githubusercontent.com/78511177/182875531-1f08ec0f-09a2-4d8e-b8ad-a5ac7f4aed78.png">




    2) If a pub is inputted, the recommendations are pubs
       
       Example:  Church Street Social??
       
       
       
       <img width="313" alt="image" src="https://user-images.githubusercontent.com/78511177/182877237-951e8c91-e2c8-4da2-9f31-f0eae6c1c87a.png">




Other Results -
      
Search results for Chianti:

<img width="721" alt="Screen Shot 2022-08-03 at 10 00 08 AM" src="https://user-images.githubusercontent.com/78511177/182668073-438e0d8f-8c02-4e3a-a8f9-adc66bac7c39.png">


Search results for Pai Vihar:

<img width="717" alt="Screen Shot 2022-08-03 at 10 03 26 AM" src="https://user-images.githubusercontent.com/78511177/182668281-ef5ba258-de4a-46b4-912b-7180a993c9e6.png">




Future Work
------------
* Include review text and user rating evaluations (whether other users thought a particular user???s review was funny, useful, or helpful) as features in the prediction model
* Take into consideration individual dietary restrictions
* A platform, like WhatsApp or Facebook Messenger, can be leveraged to provide low-cost, healthy food to *food deserts*, undeveloped areas with increased levels of food insecurity. For example, at the end of day restaurant food gets trown out. That food can be routed to families living in food deserts
* Engage other successful platforms and other organizations to increase reach. Some possible collaborators include, Amazon, Sea, MercadoLibre, Jumia, Shopify, America's Healthy Food Financing Initiative Reinvestment Fund, and Partnership for a Healthier America

Conclusion
----------
* Tencent's WeChat is not successful because it has so many people or sells things. Rather, it monetizes its vast user base by providing seamless integration of??Search x Social x Commerce x Logistics x Payments x Gaming
* Since there are many great existing social media products, any given platform needs to give users many reasons to stay. Giving them great product recommendations, engaging content, and channels to connect with their networks = a "sticky" platform that can fuel company growth 
* Prioritizing users by playing towards their preferences and personalities, can lead to increased customer lifetime value
* A platform that can serve many people at the same time also serves to decarbonize grocery and food delivery
* A social business is the best type of business serving the social, economics, and environmental needs of the most vulnerable
 

Additional Resources
--------------------
* Corresponding Slide Deck: [here](https://prodduke-my.sharepoint.com/:p:/g/personal/da204_duke_edu/EScIg4CKoqJOqLhn_NIefk8Bj4aZ5zOENWZVOYkwIkT7zg?e=WjJlps)

* Creating a World Without Poverty: Social Business and the Future of Capitalism by Muhammad Yunus: [here](https://www.amazon.com/Creating-World-Without-Poverty-Capitalism/dp/1586486675/ref=sr_1_1?crid=2M36RNX09TRDJ&keywords=Creating+a+World+Without+Poverty%3A+Social+Business+and+the+Future+of+Capitalism+by+Muhammad+Yunus&qid=1659367467&sprefix=creating+a+world+without+poverty+social+business+and+the+future+of+capitalism+by+muhammad+yunus%2Caps%2C147&sr=8-1)

* Bloomberg Article on Meta's (formerly known as Facebook) $19 Billion Acquisition of WhatsApp: [here](https://www.bloomberg.com/opinion/articles/2022-07-25/zuckerberg-s-bet-on-whatsapp-might-not-pay-off)

* McKinsey Report: Decarbonizing Grocery: [here](https://www.mckinsey.com/industries/retail/our-insights/decarbonizing-grocery)

* Michelle Obama lead America's Healthy Food Financing Initiative Reinvestment Fund: [here](https://www.investinginfood.com/)

* Partnership for a Healthier America: [here](https://www.ahealthieramerica.org/)

