class MarksheetBean:

    def __init__(self):
        self.__id = 0
        self.__rollNo = 0
        self.__name = ''
        self.__physics = 0
        self.__chemistry = 0
        self.__maths = 0

    # Getter and Setter for id
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    # Getter and Setter for rollNo
    def get_rollNo(self):
        return self.__rollNo

    def set_rollNo(self, rollNo):
        self.__rollNo = rollNo

    # Getter and Setter for name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    # Getter and Setter for physics
    def get_physics(self):
        return self.__physics

    def set_physics(self, physics):
        self.__physics = physics

    # Getter and Setter for chemistry
    def get_chemistry(self):
        return self.__chemistry

    def set_chemistry(self, chemistry):
        self.__chemistry = chemistry

    # Getter and Setter for maths
    def get_maths(self):
        return self.__maths

    def set_maths(self, maths):
        self.__maths = maths