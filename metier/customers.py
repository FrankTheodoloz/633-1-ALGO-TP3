from domaine.customer import Customer


class CustomerTree:

    def __init__(self) -> None:
        self.root: Customer = None
        self.size = 0

    def build_tree(self, costumers: list, relations: list) -> None:
        """
        Utilise les listes de clients et de relations pour créer un arbre
        :param costumers: liste de clients
        :param relations: liste de relations
        """
        # TODO: Votre code ici
        pass

    def add(self, customer: Customer, to: Customer) -> None:
        """
        Ajoute un client à l'arbre
        :param customer: client à ajouter à l'arbre
        :param to: client qui à invité le client à ajouter
        """
        # TODO: Votre code ici
        pass

    def remove(self, customer: Customer) -> None:
        """
        Supprime un client de l'arbre. Supprime également tous les fils de ce client
        :param customer: Le client à supprimer
        """
        # TODO: Votre code ici
        pass

    def get(self, customer: Customer) -> Customer:
        """
        Retourne un élément de l'arbre
        :param customer: Le client à trouver
        :return: le client trouvé
        """
        # TODO: Votre code ici
        return None

    def get_average_age(self) -> float:
        """
        Calcule la moyenne d'âge des clients présents dans l'arbre
        :return: la moyenne d'âge
        """
        # TODO: Votre code ici
        return 0.0

    def get_average_invitations(self) -> float:
        """
        Calcule le nombre d'invitations moyen par client
        :return: la moyenne des invitations
        """
        # TODO: Votre code ici
        return 0.0

    def get_row(self, n_row: int) -> list:
        """
        Retourne une liste contenant les clients se trouvant à une certaine profondeur
        :param n_row: numéro de la profondeur
        :return: liste de clients
        """
        # TODO: Votre code ici
        return None

    def linear_sort_by_job(self, job_contains: str) -> list:
        """
        Retourne une liste triée contenant les clients dont leur job contient un certain string au début de la liste.
        Par exemple, tous les "IT" au début de la liste et ensuite les autres.
        :param job_contains: le contenu à chercher dans le job des clients
        :return: liste de clients
        """
        # TODO: Votre code ici
        return None

    def linear_sort_by_class_age(self, classes: list) -> list:
        """
        Retourne une matrice contenant n-classes. Chaque ligne de cette liste contient les clients se trouvant
        dans une classe d'âge donnée
        :param classes: liste de classes d'âge - [10, 15, 20, 25]
                                                Ceci veut dire que vous avez 3 classes d'âge (ou 3 listes) :
                                                [10, 15[, [15, 20[, [20, 25[

        :return: matrice contenant les clients se trouvant dans une classe d'âge
        """
        # TODO: Votre code ici
        return None

    def __str__(self) -> str:
        """
        Retourne une représentation en string de l'arbre sous la forme suivante :
        Customer Remy Reese
        |__Customer Allison Bingham
        ||__Customer Julius Morrison
        |||__Customer Alba Ripley
        ....
        |__Customer Barney Curtis
        ||__Customer Cristal Gardner
        |||__Customer Abdul Archer
        ||||__Customer Barry Ranks
        ||||__Customer ...

        :return: représentation de l'arbre
        """
        # TODO: Votre code ici
        return None
