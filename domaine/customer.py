import datetime


class Customer:

    def __init__(self, id: int, first_name: str = None, last_name: str = None, email: str = None,
                 date_birth: datetime = None, job_title: str = None) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_birth = date_birth
        self.job_title = job_title
        self.invitations = []

    def get_id(self) -> int: return self.id

    def add_invitation(self, invitation) -> None:
        """
        Ajoute un client à la liste des clients invités
        :param invitation: un client
        """

        self.invitations.append(invitation)

    def get_age(self) -> int:
        """
        Calcule l'âge du client en se basant sur la date de naissance
        :return: int qui correspond à l'âge de la personne
        """

        today = datetime.date.today()

        # when the month and day are in future, remove 1
        return today.year - self.date_birth().year - (
                (today.month, today.day) < (self.date_birth().month, self.date_birth().day))

    def __str__(self) -> str:
        return "Customer {0} {1}".format(self.first_name, self.last_name)
