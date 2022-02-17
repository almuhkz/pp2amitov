def isgoodmovie(movies):
    moviename = input("Enter the name of a movie: ")
    movie = {}
    for i in movies:
        if moviename == i.get("name"):
            movie.update(i)
            break
    if(len(movie)>0):
        if(movie.get("imdb")>5.5):
            return True
    return False
def goodmovies(movies):
    goodmovies = []
    for i in movies:
        if(i.get("imdb")>5.5):
            goodmovies.append(i)
    return goodmovies
def categories(movies):
    moviecat = input("Enter the category of a movies: ")
    category = []
    category_movie=[]
    for i in movies:
        if(i.get("category")==moviecat):
            category.append(i)
    for i in category:
        category_movie.append(i.get("name"))
    return category_movie
def average_score(movies):
    txt = input("Enter movie names separated with ',': ")
    movienames = txt.split(",")
    all_point = 0
    for i in movienames:
        for j in movies:
            if(i == j.get("name")):                                
                all_point += j.get("imdb")
    return all_point/len(movienames)
def categories_average(movies):
    moviecat = input("Enter the category of a movies to compute average score in a category: ")
    category_movie=[]
    all_point = 0
    for i in movies:
        if(i.get("category")==moviecat):
            category_movie.append(i)
            all_point += i.get("imdb")
    return all_point/len(category_movie)
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
print(isgoodmovie(movies))
print(goodmovies(movies))
print(categories(movies))
print(average_score(movies))
print(categories_average(movies))