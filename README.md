# A Tale of Two Cities: Tier-2 & Tier-3
# Using Zomato User-Reviews to Generate Restaurant Recommednations 
![image](https://user-images.githubusercontent.com/78511177/182169566-c93f872b-daa2-469c-9f91-8e5c6c795308.png)


#### AIPI 540 Deep Learning Applications
#### Project by: Derrick Adam
#### Project Structure: Recommendation System Module
#### Category: Social Commerce

Motivation
----------
"A charity dollar has only one life; a Social Business dollar can be invested over and over again." - Muhammad Yunus

Social x Mission-Driven Commerce


![image](https://user-images.githubusercontent.com/78511177/182501979-476cec75-e8a9-4d6d-8f70-99d6f74322f9.png)


In 2021, online retail sales in the U.S. totaled $960 Billion. China's total was $2.49 trillion and India's was 1.08 trillion. China's e-commerce market is larger than the U.S., U.K., Japan, and Germany *combined*. China has many e-commerce competitors, such as Alibaba, JD.com, Tencent, Meituan, and Pinduoduo.  Pinduoduo, for example, is successful in China because it leverages the social networks created on the ubiquitous WeChat platform (owned by Tencent). WhatsApp (owned by Meta) has similar ubiquity in India, the U.S., Africa, and South America. WhatsApp is sitting on a goldmine of social networks from which group-buying can bring affordable groceries and fast moving consumer goods (FMCG) to users, especially in Tier-2 and Tier-3 cities. China is  already saturated, so focusing on Tier-2 and Tier-3 cities in areas where WhatsApp is most used, offers a more compelling value proposition. 
<br>
* Social media and retail integration are here to stay and have created category defining companies and platforms, such as, Pinterest, Venmo, Instagram, and Pinduoduo 
* Engagement with consumers is key to converting into a selling opportunity
* Integrated Ecosystems should be the goal. Alibaba & Tencent combine Search x Social x Commerce x Logistics x Payments
* Rise of the middle class & disposable income, internet connectivity, and mobile phone uses will continue to drive e-commerce

Massive Runway of E-Commerce
![image](https://user-images.githubusercontent.com/78511177/182518312-4b3746fe-5431-4192-8d05-7791e5912414.png)

(Source: convergine.com)


Problem Statement
-----------------
* The objective of this project is to generate restaurant recommendations from user reviews on the Zomato platform, an Indian company that focuses Tier-2 and Tier-3 cities
* Tastes are unique and oftentimes representative of the area one lives in
* This project will serve as proof-of-concept for  WhatsApp to integrate with e-commerce retailers serving other Tier-2 cities, Tier-3 cities, and food deserts. Group-Buying, a cocnept proven by China's Pinduoduo, makes use of the WeChat platform and the rise in social commerce to drive down the costs of goods for those living in Tier-2 and Tier-3 cities. 
* The interactive Streamlit platform abstracts away the mundane and provides value to the end user in the following ways: 

    1) Users input their favorite restaurant

    2) TF-IDF Is used to find similar words

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
Here a demo of the Streamlit app:

https://user-images.githubusercontent.com/78511177/182522439-12f4503f-34fb-4bea-babd-643905e7fa57.mp4



Data Sourcing, Processing, & Modeling
-------------------------------------

Adavantages of Deep Learning vs. Non-Deep Learning in E-Commerce
---------------
Deep Learning Recommendation Systems in E-Commerce can better capture the proprietary meaning of one's data. Past engagement data is used to make informed reommendations in the future.

Recommendation Systems enrich the buying and social aspects of e-commerce in the following ways:

   1) Personalized Recommendations: Depth over breadth. Understanding the individual is directly correlated to higher platoform engagement whch yields a higher buying convert rate 
    
   2) Dynamic Pricing: Influencers can use their network to generate price reductions for groups or members of their platform 
     
   3) Search and Discovery: Breadth over depth. Recommendation systems have access to engagement data within thier platform and can suggest items an individual might not consider otherwise

