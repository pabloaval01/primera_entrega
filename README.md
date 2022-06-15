# Personalized music library

## In the personalized music library you can enter artists and albums related to the Grunge, Punk and Funk genres. The URL box is made up as follows:

| URL                    | Descrition           |
| ---------------------- | ---------------------| 
| /                      | Home Page            |
| /grungeArtistForm      | Record Grunge Artist |
| /punkArtistForm        | Record Punk Artist   |
| /funkArtistForm        | Record Funk Artist   |
| /albumGrungeForm       | Record Grunge Album  | 
| /albumPunkForm         | Record Punk Album    |
| /albumFunkForm         | Record Funk Album    |

<br />


## To perform searches, please use the following

| URL                        | Descrition                         |
| -------------------------- | -----------------------------------| 
| /searchGrungeArtist        | Search Form for Grunge Artists     |
| /searchGrungeArtist_result | Grunge Artists Search Results Form |
| /searchGrungeAlbum         | Search Form for Grunge Album's     |
| /searchGrungeAlbum_result  | Grunge Album's Search Results Form |
| /searchPunkArtist          | Search Form for Punk Artists       | 
| /searchPunkArtist_result   | Punk Artists Search Results Form   |
| /searchPunkAlbum           | Search Form for Punk Album's       |
| /searchPunkAlbum_result    | Punk Album's Search Results Form   |
| /searchFunkAlbum           | Search Form for Funk Album's       |
|searchFunkAlbum_result      | Funk Album's Search Results Form   |


# Install dependencies from the "Requirements.txt" file

<br />

# Adaptation of environments:

## Modify the paths of the templates in "settings.py" by those corresponding to your local environment. Also modify the template loading route, in the Bootstrap "Padre.html" template itself, to point to the local environment.


```
Biblioteca/
     ├── settings.py
     └── Artistas
          └── templates/
                └── Artistas
                    └── padre.html


```