# What is this?

**[Go down to the Projects section](#projects)**

I have been coding since I was 15. I've started with Visual Basic and then dove into web. Since then I've been consuming all sorts of knowledge on programming, algorithms, and computers in general.

I'm a physicist, but I have worked as web developer, web designer, graphic designer, social media guru, etc. Besides all of those, I am using computation and automation in my own work all the time. I simulate integrated optical devices, I automate experimental setups, I collect data, I analyse data, I visualise data, and so on...

However I am also very interested in other sorts of data. So I've been fiddling around with web scraping and I've been working on visualizing the data I've collected. So here, I am presenting the results of those works, both the codes and the data.

Since these are very small projects, I intend to list them on one page (with explanations.) However, if a project becomes more involved, then it'll have it's own page.

If you have any questions or comments, you can contact me through these channels:

* Email: [ekarademir@gmail.com](mailto:ekarademir@gmail.com)
* LinkedIn: [ekarademir](https://ie.linkedin.com/in/ekarademir)
* GitHub: [ekarademir](https://github.com/ekarademir)
* Twitter: [plexcitonic](https://twitter.com/plexcitonic)

Enjoy!

<a name="projects"></a>
# Projects
### What were you born for?

If you feel like you are in rut and suspect that it has something to do with your birthday, you might soon be able to find out. In this project I'm collecting birthdays of well known people and matching their zodiac signs with their occupation.

I know that there is no correlation between zodiac signs and occupations (with anything really), but it's an excuse for me to scrape Wikipedia and get me some data.

I've done the first iteration. The **raw results** are here: [data-wikibdays-occupations.csv][wikibdays]. I am yet to implement a visualisation page. But it is coming!

If you are curious about the code that generated above data set you can check the source here: [birthday-wrangler][wikibdays-code].

[wikibdays]:https://github.com/ekarademir/data-sets/blob/master/data-wikibdays-occupations.csv?raw=true
[wikibdays-code]:https://github.com/ekarademir/birthday-wrangler

### Property Listings
This is a work in progress. My aim is to scrape property listings on a popular listing site in Dublin. I've started with a naive approach that just scrapes rent houses for now. However I'm planning to implement [Scrapy][scrapy] library for more robust approach.

Again, results of the first iteration care here: [data-house-rent-listings.csv][property-data]; and the code is here: [property-crawler][property-crawler]

[scrapy]:https://scrapy.org/
[property-crawler]:https://github.com/ekarademir/property-crawler
[property-data]:https://github.com/ekarademir/data-sets/blob/master/data-house-rent-listings.csv

### Old Projects [(GitHub)](https://github.com/ekarademir/old-projects)
Zip archives of few old projects written in PHP. They are not archaic, but they are quite old. Even though I tried to explain everything in comments, it would take a lot of time to go through. However you are free to download them and use them in whichever capacity that you want to use.

These are developed in and for [Bilkent University](http://w3.bilkent.edu.tr/bilkent/), [Department of Physics](http://physics.bilkent.edu.tr/) as I was the TA responsible for everything web related.

I was also the only developer in these applications. So most of the comments are for myself. In some cases, for the unlucky person who might have wanted to add something to them. I tried to follow all basic project development conventions, but my aim was to ger something going, **_very fast_**. So I had to leave few dirty code here and there (_looks around with shifty eyes._)

A bit of explanation about them:

#### [academic-event-management.zip](https://github.com/ekarademir/old-projects/blob/master/academic-event-management.zip)
This application was first developed in May 2008 on a hype web application framework of the time: [CakePHP](https://cakephp.org/). I am a bit surprised that it still exists. I don't know their status now, but back then Cake was a well intended PHP. It was quite ambitious. It was just wright for agile development. However, it was also very hard to write clean code. If the project was huge, it's fine; but if you wanted to try a small thing you had to go load an elephant to crack one nut.

After 2008, the app was used at least 10 times in other consequent events. I've improved it at each iteration. This copy might be the 8th or so. It contains the whole framework too. The app handled registration, abstract upload, registrant confirmation, emailing, page publishing, and finally backups. So there is also a DB backup in webroot folder.

#### [physlab.zip](https://github.com/ekarademir/old-projects/blob/master/physlab.zip)
This one was developed in 2012 summer in 2 weeks. Then it went through 2 months of bug-fixes as it was being used. So I learned quite a lot of project management and application development with this one. It offered classroom management, grade updates by assistants, grade confirmation by TA manager, an online chat box, database backup, etc.

After one term of usage, the professor was lazy to copy **one** column of the grade summary data of his class from the application report to an excel file so he decided, it's not worth to use it. And I was too pissed of to write an excel exporter. So the multi-user management part was shelved. However, later on, the same professor decided they needed some sort of a system to find previous grades of repeating students at the start of each term. So I went ahead and added an archival module that could not only import data from excel files, but also search the grades fast. It is still in use!

For this project I've used **[Zend Framework](https://framework.zend.com/)**. It was light years ahead of Cake and much more robust. It also offered quite a selection of modules to work with. The ability to use only parts of the framework that are needed was another reason to build on Zend. I would still choose Zend Framework if I am to build another PHP application.

#### [seniorproject.zip](https://github.com/ekarademir/old-projects/blob/master/seniorproject.zip)
This was a project developed in an even shorter time frame, The aim was to emulate peer-review style grading for senior students at the senior project course. Even though it was only used twice, [the website](http://www.fen.bilkent.edu.tr/~physics/seniorproject/index.php) is still operational. Built with Zend Framework.
