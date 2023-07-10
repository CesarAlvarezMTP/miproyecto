Feature: Feature Requests

 Scenario: suma GET
   Given el usuario está registrado
   When cuando introduce un nombre de usuario
   And cuando introduce su password
   And el usuario pulsa "Login"
   Then el usuario accede al portal

 Scenario: suma POST
   Given el usuario está registrado
   When cuando introduce un nombre falso de usuario
   And cuando introduce su password
   And el usuario pulsa "Login"
   Then el usuario no accede al portal