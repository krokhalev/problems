def best_max(matches_data):
    best_score = 0
    max_matches = 0
    for _, value in matches_data.items():
        if best_score < value["score"]:
            best_score = value["score"]
        if max_matches < value["winnable_matches"]:
            max_matches = value["winnable_matches"]

    return best_score, max_matches


def football_table():
    raw_matches_data = input().split(", ")
    matches_data = {}
    for match in raw_matches_data:
        m = match.split(" - ")
        s = m[-1].split(":")
        if s[0] > s[1]:
            # first team
            if matches_data.get(m[0]):
                history = matches_data[m[0]]["history"]
                history.append("W")
                matches_data[m[0]]["history"] = history
                score = matches_data[m[0]]["score"]
                score += 3
                matches_data[m[0]]["score"] = score
                winnable_matches = matches_data[m[0]]["winnable_matches"]
                winnable_matches += 1
                matches_data[m[0]]["winnable_matches"] = winnable_matches
            else:
                matches_data[m[0]] = {
                    "history": ["W"],
                    "score": 3,
                    "winnable_matches": 1
                }
            # second team
            if matches_data.get(m[1]):
                history = matches_data[m[1]]["history"]
                history.append("L")
                matches_data[m[1]]["history"] = history
            else:
                matches_data[m[1]] = {
                    "history": ["L"],
                    "score": 0,
                    "winnable_matches": 0
                }
        elif s[0] < s[1]:
            # second team
            if matches_data.get(m[1]):
                history = matches_data[m[1]]["history"]
                history.append("W")
                matches_data[m[1]]["history"] = history
                score = matches_data[m[1]]["score"]
                score += 3
                matches_data[m[1]]["score"] = score
                winnable_matches = matches_data[m[1]]["winnable_matches"]
                winnable_matches += 1
                matches_data[m[1]]["winnable_matches"] = winnable_matches
            else:
                matches_data[m[1]] = {
                    "history": ["W"],
                    "score": 3,
                    "winnable_matches": 1
                }
            # first team
            if matches_data.get(m[0]):
                history = matches_data[m[0]]["history"]
                history.append("L")
                matches_data[m[0]]["history"] = history
            else:
                matches_data[m[0]] = {
                    "history": ["L"],
                    "score": 0,
                    "winnable_matches": 0
                }
        else:
            if matches_data.get(m[0]):
                history = matches_data[m[0]]["history"]
                history.append("D")
                matches_data[m[0]]["history"] = history
                score = matches_data[m[0]]["score"]
                score += 1
                matches_data[m[0]]["score"] = score
            else:
                matches_data[m[0]] = {
                    "history": ["D"],
                    "score": 1,
                    "winnable_matches": 0
                }
            # second team
            if matches_data.get(m[1]):
                history = matches_data[m[1]]["history"]
                history.append("D")
                matches_data[m[1]]["history"] = history
                score = matches_data[m[1]]["score"]
                score += 1
                matches_data[m[1]]["score"] = score
            else:
                matches_data[m[1]] = {
                    "history": ["D"],
                    "score": 1,
                    "winnable_matches": 0
                }

    winners = []
    for i in range(1, 3+1):
        teams = {}
        best_score, max_matches = best_max(matches_data)

        for name, value in matches_data.items():
            if value["score"] == best_score and value["winnable_matches"] == max_matches:
                teams[name] = matches_data[name]
                teams[name]["place"] = i

        winners.append(teams)

        for team in teams:
            if matches_data.get(team):
                matches_data.pop(team)
            else:
                continue

    return winners, len(raw_matches_data), matches_data


def print_winners():
    winners, count_matches, losers = football_table()

    count = 1
    for teams in winners:
        for team, value in teams.items():
            print(f"|{count}|  {team} - {value['history']}  |{value['score']}|{value['place']}|")
            count += 1

    for team, value in losers.items():
        print(f"|{count}|  {team} - {value['history']}  |{value['score']}| |")


print_winners()
