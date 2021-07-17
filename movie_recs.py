import requests

def get_movies_from_tastedive(name):
    kv = {"q":name, "type":"movies", "limit":5}
    page = requests.get("https://tastedive.com/api/similar", params = kv)
    #print(page.json())
    return page.json()

def extract_movie_titles(data):
    ret = []
    for x in data['Similar']['Results']:
        ret.append(x['Name'])
    return ret

def get_related_titles(input_list):
    final_list = []
    for movie in input_list:
        unfiltered = extract_movie_titles(get_movies_from_tastedive(movie))
        for related_movie in unfiltered:
            if related_movie not in final_list:
                final_list.append(related_movie)

    return final_list

def get_movie_data(name):
    kv = {"t":name, "r":"json"}
    page = requests.get("http://www.omdbapi.com/", params = kv)
    #print(page.json())
    return page.json()

def get_movie_rating(json_result):
    for ratings in json_result['Ratings']:
        if ratings['Source'] == 'Rotten Tomatoes':
            return int(ratings['Value'][:2])
    return 0

def get_sorted_recommendations(input_list):
    #print(input_list)
    unsorted = {}
    for movie_result in get_related_titles(input_list):
        unsorted[movie_result] = get_movie_rating(get_movie_data(movie_result))
    sorted_output = sorted(unsorted, key=lambda x: (unsorted[x], x), reverse=True)
    return sorted_output
    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