Model Evaluation & Results
----------------------------

Search results for Chianti:

<img width="721" alt="Screen Shot 2022-08-03 at 10 00 08 AM" src="https://user-images.githubusercontent.com/78511177/182668073-438e0d8f-8c02-4e3a-a8f9-adc66bac7c39.png">


Search results for Church Street Social:

<img width="728" alt="Screen Shot 2022-08-03 at 10 02 33 AM" src="https://user-images.githubusercontent.com/78511177/182668158-5cb0be61-dbf6-4dfd-9b39-681eb25f55d0.png">


Search results for Pai Vihar:

<img width="717" alt="Screen Shot 2022-08-03 at 10 03 26 AM" src="https://user-images.githubusercontent.com/78511177/182668281-ef5ba258-de4a-46b4-912b-7180a993c9e6.png">


Search results for Container Coffee:

<img width="720" alt="Screen Shot 2022-08-03 at 10 06 47 AM" src="https://user-images.githubusercontent.com/78511177/182668360-398bbc01-1b74-46a8-9ecd-6a3b1ecd9f08.png">



Future Work
------------
* include review text and user rating evaluations (whether other users thought a particular user’s review was funny, useful, or helpful) as features in the prediction model
* A platform, like WhatsApp or Facebook Messenger, can be leveraged to provide low-cost, healthy food to *food deserts*, undeveloped areas with increased levels of food insecurity
* 

Conclusion
----------
* Tencent's WeChat is not successful becuase it has so many people or sells things. Rather, it monetizes its vast user base by providing seamless integration of Search x Social x Commerce x Logistics x Payments x Gaming
* In the case of Meta/Facebook, the only way to retain and grow its existing user base is to provide them exceptional value beyond the ad business 
* Apple shifted from a hardware focus to a recurring revenue services business -> resulting in multiple expansion -> ~2.5 trillion market cap
* Since there are many great exisitng products, any given platform needs to give users many reasons to stay. Giving them great product recommendations, engaging content, and channels to connect with their networks -> create a "sticky" platform that can fuel company growth 
* Prioritzing users by playing towards their prefernces and personalities, can lead to increased customer lifetime value
* A platform that can serve groups of people at the same time can serve many while decarbonizing grocery and food delivery
 

Additional Resources
--------------------
* Corresponding Slide Deck: [here](https://prodduke-my.sharepoint.com/:p:/g/personal/da204_duke_edu/EScIg4CKoqJOqLhn_NIefk8Bj4aZ5zOENWZVOYkwIkT7zg?e=WjJlps)

* Creating a World Without Poverty: Social Business and the Future of Capitalism by Muhammad Yunus: [here](https://www.amazon.com/Creating-World-Without-Poverty-Capitalism/dp/1586486675/ref=sr_1_1?crid=2M36RNX09TRDJ&keywords=Creating+a+World+Without+Poverty%3A+Social+Business+and+the+Future+of+Capitalism+by+Muhammad+Yunus&qid=1659367467&sprefix=creating+a+world+without+poverty+social+business+and+the+future+of+capitalism+by+muhammad+yunus%2Caps%2C147&sr=8-1)

* Bloomberg Article on Meta's (formerly known as Facebook) $19 Billion Acquisition of WhatsApp: [here](https://www.bloomberg.com/opinion/articles/2022-07-25/zuckerberg-s-bet-on-whatsapp-might-not-pay-off)

* McKinsey Report: Decarbonizing Grocery: [here](https://www.mckinsey.com/industries/retail/our-insights/decarbonizing-grocery)

* Michelle Obama lead America's Healthy Food Financing Initiative Reinvestment Fund: [here](https://www.investinginfood.com/)

* Partnership for a Healthier America: [here](https://www.ahealthieramerica.org/)

Citation
--------
