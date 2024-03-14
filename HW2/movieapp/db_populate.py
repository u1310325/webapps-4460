import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','movieapp.settings')
django.setup()

from movie.models import Movie, User

# 1.Empty all existing rows
for movie in Movie.objects.all():
    movie.delete()
for user in User.objects.all():
    user.delete()

# 2.Add 10 movie rows
Movie.objects.create(
    title='Cars',
    description='Animated movie about talking cars.',
    director='John Lasseter',
    release_year=2006,
    budget=120000000,
    runtime=117,
    rating='G',
    genre='Animation, Comedy, Family'
)

Movie.objects.create(
    title='Shrek',
    description='Animated movie about an ogre.',
    director='Andrew Adamson, Vicky Jenson',
    release_year=2001,
    budget=60000000,
    runtime=90,
    rating='PG',
    genre='Animation, Adventure, Comedy'
)
Movie.objects.create(
    title='Thor',
    description='Superhero movie about the Norse god Thor.',
    director='Kenneth Branagh',
    release_year=2011,
    budget=150000000,
    runtime=115,
    rating='PG-13',
    genre='Action, Adventure, Fantasy'
)

Movie.objects.create(
    title='Ironman',
    description='Superhero movie about Tony Stark, a billionaire industrialist and inventor who builds a powered exoskeleton and becomes the technologically advanced superhero Iron Man.',
    director='Jon Favreau',
    release_year=2008,
    budget=140000000,
    runtime=126,
    rating='PG-13',
    genre='Action, Adventure, Sci-Fi'
)

Movie.objects.create(
    title='Spiderman',
    description='Superhero movie about Peter Parker, a high school student who gains spider-like abilities after being bitten by a radioactive spider.',
    director='Sam Raimi',
    release_year=2002,
    budget=139000000,
    runtime=121,
    rating='PG-13',
    genre='Action, Adventure, Sci-Fi'
)

Movie.objects.create(
    title='Interstellar',
    description='Science fiction film about a group of astronauts who travel through a wormhole near Saturn in search of a new habitable planet for humanity.',
    director='Christopher Nolan',
    release_year=2014,
    budget=165000000,
    runtime=169,
    rating='PG-13',
    genre='Adventure, Drama, Sci-Fi'
)

Movie.objects.create(
    title='Wall-E',
    description='Animated movie about a robot named WALL-E, who is designed to clean up a polluted Earth, falls in love and embarks on a space journey.',
    director='Andrew Stanton',
    release_year=2008,
    budget=180000000,
    runtime=98,
    rating='G',
    genre='Animation, Adventure, Family'
)

Movie.objects.create(
    title='A Christmas Story',
    description='Comedy film about a young boy named Ralphie who attempts to convince his parents, his teacher, and Santa that a Red Ryder B.B. gun really is the perfect Christmas gift.',
    director='Bob Clark',
    release_year=1983,
    budget=3500000,
    runtime=94,
    rating='PG',
    genre='Comedy, Family'
)

Movie.objects.create(
    title='The Godfather',
    description='Crime film about the aging patriarch of an organized crime dynasty who transfers control of his clandestine empire to his reluctant son.',
    director='Francis Ford Coppola',
    release_year=1972,
    budget=6000000,
    runtime=175,
    rating='R',
    genre='Crime, Drama'
)

Movie.objects.create(
    title='Up',
    description='Animated movie about an elderly widower named Carl Fredricksen and a young Wilderness Explorer named Russell who fly to South America in a house suspended by helium balloons.',
    director='Pete Docter, Bob Peterson',
    release_year=2009,
    budget=175000000,
    runtime=96,
    rating='PG',
    genre='Animation, Adventure, Comedy'
)



#3. Add 3 user rows
User.objects.create(
    username='agrimit',
    password='password1',
    first_name='Alex',
    last_name='Grimit',
    email='user1@example.com'
)

User.objects.create(
    username='lsanders',
    password='password2',
    first_name='Landen',
    last_name='Sanders',
    email='user2@example.com'
)

User.objects.create(
    username='vbrusch',
    password='password3',
    first_name='Victor',
    last_name='Brusch',
    email='user3@example.com'
)

#4. QuerySet Statements
# Retrieve all movies
all_movies = Movie.objects.all()

# Filter for movies starting with some text
startWith = Movie.objects.filter(title__startswith='The')

# Get one movie
movieOne = Movie.objects.get(pk=1)  

# Update one movie
movie_to_update = Movie.objects.get(pk=2)
movie_to_update.title = "New Movie Title"
movie_to_update.save()

# Delete one movie
Movie.objects.filter(pk=5).delete()

# Model Statement
userOne = User.objects.get(username='agrimit')

