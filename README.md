# 2024-Live-Election-Results
The 2016 election was filled with so much uncertainty from the Democratic party and Hillary Clinton frequently publicly calling the election a Russian collusion and rigged for Donald Trump. The 2020 election was filled with so much uncertainty from the Republican party and Donald Trump frequently publicly calling the election fraudulent and rigged. As result, there is often great division between people who believe in election integrity and people who do not. This is extremely frustrating, and I, an independent data scientist and investigator has decided to take matters into my own hands. There is very frequent live coverage of the election on TV, YouTube, Rumble, etc. that people like to tune into and see how it's going. There is also live coverage online with maps telling you how many votes each candidate has, who is leading, odds of winning, etc. For those that prefer to just see the numbers, you may tune into stuff like that.\
\
That is where this project comes into play. One of the issues with investigating the results of elections is that everybody is just looking at the end result. Elections in America (as of recently) span over the course of 1-2 weeks. The first day has the most activity as day of voting is the busiest, and counting is the most prevalent. However, counting continues in some states for up to two weeks after election day. Therefore, the numbers will continue to tick up for both candidates in that time. The project I have created will continuously acquire the numbers for each candidate in each state, and store the information into a table for each state. For a select few swing states, I will also be acquiring specific county results for the candidates and storing that data into separate tables.\
Each state's table will obtain the following information:
- Date/Time data acquired
- Leading Candidate
- Voting Percent of Leading Candidate
- Vote Count of Leading Candidate
- Trailing Candidate
- Voting Percent of Trailing Candidate
- Vote Count of Trailing Candidate
- Estimated Reported Percent

<!-- end of the list -->

The swing states' detail tables will include the following extra information about each COUNTY:
- Name of the county
- Date/Time data acquired
- Leading Candidate
- Voting Percent of Leading Candidate
- Vote Count of Leading Candidate
- Trailing Candidate
- Voting Percent of Trailing Candidate
- Vote Count of Trailing Candidate
- Estimated Reported Percent

<!-- end of the list -->

I can only provide county data for select swing states as my computer will struggle to handle all of this data coming in from several chrome tabs being open and analyzed simultaneously. The swing states that I will likely be collecting county data include
- Arizona
- Georgia
- Michigan
- Nevada
- North Carolina
- Pennsylvania
- Wisconsin

<!-- end of the list -->

The programs have been tested and function properly on https://www.cnn.com/election/2020/results/president\
This data upon collection will be published where it can then be analyzed by anybody who cares to see it. This will give everyon an opportunity to see the entire picture of exactly what happened in this election from strictly a numbers standpoint. \
DISCRETIONS:
- This data will be collected from https://www.cnn.com/election because they claim to collect their data directly from the Associated Press and their website is a lot easier to navigate and has a very user and computer friendly interface that collecting data will be easier.
- The county results from swing states may vary slightly from the summarized data because the data collection is not perfectly in sync, so an update may occur between collections. Take those discrepancies with a grain of salt, they do not prove that CNN or anybody is directly fudging the numbers, it just proves my computer is working hard and slowing down.
- The purpose of this project is to promote integrity and transparency in a process that many people do not believe to be honest. All of my code is purposely public, can be downloaded and used to ensure it does exactly what I advertise it to do.
- All times in the data are CST, so if you live in a different time zone, make sure to take that into account while reading the data
- IF there is anything truly suspicious in the numbers, spread the data discrepancy to as many people as possible!!!!!
  - d
