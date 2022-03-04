# Sports Franchise App
**SQL/Python Portfolio Project Report**

By Jeremy Jeremiah


### Description ###
The NFL Franchise database I've created is a simple database containing 5 NFL teams and there respective stadiums,coaches,
administrative staff, players and equipment for players.

### API Reference Table ###
| Path                              | Method | Parameters         | Name               | Description                                                       |
|-------------------------------    |--------|---------------------------------------------------------|--------------------|------------------------------------------------------------------|
| /teams/16/players_in_team         | GET    |                    | players_in_team    |                                         players who belong to a team                                                  |
| /teams/15/coaches_in_team         | GET    |                    | coaches_in_team    |                                           coaches associated with a team                                            |
| /teams/14/stadium_belongs_to_team | GET    |                    | stadium_belongs_to_team                                  |   RETURNS the stadium associated with team   |
| /teams/17/admins_for_team         | GET    |                    | admins_for_team   
RETURNS all admin staff associated with team                                            |
| /coaches/13/team_for_coaches      | GET    |                    | team_for_coaches                                         |
| /coaches/12/players_for_coach     | GET    |                    | players_for_coach                  
RETURNS the player coached by coach |        |                    |                                                          |
| /players/14/team_for_players      | GET    |                      team_for_players
RETURN the team a player belongs to | GET    |                    |                      |  
|/players/13/coach_for_players      | GET    |                    | coach_for_players
RETURNS the coaches for each player | GET    |
|/players/18/equipment_for_players  | GET    |                    | equipment_for_players
RETURNS the equipment for player    | GET    |
|{{ _.base_url }}/players           | POST   |                    | players 
creates a player
|{{ _.base_url }}/players/15        | PUT    |                    | /players/15
modifies a player
|{{ _.base_url }}/players/16        | DELETE |                    | players/16
delets a player   

### Steps to run ###
1. Add all of the files in folder "franchise" to workspace via command palette

2. Change CMD line in Dockerfile to run flask and use that docker file to build the "franchise" image.

3. Take that franchise image and add it as a base image in docker compose under services

4. Add a postgres base image to docker services, in the docker compose file and create a volume that holds the franchise database, from
   the file system.
   Once the volume in psql is created all the commands is executed from init.sql that will create and seed the database.

5. Execute docker compose up -d to build and run the franchise flask app automatically running flask server, with the corresponding
   postgress database it requires.

