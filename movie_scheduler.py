current_movies = {"The Grinch": "11h",
                  "Rudolph": "13h",
                  "Frosty the Snowman": "15h",
                  "Chistmas Vacation": "17h"
                  }
print("We're showing the following movies:\n")
for key in current_movies:
    print(key)

movie = input("What movie would you like the showtime for?\n")

showtime = current_movies.get(movie)

if showtime:
    print(movie, "is playing at", showtime)
else:
    print("Requested movie is not available")
