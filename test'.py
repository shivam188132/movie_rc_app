import requests

# url = "https://api.themoviedb.org/3/movie/19995?api_key=8a5a4bb0bf23e25aaeb0c8b917338db6"
#
# headers = {
#     "accept": "application/json",
#     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4YTVhNGJiMGJmMjNlMjVhYWViMGM4YjkxNzMzOGRiNiIsInN1YiI6IjY1OGQ2NmNjYTMzNjEyNWI5OTU4ZWVhMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zbsRu4BHilwxZ-7j7xAa6NBIboZOowq2x68puP1LxSg"
# }
#
# response = requests.get(url)
#
# print(response.text)
def movie_poster(id):
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{id}?api_key=8a5a4bb0bf23e25aaeb0c8b917338db6").json()
    full_url = "https://image.tmdb.org/t/p/w500/" + response['poster_path']
    print(full_url)
    print(type(full_url))


movie_poster(19995)