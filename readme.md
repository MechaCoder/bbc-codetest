#bbc coding test

## Technical Question
### 1. We're looking for people with a real passion for collaboratively creating great software. Please give an example of a software component you have designed and written from concept to deployment, outlining the steps you took. (1000 character limit).
***mysite***
A new component I did was to an addition to my site (a project that involved using react and Python to build a small scale site to show case and learn skills). The element was a CV Builder thought would hold data about my experience. With different languages and then download as a '.doc.' (ms word document). I started by writing, what I needed to do on a whiteboard. And next came the research I needed to look at at the tools I needed to use.

***aws***
Something else on a much bigger scale which was an issue in the performance of the image rendering, the images rendered in fast enough and in the case of a page that had a lot of images the page would hang and not perform correctly. Because the pictures were served from Amazon s3 bucket, this was slowing down the render. I found a solution where the files regularly requested images were stored on the server and thus be served more quickly. This was done through writing the component that would pull the copy the file from s3 and place it on the server, and the images were deleted by a cron'd 'job' that was set to run once a day.

### 2. Using the example that you provided above, tell us about a significant decision you made to solve a technical challenge. Give details of technologies that you chose and why you chose them. (1000 character limit)
With the AWS  example, the biggest problem I found was the fact that the software was using `cfcontent` ([link](http://openbd.org/manual/?/tag/CFCONTENT)) to serve the images; this meant that the to get the image the following happens. Because of the way this setup worked the software was making a request and then one to Amazon s3. This meant that on a page such as a gallery that could have as many as 300 images each would have to make two requests each.

by writing each file to the server, this meant that while the first request would be a little slow, all requests could be served as quickly as possible.

### 3. Using the example that you provided above, tell us about how you ensured your software was fit for purpose and of high quality. What did you learn and what would you do differently next time to do a better job? (1000 character limit)
Because the issue was something to do with the performance it was tested manually over 25 requests (me refreshing the page) using a gallery that had 15 images and timing requests completion time and putting into a spread sheet and there was compassion with times taken before fixed before. I would in the feature be using something like `Nightwatch` to automate the testing,

## Coding Challenge
I have been asked to make a tool that will convert an integer between 1 and 3999 to a sting of the entered integer as represented by the roman system.

### setting up and running to run the code
While you should not need a virtualvenu to execute the project, I have used tools to ensure the quality of the code. I have used `mypy` (type checking) and `coverage.py` (how much of the code is ran) the report which is held in `coverage_report`. To Run this code, you will need `Python 3.5` or greater. And using the following command `python3.5 numeral_unittest.py`. This code has been written on a Linux machine
