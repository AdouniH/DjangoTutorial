
x1 = {"day": "20/12/2019", "day_name": "samedi", "hour": "16:30", "id": 1, "comparator": 20191220}
x2 = {"day": "20/12/2019", "day_name": "samedi", "hour": "17:30", "id": 5, "comparator": 20191220}
x3 = {"day": "21/12/2019", "day_name": "samedi", "hour": "16:30", "id": 2, "comparator": 20191220}

l = [x1, x2, x3]
context = {"crenaux": [{
    "day": "20/12/2019",
    "day_name": "samedi",
    "comparator": 20191220,
    "hours": [{"hour": "16:30", "id": 1},
              {"hour": "16:30", "id": 5}]
}, {
    "day": "21/12/2019",
    "day_name": "samedi",
    "comparator": 21191220,
    "hours": [{"hour": "16:30", "id": 2}]
}]}


def arrange(l):

    b = []
    for i in l:
        b.append(i["comparator"])
        b = list(set(b))

    dico = {}
    c = []
    for j in b:
        toto = {}
        for i in l:
            if i["comparator"] == j:
                if not toto:
                    toto = {
                            "day": i["day"],
                            "day_name": i["day_name"],
                            "comparator": i["comparator"],
                            "hours": [{"hour": i["hour"], "id": i["id"]}]
                        }
                else:
                    toto["hours"].append({"hour": i["hour"], "id": i["id"]})
        c.append(toto)

    b.sort()
    sorted = []
    for i in b:
        for j in c:
            if i == j["comparator"]:
                sorted.append(j)
    return sorted

if __name__ == "__main__":
    x1 = {"day": "20/12/2019", "day_name": "samedi", "hour": "16:30", "id": 1, "comparator": 20191220}
    x2 = {"day": "20/12/2019", "day_name": "samedi", "hour": "17:30", "id": 5, "comparator": 20191220}
    x3 = {"day": "21/12/2019", "day_name": "samedi", "hour": "16:30", "id": 2, "comparator": 21191220}

    l = [x1, x2, x3]
    print(arrange(l))