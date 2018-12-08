from person import Person

def get_informations(file_path):
    '''list that'll contain object of our type "Person"'''
    persons = []
    with open(file_path, "r") as information_file:
        persons_info = information_file.readlines()
        for line in persons_info:
            '''Instantiation of an object of type "Person", the special method __init__ of our class is called'''
            person = Person()
            '''Calling the init_information method, this method will automatically give values to our attributes'''
            person.init_informations(line)
            persons.append(person)
        information_file.close()
    return persons


def comment_file(persons):
    with open("infos_commented.csv","w") as information_file:
        for person in persons:
            '''The method csv_info of our class returns a string in csv format that contains the person's information'''
            line = person.csv_info()+"\n"
            information_file.write(line)
        information_file.close()


informations = get_informations("infos.csv")
comment_file(informations)
