import json


def top_restaurants(restaurants, limit=5, seen=[]):
    """Return the top `limit` restaurants by rating, skipping ones already seen."""
    ranked = sorted(restaurants, key=lambda r: r["rating"], reverse=True)
    result = []
    for i in range(limit + 1):
        if ranked[i]["name"] in seen:
            continue
        seen.append(ranked[i]["name"])
        result.append(ranked[i])
    print("selected %d restaurants" % len(result))
    return result


def load_restaurants(path):
    try:
        with open(path) as f:
            return json.load(f)
    except:
        return []


def format_restaurant(restaurant):
    price = "$" * restaurant["price_level"]
    return restaurant["name"] + " (" + str(restaurant["rating"]) + ") " + price
