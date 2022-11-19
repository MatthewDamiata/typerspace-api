# API for [typerspace](https://github.com/benjaminlapidus/typerspace), built with FastAPI

## What is Typerspace?
Typerspace lets users practice their typing skills by following along with the captions to a YouTube video.

## Inspiration
When deciding on an idea for this hackathon, one of our members fondly recalled a typing game that we played in primary school. Unlike modern typing games such as TypeRacer, which are purely text-based, it provided interesting and fun visuals which promoted greater engagement with and passion for the game. We decided that we could apply this same concept in our project by allowing users to engage with interesting content on YouTube while they type, which will ideally let them practice an additional skill without making it seem like work.

## How we built it
Thanks to sponsorships from MLH, Domain.com, and other HackBU sponsors, we were able to host the backend of our site to create a public API using Flask and Heroku that served as the foundation of our project. Building on this foundation, there was a complicated set of components that manipulated the data we created on our servers. Using HTML, Sass, and JavaScript,  we developed a complex front-end experience; dynamically displaying text to multiple means of text entry to slick animations, the front-end of this site used a variety of modern web tools to capture what will be a fantastic user experience.

## Challenges we ran into
The main challenge we ran into was, unsurprisingly, the time limit. We spent a lot of time developing the back-end and front-end of our app, and eventually ran out of time to fully configure our web hosting service through Heroku. The domain can be visited using the provided links, and all necessary files are included, but at the time of writing this only displays a sample home page. Additionally, we decided it would be too difficult to provide support for multiple languages, so we decided to limit it to English. Lastly, the YouTube API we used occasionally supplies captions with characters deemed unsuitable for typing (newline, no-space break, etc), which required us to do a fair bit of data cleaning.

## Accomplishments that we're proud of
The main accomplishment that we're proud of for our back-end development is the creation of our own API using Flask, which interacts with the front-end to supply caption data for any specified YouTube link. On the front-end side of things, we're very proud of the implementation of a text carousel for displaying captions, which allows a smooth transition between lines of text and promotes a simple user experience.

## What we learned
This project was a great opportunity to built an application from scratch with a team of developers, which is something that we obviously don't get to do much. The fact that the hackathon was virtual meant we gained experience in working virtually with tools such as Discord and VSC Live Share, which are very useful tools in these unprecedented times. We also learned a variety of new tools, including Flask, Heroku, and React. Overall, this was a great experience, and we had a blast seeing what we could accomplish in a relatively short time.

## What's next for Typerspace
The first thing we'd like to work on for Typerspace is fixing the configurations with Heroku and making it into a full-fledged, functioning web app. Additionally, we'd like to add typing statistics, support additional languages, allow changes to playback speed, and provide a warning to the user if captions are auto-generated, rather than manually typed. These features, while not crucial for functionality, will significantly improve the quality of user experience.
