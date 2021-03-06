# library-system <br>
a model for a school library system <br>
<h2> Resources: </h2><br>
Trello: https://trello.com/b/a3rDk7LC/library-system <br>
github: https://github.com/rabdallah-99/library-system <br>
Videos: https://www.dropbox.com/sh/mtvw2ef32b7lt78/AACQDV4TiaQlD_FI87mHaRgLa?dl=0  <br>
Risk assessment : https://docs.google.com/spreadsheets/d/1HR6_C_aUr2cwk9Qm1NOSY2wIZ9z--q5OoUCK4qK1BbU/edit#gid=0 <br>

<h2> Contents </h2> <br>
1. <a href="#C1">Project Description and Requirements </a> <br> 
   1.1 <a href="#C2"> Additional Requirements  </a><br>
   1.2 <a href="#C3"> My Approach  </a> <br> 
2. <a href="#C4"> Architecture </a> <br>
   2.1 <a href="#C5"> Design </a> <br>
   2.2 <a href="#C6">CI/CD pipeline </a> <br> 
3. <a href="#C7"> Management and Version Control </a><br>
    3.1 <a href="#B2"> Project Tracking </a> <br>
    3.2 <a href="=#B1"> Use Cases </a> <br>
    3.3 <a href="B3"> Version Control </a><br>
4. <a href="#C8">Risk assessment </a> <br>
5. <a href="#C9"> Testing </a> <br>  <br>   
6. <a href="#C10"> Flask Application Guide </a><br>  
7. <a href="#C11"> Known Issues </a><br>
8. <a href="#C12"> Author </a><br>

1.<b id=C1> Project Description and Requirements </b><br>
    - It was required to create a web application that integrates with a database and demonstrates CRUD functionality.<br>
    - To host and deploy the application using containers <br>
    - To create CI/CD pipeline that will test, build and deploy the application. <br>
    1.1 <b id=C2> Additional Requirements </b> <br>
        Additional to the above requirements there were some deliverables were requested.<br> 
            - A Trello board & Jira board derived from Trello. <br>
            - A relational database, consisting of at least two tables that model a relationship.(ERD & Schema) <br>
            - Documentation of the design phase, application architecture and risk assessment. <br>
            - A python-based Flask application. <br>
            - Test suites for the application. <br>
            - Code hosted into a Version Control System to be built through a CI server and deployed to a cloud-based virtual machine. <br><br>
    1.2 <b id=C3> My approach </b> <br>
           <p> My application is a library system for a school which has a single user (librarian).<br>
      It has implemented CRUD by giving the ability to ADD, READ, UPDATE, DELETE any of the items that builds the system like books, authors, ...etc, which will be explained as below.<br>
      The application statisfy "CRUD" functionality by having the following capabilities. <br>
        - Add Book , Add Category, Add Author, Add Borrower and Add transaction(Borrow book) all these statisfy "Create". <br>
        - Display books, Display Categories, Display Authors, Display Borrowers and Display transactions, all these satisfy "Read". <br>
        - Update books, Update Categories, Update Authors and Update Borrowers, all these satisfy "Update". <br>
        - Delete books, Delete Category, Delete Authors and Delete Borrower all these satisfy "Delete". <br><br>
      The CI/CD pipeline will be explained later, all the application components are containerised using docker.<br>
      Unit Testing is applied with every push to the github repository using github webhooks to automate the testing process, build and deploy.</p> <br><br>


2. <b id=C4> Architecture </b> <br>
   2.1 <b id=C5 >Database Design </b> <br>
         
 <img src="analysis/a.png" alt="ERD mapping to tables" height="750" width="600"> 
As shown in the database mapping diagram that there are many relations between tables and there is many-many relation between books and borrower tables. All the tables in the diagram were implemented except for table login.
To facilitate the queries and the operations two views were created by joining three tables there details are as below:<br>
view vbook was created by joining books, category and authors table. <br>
view borrowbook joins tables transaction, books and borrower. <br> <br>
    2.2 <b id=C6> CI/CD Pipeline </b> <br>
<img src="figures/CI.png"  alt="CI/CD pipeline">
<p >The figure above is the continuous integration pipeline with the associated frameworks and services related to them. This pipeline allows for rapid and simple development-to-deployment by automating the integration process. <br>

