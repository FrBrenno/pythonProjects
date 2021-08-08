class Body():
    """Body object will be showed in the screen"""

    def __init__(self):
        pass
        
    head_status = False
    body1_status = False
    l_arm_status = False
    r_arm_status = False
    body2_status = False
    l_leg_status = False
    r_leg_status = False

    dead_status = False

    head = "O"
    body = "|"
    l_member = "/"
    r_member="\\"
    dead="---"


    def show(self):

        print(" {} ".format(self.head)) if self.head_status else ''
        print("{}".format(self.dead)) if self.dead_status else ''
        print("{}{}{}".format(self.l_member if self.l_arm_status else ' ', self.body if self.body1_status else ' ', self.r_member if self.r_arm_status else ' ')) 
        print(" {} ".format(self.body)) if self.body2_status else ''
        print("{} {}".format(self.l_member if self.l_leg_status else ' ',  self.r_member if self.r_leg_status else ' '))

    def ch_status(self, nb_errors):
        if nb_errors == 0 : pass
        elif nb_errors == 1 : self.head_status = True
        elif nb_errors == 2 : self.body1_status = True
        elif nb_errors == 3 : self.l_arm_status = True
        elif nb_errors == 4 : self.r_arm_status = True
        elif nb_errors == 5 : self.bodys2_status = True
        elif nb_errors == 6 : self.l_leg_status = True
        elif nb_errors == 7 : 
            self.r_leg_status = True 
            self.dead_status = True
        else:
            print("Something in the game went wrong. Description : Body class, change status method.")



