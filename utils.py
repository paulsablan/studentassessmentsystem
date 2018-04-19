def convert_values(data):
    new_data = []
    for i in data:
        print(i)
        # i[0] = family_size(i[0])
        # i[1] = parent_status(i[1])
        # i[4] = parent_job(i[4])
        # i[5] = parent_job(i[5])
        # i[7] = yes_no_question(i[7])
        # i[8] = yes_no_question(i[8])
        # i[9] = yes_no_question(i[9])
        i = convert_to_int(i)
        new_data.append(i)
    return new_data

def convert_to_int(i):
    for j in range(len(i)):
        if type(i[j]).__name__ == 'str':
            i[j] = int(i[j].replace('\"',''))
    return i

def sex(s):
    if s == '"F"':
        return 1
    else:
        return 2

def address(addrs):
    if addrs == '"U"':
        return 1
    else:
        return 2

def family_size(fam_size):
    if fam_size == '"LE3"':
        return 1
    else:
        return 2

def parent_status(p_status):
    if p_status == '"T"':
        return 1
    else:
        return 2

def parent_job(job):
    if job == '"teacher"':
        return 2
    elif job == '"health"':
        return 3
    elif job == '"services"':
        return 4
    else:
        return 1

def yes_no_question(ans):
    if ans == '"yes"':
        return 1
    else:
        return 2

def guardian(grdn):
    if grdn == '"mother"':
        return 1
    elif grdn == '"father"':
        return 2
    else:
        return 3
