# NASA HUB NASA SPACE APP CHALLANGE 2023
**Team**: NASA HUB

**Location**: Kyiv, Ukraine

**Challange**: A marketplace for OpenSciense

## Main Challenges in Open Science

* Lack of centralized storage for grants and projects
* Inefficient tagging system, making it difficult to find relevant projects
* Limited opportunities for young scientists to connect with projects due to lack of established credentials
* Dispersed storage locations for datasets and other open data
* Inability for scientists to share specialized equipment due to lack of awareness of each other

## Our Approach - OpSci: A Marketplace for Open Science
<p align="center">
  <img src="https://github.com/olehmell/nasa-space-apps-2023/assets/39906111/5083ad38-4050-4d0d-9393-84429ba62871" width="250">
</p>

#### A marketplace that consolidates:
  * Grants from major platforms
  * Projects and grants that can be directly live on our platform
  * Individuals with specialized skills and equipment
#### Unique features for improving Open Science collaboration experience:
* Natural language-based matching (based on project descriptions or search queries)
* Open Source culture onboarding for new scientists
* Cross-platform profile and score for easier matching
  
<p align="center">
  <img src="https://github.com/olehmell/nasa-space-apps-2023/assets/39906111/53204d75-1501-4adb-8d9d-433f3ae9cf9c" width="720">
</p>

## Tech Details

### Cross-platform score for easier matching

By aggregating data from diverse sources using ORCID (allows aggregating  from CrossRef, SCOPUS API, ResearcherID, DataCite, BASE), GitHub, the system provides a holistic view of a contributor's academic and coding contributions. This comprehensive analysis ensures a more accurate representation of a contributor's impact and expertise.
<p align="center">
  <img src="https://github.com/olehmell/nasa-space-apps-2023/assets/39906111/d97e12fc-eb59-47f9-8bb2-6cabd1d86c6c" width="500">
  <img src="https://github.com/olehmell/nasa-space-apps-2023/assets/39906111/4c5e05aa-7fd7-439d-9672-d3500814001d" width="500">
</p>
 
The cross-platform score can facilitate better matchmaking between projects and potential contributors. Projects can identify contributors with the required expertise, while contributors can find projects aligned with their skills and interests.

Different platforms can have biases based on their primary user base or purpose. By incorporating multiple platforms, this system can minimize the biases associated with any single platform.

Instead of manually checking multiple platforms for contributor information or project details, stakeholders can get an aggregated score swiftly, saving time and effort.

Also, a scoring system combats spam and malicious activity on digital platforms. Thresholds and Limitations, restrict users or content that fall below set scores, deterring undesired behaviors.


### Matching system architecture
The system takes a scientist or project's description and score, cleans the text using nltk, and extracts keywords with YAKE. These keywords and the score guide a search in ElasticSearch for relevant matches. The system then uses TF-IDF vectors to measure similarity between descriptions with cosine similarity. Finally, an LLM explains the reasons for each match.

#### Step by step algorithm 
<p align="center">
  <img src="https://github.com/olehmell/nasa-space-apps-2023/assets/39906111/7b4ef4a0-c46f-4232-988a-d88ea6a3cbf8" width="720">
</p>

1. Input: Description and profile score of scientist or project.
2. Text Cleaning (using nltk): Remove stop words, stemming, tokenization.
3. Keyword Extraction (using YAKE): Identify key terms from the cleaned description.
4. Search in ElasticSearch: Use extracted keywords and score as search parameters.
5. Text-to-Vector Conversion: Convert descriptions to TF-IDF vectors for similarity analysis.
6. Cosine Similarity Calculation: Measure similarity between input and potential matches.
7. Text Matching: Identify best matches based on similarity scores.
8. Explanation using LLM: Provide context on why each match was selected.

MVP matching script: [code](https://github.com/olehmell/nasa-space-apps-2023/blob/main/main.py)


### Reduce joining friction for new scientist
New scientists often encounter barriers when trying to secure funding and collaborate on research projects. They face the daunting task of navigating through numerous grant sources, each with its own platform and application process. Additionally, these emerging scientists might not have an established reputation or sufficient "score" within the scientific community, making it challenging to join ongoing projects. Moreover, grant organizations often struggle with visibility, with their grant opportunities getting lost amidst the myriad of sources.

By aggregating grants from popular sources into a single platform, our solution removes the need for scientists to sift through multiple websites or databases. This consolidation streamlines the grant discovery process, ensuring scientists can easily find and apply for relevant funding opportunities.
<p align="center">
  <img src="https://github.com/olehmell/nasa-space-apps-2023/assets/39906111/01f440bb-6643-412f-83ac-0378095a6b0d" width="720">
</p>

Drawing inspiration from the open-source community, the platform introduces the concept of "first good research" opportunities. Much like "first good issues" in coding projects, these are entry points for scientists who might not have an established track record. By completing these research tasks, new scientists can showcase their skills and potential, making it easier for them to join larger projects and collaborations.

## Future improvements

### Open Science Graph based on Blockchain
Blockchain technology offers an immutable and transparent way to store and verify scientific contributions. We plan to develop an Open Science Graph that will record key milestones in a scientist's career, thereby enhancing credibility and trust within the community. 

### Zero-Knowledge Proof for Linking Science's Achievements with Profile
Privacy is a major concern in academic circles. With the incorporation of Zero-Knowledge Proofs, scientists can validate their credentials and achievements without revealing sensitive information. This enables a secure and private way to establish credibility. We are looking for [PolygonID](https://polygon.technology/polygon-id) 

### Generic Score
The current scoring system desogn is splited by platforms. We aim to introduce a more generic scoring metric that can be widely applicable across various scientific disciplines and types of contributions.

## References
https://spotintelligence.com/2022/12/19/text-similarity-python/#1_Text_similarity_with_NLTK

https://www.crossref.org/documentation/retrieve-metadata/rest-api/

https://support.datacite.org/docs/api

https://api.base-search.net

https://dev.elsevier.com/sc_apis.html

https://up-for-grabs.net/#/

https://github.com/showcases/great-for-new-contributors

https://goodfirstissue.dev/

https://nationaltoday.com/free-open-source-software-month/

https://scientificandmedical.net/events/

https://www.nasa.gov/missions/station/open-source-science-opportunities/

https://www.kickstarter.com/pages/science 

https://www.zooniverse.org/talk/18

https://zooniverse.github.io/panoptes/?http#list-all-projects

https://scistarter.org/
