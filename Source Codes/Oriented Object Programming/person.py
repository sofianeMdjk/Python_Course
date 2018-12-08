import BMI
class Person:
    '''This method is the "Constructor" Method, it initializes the attributes, i gave default you can put anything you want'''
    def __init__(self):
        self.student_id = "0"
        self.name = "default"
        self.height = None
        self.weight = None
        self.bmi_comment = ""

    '''     
        def __init__(self, infos):
            information_list = infos.split(",")
            self.student_id = information_list[0]
            self.name = information_list[1]
            self.height = information_list[2]
            self.weight = information_list[3]
            self.bmi_comment = ""
    '''

    def init_informations(self, infos):
        information_list = infos.split(",")
        self.student_id = information_list[0]
        self.name = information_list[1]
        self.height = float(information_list[2])
        self.weight = float(information_list[3])
        ''''We don't even need to call the calculate_bmi method out of our script, we can do it inside our class as you can see'''
        self.calculate_bmi()


    '''Sometimes in classes you'll find methods that return a little description of the attributes of your object'''
    def description(self):
        message = "Hi, My name is :"+self.name+" and i am a student with the id : "+self.student_id+""\
                  "\n"+"I currently weight : "+self.weight+"Kg for about : "+self.height+"m,\napparently i am in a state of : "+self.bmi_comment

        return message

    def calculate_bmi(self):
        self.bmi_comment = BMI.classify_bmi(BMI.body_mass_index(self.weight, self.height))

    def csv_info(self):
        return ",".join([self.student_id, self.name, str(self.height), str(self.weight), self.bmi_comment])

    def csv_info_without_comment(self):
        return ",".join([self.student_id, self.name, self.height, self.weight])

