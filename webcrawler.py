import requests
from bs4 import BeautifulSoup
from csv import writer




"""
EXAMPLE--
    <article>
      <h4 class="section-heading">
        <a href="/blog/student-interview-paula-miranda">Student Interview: Paula + Miranda on Company Projects</a>
      </h4>
      <div class="card">
        <time pubdate="" datetime="2018-06-05"></time>
        <p>At Rithm, we believe that one of the best ways to prepare students for jobs as web developers is by giving them opportunities to work on real-world projects. Working on personal projects can be fun, but working in a team or on an existing code base gives students insights into the day-to-day challenges of a developer that they might not otherwise learn. Our 6th cohort is nearing the end of working on these projects, so we spoke with our students Miranda Howitt and Paula Goyanes to get their perspective on the experience.</p>

          <p><a href="/blog/student-interview-paula-miranda">Continue Reading</a></p>
        <h4 class="service-heading"><small>June 05, 2018</small></h4>
      </div>
    </article>
"""
### Beautiful Soup is a Python library for pulling data out of HTML and XML files.


response = requests.get("https://www.rithmschool.com/blog?page=1")
soup = BeautifulSoup(response.text,"html.parser")

### <span class = "page"></span>
pages = soup.find_all(class_="page")


### index is for counting pages
index = 0

### blog.csv is a comma separated file

with open("blog.csv","w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["DATETIME","LINK","TEXT"])
    

    for page in pages:
        
        index +=1
        response = requests.get("https://www.rithmschool.com/blog?page="+str(index))
        soup = BeautifulSoup(response.text,"html.parser")
        

        ### <article> .....</article>
        articles = soup.find_all("article")
        
        #print("PAGE NO--"+str(index))
        csv_writer.writerow(["PAGE NUM",index])
        for i in articles:
            
            
            ### <time pubdate="" datetime="2018-06-05"></time>
            datetime = i.find("time")["datetime"]
            
            ### <a href="/blog/student-interview-paula-miranda">Student Interview: Paula + Miranda on Company Projects</a>
            url = i.find('a')["href"]
            
            ### {Student Interview: Paula + Miranda on Company Projects} in 'a' tag
            text = i.find('a').get_text()
            
            #print(datetime,url,text)

            csv_writer.writerow([datetime , url , text])
            





    