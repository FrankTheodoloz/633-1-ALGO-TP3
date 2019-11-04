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

    def add_invitation(self, invitation) -> None:
        """
        Ajoute un client à la liste des clients invités
        :param invitation: un client
        """
        # TODO: Ajouter un client à la liste d'invitations
        pass

    def get_age(self) -> int:
        """
        Calcule l'âge du client en se basant sur la date de naissance
        :return: int qui correspond à l'âge de la personne
        """

        # TODO: Comparer la date de naissance et la date d'aujourd'hui pour connaître l'âge de la personne
        return -1
