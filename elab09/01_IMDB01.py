#------------------------------------------- IMDB HEADER -------------------------------------------
# Only 'import json' command is allowed!!!
# Failing to follow this rule, you will get zero mark :_)
import json

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

# specifying the zip file name
filename = "IMDB_movies_merged.json"

### do not forget to uncomment the next line to read json data
data = read_json(filename)
### ----------------------------------------------------------
#------------------------------------------- IMDB HEADER -------------------------------------------


def find_records(data=[], included_actors=[], excluded_actors=[], included_directors=[], excluded_directors=[], sortby='ratingValue'):
        records = []
        for i in range(len(data)):
            d = data[i]
            if 'director' in d:
                if d['director']['name'] in excluded_directors:
                    continue
                actors = [actor['name'] for actor in d['cast']]
                if set(included_actors).issubset(actors) and d['ratingValue'] != '':
                    records.append(d)
        sort_records = sorted(records, key=lambda item: float(item[sortby]), reverse=True)
        return sort_records

def q1():
    sorted_records = find_records(data=data, included_actors=['Harrison Ford'], excluded_directors=['Steven Spielberg'])
    i, rating, directors = 0, '', []
    for d in sorted_records:
        if d['ratingValue'] != rating:
            i += 1
        if i > 5:
            break
        directors.append(d['director']['name'])
        rating = d['ratingValue']
    directors = sorted(directors)
    print("\n".join(directors))

def q2():
    sorted_records = find_records(data=data, included_actors=['Harrison Ford', 'Tommy Lee Jones'], excluded_directors=['Steven Spielberg', 'George Lucas'])
    top1 = sorted_records[0]
    print(top1['name'])


#----- driver code
print('(1) Answer of Q1')
print('(2) Answer of Q2')
ans = input('or just press (Enter): ')
if ans == '1':
  q1()
elif ans == '2':
  q2()
else:
    print('Nothing to do..')
