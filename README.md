# pythonproject
The goal of this project is to familiarize yourself with Python syntax, and some basic tasks that are common in systems programming and administration. 

![python](https://www.python.org/static/opengraph-icon-200x200.png)
![vscode](https://seeklogo.com/images/V/visual-studio-code-logo-284BC24C39-seeklogo.com.png)

**Here’s the scenario:** you work for a medium sized company that sells widgets directly to consumers through brick-and-mortar retail stores. The marketing department wants to try a new promotional campaign to ramp up direct internet sales, but needs better data about current traffic to your website. Your boss has asked you to take the HTTP server logs from the webserver and provide some analytics to Marketing.

This is my python program that reads from http_access_log.txt and returns back the total amount of requests that were made and the total amount of requests that were made in the year '1995'.

When running this program, you may need to wait until the dots finishing printing to see the last year requests and the total requests.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Marketing was very happy with the data you provided them. Now they want more. They have asked that you answer more questions  so they have a better idea about the nature of the visitors that are coming to the company website.

Marketing is asking for answer to the following questions:

1) How many requests were made on each day? 
2) How many requests were made on a week-by-week basis? Per month?
3) What percentage of the requests were not successful (any 4xx status code)?
4) What percentage of the requests were redirected elsewhere (any 3xx codes)?
5) What was the most-requested file?
6) What was the least-requested file?

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
This code will print out the number of requests made each day (by actually date, and not average because that is now how I interpreted it).
After printing the dates, my code will take a few moments to print out the percentage of requests that were not successful and then redirected.
