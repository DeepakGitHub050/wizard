Here as the problem statement defines we have came with the solution of smart hotel check in and also adding some functionalities to our product 
which will be helpful for users like the problems of queue for check in,  manual billing and many more.
So at a time we are trying to solve two problem statements i.e "Take out the human interaction" and "Smooth the step in".

Here we are introducing:
Website- used for hotel rooms booking
An App- for hotel check in
An IoT setup - used for setup of local server and to provide user the security while hotel check in process

Taking the example of an user name XYZ. Lets cover his journey from hotel booking to check in:-
1. Firstly he will be booking the room through our website by filling up his details.
2. While booking an unique no. will be alloted to him which he must note down.
3. While hotel check in he will not be given any keys or will not make any physical contacts to room's door for opening or closing purpose.
4. He will be connecting our app( MIT app) which will only run on the local server as setup in hotel.
5. Now he will login in app through the unique no.( as given in point 2).
6. Simultaneously an IoT setup installed above the door( as shown in Simulink) will check his presence.
7. When the sensor will detect his presence, the QR code will get displayed on screen beside of door lock.
8. If the password entered by him is correct, he will be given option of "open" and "close".
9. Through open, a QR code scanner screen will appear. He will be scaning those code and if the code is valid the door will get open.

We have tried to provide much security and privacy while hotel checkin. Here the admin panel plays an important role for it.

1. Admin will be alloting an unique id to each room with unique no. of user.
2. For notification, when the user will come under the range of Human sensor and will scan the QR code successfully, admin will recieve notifivation
   of it.