Code is written on local machine and pushed to GitHub, which will automatically push the new code to Jenkins via a webhook to be automatically installed on the cloud virtual machine and build docker images and push them to docker hub. From there, tests are automatically run and reports are produced. A testing environment for the app is also run in debugger mode, allowing for dynamic testing. Jenkins deploy docker stack on remote node , the stack contains two services the flask app and mysql database </p>
<img src="figures/infra.png"  alt="infrastructure diagram">
<img src="figures/tier.png"  alt="tier components diagram">
3. <b id=C7> Management and Version Control </b> <br> <br>
    3.1 <b id=B2> Project Tracking </b> <br>
        Trello was used to keep track of what is done and what is still not complete as shown below. <br>
 <img src="figures/trello.png" alt=" Trello board" > <br>
 The board is divided into lists from left to right as the flow of the project : <br>
Backlog: This list is the start of the project it contained all the items which should be done. <br>
User stories: This list contained the functionality that is required to be performed which helps in the coding stage. <br>
To Do : This list contains all items that need to be done but didn't start yet. <br>
Doing:  This list contains all the open items which are currently under development. <br>
Testing: This list contains the items which completed its development and waiting for their unit testing.<br>
Done: this list contains all the finished items. <br> <br>
    3.2 <b id=B1> Use Cases </b> <br>
   The below use cases were used to create the first MVP for the project <br>
    - As a librarian I want to be  able to add borrow transaction so that I keep log of borrowed books <br>
    - As a librarian I want to be able to add new books to the library so that they appear in the system <br>
    - As a librarian I want to be able to modify any data entry error <br>
    - As a librarian I want to be able to return borrowed book, so they become available for borrowing <br>
    - As a borrower I want to see the available books, so I can choose from them <br>
    - As a librarian I want to see a list of late books, so I can take action <br> <br>

 3.3 <b id=B3> Version Control </b> <br>
    git was used as the version control and the code was uploaded to github repository. The repository consists of many feature branches to separate the functionality.<br> 
4. <b id=C8> Risk Assessment </b> <br>
   The risk assessment is found on https://docs.google.com/spreadsheets/d/1HR6_C_aUr2cwk9Qm1NOSY2wIZ9z--q5OoUCK4qK1BbU/edit#gid=0, a screenshot is found below  
<img src="figures/risk.png" alt="Risk Assessment"  >

5. <b id=C9 > Testing </b> <br>
Testing is a crucial part of software development. The pytest framework makes it easy to write small, readable tests,and can scale to support complex functional testing for applications and libraries.
  
<img src="figures/coverage.png" alt="Coverage report"> <br>

6. <b id=C10> Flask Application Guide</b><br>
  As mentioned above about the CRUD functionality satisfied,the below screenshots show a part of the application functionality. <br>
  The application front-end is mainly html there is no css or javascript used thus the very simple appearance.<br>
<b style="color:red"> Add Category </b>
<img src="figures/add category.png" alt="Add Category">

   <b style="color:red"> Add Book </b>
<img src="figures/add book.png" alt="Add book">

<b style="color:red"> Display Category </b>
<img src="figures/dispcat.png" alt="Display Category">

   <b style="color:red"> Display transaction </b>
<img src="figures/disptrans.png" alt="Display Transaction">
    
<b style="color:red"> Delete Category </b>
<img src="figures/delcat.png" alt="Delete Category">

   <b style="color:red"> Update Book </b>
<img src="figures/updatebook.png" alt="Update Book">

 <b style="color:red"> Display late Books </b>
<img src="figures/late.png" alt="Late Book">

<b style="color:red"> Return Books </b>
<img src="figures/return.png" alt="Return Book">

7. <b id=C11> Known issues </b><br>
   <p> I didn't manage to finish the login module so this website doesn't have any authentication method currently. I need to add more validation on data entry. Add Search feature
     The flask app container tends to break giving error " ModuleNotFoundError: No module named 'flask' " which I couldn't resolve so I'm attaching all the pipeline configuration and all other scripts i was going to use </p> <br>
   <img src="figures/jenkins.png" alt="jenkins output". >
8. <b id=C12> Author </b><br>
Riham Ahmed 

