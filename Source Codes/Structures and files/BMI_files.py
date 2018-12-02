from BMI import bmi_classify
def get_informations(file_path):
    informations = {}
    with open(file_path,"r") as information_file:
        persons_info = information_file.readlines()
        for person in persons_info:
            tmp = person.split(",")
            mat = tmp[0]
            first_name = tmp[1]
            height = float(tmp[2])
            weight = float(tmp[3].strip("\n"))
            informations[(mat,first_name)]=(height,weight)
        information_file.close()
    return informations

def comment_file(informations):
    with open("infos_commented.csv","w") as information_file:
        for id, infos in informations.items():
            mat, name = id
            height, weight = infos
            comment = bmi_classify(weight,height)
            information = [mat,name,str(height),str(weight),comment]
            line = ",".join(information) + "\n"
            information_file.write(line)
        information_file.close()

informations = get_informations("infos.csv")
comment_file(informations)
