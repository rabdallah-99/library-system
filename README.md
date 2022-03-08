# library-system <br>
a model for a school library system <br>
<h2> Resources: </h2><br>
Presentation: add link here <br>
Trello: https://trello.com/b/a3rDk7LC/library-system <br>
Website:   add url <br>
github: https://github.com/rabdallah-99/library-system
Risk assessment : add link here <br>

<h2> Contents </h2> <br>
1. <a href="#C1">Project Description and Requirements </a> <br> 
   1.1 <a href="#C2"> Additional Requirements  </a><br>
   1.2 <a href="#C3"> My Approach  </a> <br> ( A technical description of how the application works.)
2. Architecture <br>
   2.1 Database <br>
   2.2 CI/CD  <br> ( technical description of how the pipeline works.)
3. Project Management and Version Control <br>
4. Risk assessment <br>
5. Testing  <br>  report on the success and code coverage of your unit tests. <br>
6. 

1.<b id=C1> Project Description and Requirements </b><br>
    - It was required to create a web application that integrates with a database and demonstrates CRUD functionality.<br>
    - To host and deploy the application using containers <br>
    - To create CI/CD pipeline that will test, build and deploy the application. <br>
    1.1 <b id=C2> Additional Requirements </b> <br>
    1.2 <b id=C3> My approach </b> <br>
          My application is a library system for a school which have only one user (librarian).<br>
          It has implemented CRUD by giving the ability to ADD, READ, UPDATE, DELETE any of the items that builds the system like books, authors, categories, borrowers...<br>
        The CI/CD pipeline will be explained later, all the application components are containerised using docker.<br>
        Unit Testing is applied with every push to the github repository using github webhooks to automate the testing process, build and deploy.<br><br>


         

Any future improvements you would make.

You must use diagrams to illustrate your work as much as possible and opt for a succinct writing style. Examples of diagrams to include are:

    Entity Relationship Diagram (ERD).
    A full CI/CD pipeline diagram.
    An infrastructure diagram, illustrating the cloud resources and how they network together.
    A component-level diagram, illustrating how the application interfaces with the database.

