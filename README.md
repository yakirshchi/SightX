# Part 1
I've decided to use MongoDB NoSQL database because I assumed that this is the best choice when handling with data in the format of documents like JSON objects. Each document contains pairs of fields and values. The values can typically be a variety of types including things like strings, numbers, Booleans, arrays, or objects. It also good choice for Fast-paced Agile development, huge volumes of data and when the requirements are for scale-out architecture. 
In the script named `gtELT.py` I've written a code for scanning a predefined location where the folders with the ground truth JSON files are located. When a directory is found then its content is scanned for finding JSON files and to load them into MongoDB new collection. The name of the new collection is defined by the name of the folder scanned (the site name). The code loop over all the JSON files in the folder and loads them to the new collection.
Note: I've scanned the predefined location once, but it can be set to monitor the folder the same way as I've coded in part 2 of the home assignment. 

My idea is to load the data to the database and only then to query and analyze it. In the script named `gtAnalysis.py` I've written a code for fetching predefined site collections from MongoDB, for each site to extract all the movies zeroframe data and combine it to one dataframe series for using pandas functions for analyzing the data and calculating metrics like: for each site what was the total movies taken and accordingly what was the average frames count, the average keyframe taken and average count of the number of objects recognized.  
Lior mentioned that the assignment should not take long and to providing explanations will also be accepted. My code stopes at the point after creating a dataframe with all the sites zeroframe data ready for analysis. 
Based on the analysis of the metrics that I've mentions we could see if there is a specific site with more "findings" per movies taken then we can choose to use it more or if a specific site has more objects detected then we can continue analyzing what sort of objects and may get more insight of the type of objects that are better detected then other. And so on. 

# Part 2
In the script named `movieHandler.py` I've written a code that does the following:
Scans the rootPath for .avi file format. if found then checks if the file exists in the rawPath folder. if not, then copy the file to the rawPath folder, creates destination directory for the movie file frames in the trainPath and annotationPath and then extract the frame from the movie file and save them in these directories according to the instructions given.  
Note: The code monitor the rootPath directory every 15 seconds.

# Part 3

Considering that each data collection event includes recording movies from cameras on laptops then we can use internet connection for loading the files to a location on cloud platform that will be preconstructed. let's call the location (server) where the files will be loaded to as "Bucket" directory. This " Bucket " location will be monitored by pre-designed scripts that will recognize the files type and format and will copy them accordingly to another location (on the cloud), let's call the location (server) where the files will be copied to as "Raw" directory. In the "Raw" directory the files will be sorted to folders by business needs like files that need to be sent for external data annotation, files required for low/high resolution etc.
The files that require annotation will be copied to another location directory where they will be deleted after use. The resulted annotation (I assume like the json files) will be going through ETL data quality management procedures for cleaning the data and preparing it for training and the result will be stored in a new location, let's call it "Train" for that use.
These data will also be loaded to and stored in MongoDB database where we can query it easily. 
For storing movie files (Big Data) we can use Hadoop open source. It is optimized to handle massive quantities of data which could be structured, unstructured or semi-structured, using commodity hardware, that is, relatively inexpensive computers. It also allows parallel processing done with great performance. 
For the purpose of data analysis we can consider using hive which is a data warehouse system built on top of Hadoop. Hive facilitates easy data summarization, ad-hoc queries, and the analysis of very large datasets that are stored in Hadoop. Or, we can design a dimensional data model where preprocessed data will be loaded to a relation database for the purpose of reporting (depending on what sort of reporting and analysis will be required). 
All the data passing thorough the "locations" mentioned above should be saved either in MongoDB, Hadoop file system or relational db for BI and analytics purposes and will be deleted from the "locations" after they will be saved. 
The cloud platform is using by default high security standard. All the files loaded and copied will be encrypted and the final location (servers) where that data will be stored will reside in a separate network from where the files are be loaded to. Processes for saving the data in these content stores will initiated from the secure network and no external traffic will be allowed (firewall).

Thank you for taking the time reviewing my home assignment :)

Yakir Shchigelski.

 
