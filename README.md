# DS4003_evabutler
DS4003 repository for term project

Why I chose this data: 
    I chose this data set because I love the idea of anaylizing a large data set about books! The reviews of the data set are good and people seem to not have problems with it. I found a manipulated version of the origional data set where a Kaggle user scrapped the internet and added genres to the data set. This was the data set I origionally downloaded from Kaggle and later manipulated to form the data.csv file. Overall, the data appears to be trustworthy and accurate. It included genres and titles, which are two things I really want to focus on. I want to be able to possibly look up images based on an isbn number, so I wanted to have that information. I like the idea of being able to look up a list of books based on an author. I like the idea of being able to click on a book and getting a page of information on the book and different comparisons based on its genres. 

Data Provenance:

    ORIGIONAL DATA SET: https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks
        - This is the origional data set that was created by scraping the Goodreads API under the CC0: Public Domain license. It is updated weekly. 

    MANIPULATED DATA SET by Kaggle user: https://www.kaggle.com/datasets/middlelight/goodreadsbookswithgenres/data
        - User added genres by making a call to 'https://www.googleapis.com/books/v1/volumes?q=isbn:' 
        Books for which a genre could not be found were dropped rather than manually added in
        
    PERSONAL MANIPULATIONS TO DATA SET: data.csv 
        - Removed all rows containing N/A values
        - Renamed column headers to follow personal formatting
        - Seperated Genres column into seperate columns for each genre. This was done with the intention of being able to analyze genres seperately. If a book was placed within the genre, it recieved a 1 and if it was not within the genre it recieved a 0. 
        - Next, genres with the same super genre were grouped together to lessen the total number of genres. 
        - Next, a column mapping genres that I determined were neccessary to the data set's genres was applied to the set and new genres were determined. 
        - Finally, I reordered some of the columns, so that they were in my desired order. 

Process of Building the Dashboard:
  To begin, I started by tackling the general layout of the dashboard. Then, I started with creating the genres graph in the center of the page. As we learned in class, I was able to associate genres with different colors. Next, I moved onto developing the authors table on the right side of the page. Based on the author that the user selects, the authors corresponding books will populate the table. Once the table is populated, an automatic blurb is written beneath that says what the authors most popular book is based on a books rating and number of ratings. To end, I constructs the left portion of the page by starting with a book title dropdown. The dropdown also has a search function that allows you to find titles. Once a title is selected, I call the Open Library API using the books corresponding ISPN number to pull the book cover. Underneath the book cover there are three sections that are also populated based on the user's selected title: author name, number of pages, and genres. Underneath the listed genres, there is a button called "Other books by this author". When the user selects this button, the data table on the far right of the page is populated with the rest of the authors books. 

Learning Experiences: 
  Next time I will spend a longer time in the data exploration and cleaning portion of the project. As I was working on constructing the dashboard, I would find errors in the data that eventually messed up part of the funcitonality. Now I know the importance of fully grasping what is present in your data before starting to build anything. 
    On a more positive note, I really enjoyed learning how to implement an API and is a good skill to use in the future. 


Render URL: https://ds4003-evabutler.onrender.com
