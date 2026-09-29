def assign_to_team(teams, person, team_name):
    # TODO: assign `person` to `team_name`, unless they're already on
    # any team. Return a new dict; do not mutate the input.
    new_teams = teams.copy()
 
    for team in teams:
        if person in teams[team]:
            return teams
    
    if team_name not in new_teams:
        new_teams[team_name] = [person]
    else:
        new_teams[team_name] = new_teams[team_name].copy()
        new_teams[team_name].append(person)

    return new_teams


def team_skill_coverage(teams, people_skills, team_name):
    # TODO: return the union of skills held by everyone on `team_name`.
    # Return an empty set if the team doesn't exist.
    unique = set()

    if team_name not in teams:
        return set()
    
    for person in teams[team_name]:
        if person in people_skills:
            skills = people_skills[person]
        else:
            skills = set()
        unique.update(skills)
    
    return unique


print(assign_to_team({}, 'Ada', 'Backend'))
print(assign_to_team({'Backend': ['Ada']}, 'Bola', 'Backend'))
print(assign_to_team({'Backend': ['Ada']}, 'Ada', 'Frontend'))
print(team_skill_coverage({'Backend': ['Ada', 'Bola']}, {'Ada': {'pyhton'}, 'Bola': {'pyhton', 'sql'}}, 'Backend'))
print(team_skill_coverage({}, {}, 'Frontend'))