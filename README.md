# A-algorithm-Autonomous-navigatioon-vehicle-
Automation is revolutionized in every field. This significantly reduces the human efforts. Recently there has been a lot of hype around autonomous vehicles. The introduction of autonomous vehicles such as Tesla has made some remarkable progress in terms of traffic management. There have also been a lot of improvements in the localisation but the only problem is the cost of implementation. Autonomous vehicles use some of the expensive sensors like lidar, Radar, and GPS. This is too expensive when it comes to small scale, like in a home, office, or industry field. We came up with a solution of being able to solve every case using a very cost-effective way. we aim to include every functionality using the programming techniques. some of them include the A* algorithm to find the shortest path between two nodes, and localisation using previously visited points which solves the case of using  GPS. For path following we are using Arduino and serial port connections.


[For more details click here visit documentation ](https://drive.google.com/file/d/12j-7yQPndvI09vNL99VdVxRqCRZR_NQ-/view?usp=drive_link)

![Dcoder](https://github.com/KoteshwarChinnolla/A-star-algorithm-based-Autonomous-navigatioon-vehicle-/blob/main/Decoder.png)


  Till now we have focused on how natural language is transformed into locations and finding the shortest path between locations (nodes). the challenge is how we can make the vehicle follow the path. one obvious way is to send the signals to Arduino with motors and motor drivers. as the Arduino contains the code to make sure the motors rotate as per the signals.

but what kind of signals can we send? the signals must be in such a way that they align with the code in the Arduino (this is described in the Arduino section). alignment here means that the directions must be accurately followed by the vehicle. Arduino code just contains the functionalities like (L, R, F, S) where.
    
    > L -> Left
    > R -> Right
    > F -> Forward
    > S -> Stop

  But outputs of the A* algorithm are like (LEFT, RIGHT, RIGHT-UP,..) and it just returns to us the direction it is following. As you can see in the FIG (...) for a sample path the A* algorithm output doesn't describe any turns. as RIGHT-UP to RIGHT, the Vehcle need to rotate about clockwise 45 degrees and RIGHT to UP is about Anti clockwise 90 degrees. As the vehicle rotates in the direction (CLOCK-WISE or ANTI-CLOCKWISE) where the angle of rotation is less.To make sure that we are considering both Anti-Clockwise and Clockwise. Anti-clockwise indicate turning left and clockwise indicates turning right. But it is only applicable when there is a change in direction like Right-UP to Right, Right to Up etc.. if there is same direction such as RIT-UP to RIGHT-UP, LEFT to LEFT we represent it as Forward (f). Clockwise 45 can be known to be one time Right as one right and one left turn represents 45 degrees clockwise and Anti-Clockwise. the same way Clockwise 90 is two times right, Anti clockwise 90 is two times left as signals to the Arduino. 
  
if we apply the same algorithm to the above example by considering it initially Right Direction

we basically follow two steps to make this happen
> 1. Direction to angles
> 2. Ange to signals.
