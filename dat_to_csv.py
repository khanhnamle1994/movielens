# This script expects a directory structure like this:
#
# dat_to_csv.py
# dat/
#     movies.csv
#     ratings.csv
#     users.csv
# csv/
#

files = {
    "movies" : "movie_id,title,genres",
    "ratings": "user_id,movie_id,rating,ts",
    "users"  : "user_id,gender,age,occupation,zip"
}
DELIM = ","
for name in files:
  with open("dat/%s.dat" % name) as src:
    with open("csv/%s.csv" % name, "w") as dst:
      headers = files[name] + "\n"
      data = src.read().replace(DELIM,"`").replace("::",DELIM)
      dst.write(headers + data)
