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