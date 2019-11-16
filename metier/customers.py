from domaine.customer import Customer


class CustomerTree:

    def __init__(self) -> None:
        self.root: Customer = None
        self.size = 0
        self.nb_of_customers: int = 0
        self.sum_of_ages: int = 0
        self.sum_of_invitations: int = 0

    def build_tree(self, costumers: list, relations: list) -> None:
        """
        Utilise les listes de clients et de relations pour créer un arbre
        :param costumers: liste de clients
        :param relations: liste de relations
        """

        # # Option 1 the iteration over the relations list
        # # Duration (w/o output : 2.1s)
        #
        # # runs over the relations using list index as customer id
        # for customer_id in range(1, relations[0]):
        #
        #     # when the customer has invitations
        #     if relations[customer_id].__len__():
        #         cust = costumers[customer_id]
        #
        #         # defines the root once
        #         if self.root is None: self.root = cust
        #
        #         # gets the invitations and adds to the customer
        #         for invited_id in relations[customer_id]:
        #             invited = costumers[invited_id]
        #             cust.add_invitation(invited)

        # Option 2 the recursion supposing that the first id is the root of all invitations
        # Duration (w/o output : 2.2s)
        def recursive_add(cust: Customer) -> None:
            """
            Recursive function
            Adds invitations to a customer and then adds invitations of invitations to invitations and...
            :param cust: the customer who invited
            :return: Nothing
            """

            # some of the last customers have no invitations (index out of range)
            if cust.get_id() <= relations[0]:

                # gets the invitations from the relations list and iterates
                for invited_person_id in relations[cust.get_id()]:
                    # gets the invited customer from the customers list and add it to the customer
                    cust.add_invitation(costumers[invited_person_id])

                    # launch the recursion
                    recursive_add(costumers[invited_person_id])

        # Starts here
        # gets the corresponding customer from the customer list
        customer: Customer = costumers[1]

        # sets the root
        if self.root is None: self.root = costumers[1]

        # calls the recursive function
        recursive_add(customer)

    def add(self, customer: Customer, to: Customer) -> None:
        """
        Ajoute un client à l'arbre
        :param customer: client à ajouter à l'arbre
        :param to: client qui à invité le client à ajouter
        """

        # gets the customer
        cust_in_tree = self.get(to)
        cust_in_tree.add_invitation(customer)

    def remove(self, customer: Customer) -> None:
        """
        Supprime un client de l'arbre. Supprime également tous les fils de ce client
        :param customer: Le client à supprimer
        """

        # if it is the root
        if self.root.id == customer.id:
            self.root = None
        else:  # finds the parent Customer who invited the Customer
            parent: Customer = self.find_parent(customer, self.root)

            # gets the invitation
            temp: Customer = self.find_child(customer, parent)

            # removes the customer from parent's invitations
            parent.invitations.remove(temp)

    def get(self, customer: Customer) -> Customer:
        """
        Retourne un élément de l'arbre
        :param customer: Le client à trouver
        :return: le client trouvé
        """

        # if it is the root
        if self.root.id == customer.id:
            return self.root
        else:  # look for the customer deeper
            return self.find_child(customer, self.root)

    def find_child(self, who: Customer, where: Customer) -> Customer:
        """
        :param who: le client à trouver
        :param where: où chercher le client
        :return: Customer: le client trouvé
        """

        # looks for the parent customer who invited
        parent: Customer = self.find_parent(who, where)

        if parent is not None:
            # runs over the invitations of the parent
            for invitation in parent.invitations:
                if invitation.id == who.id:
                    return invitation
        else:
            print('Erreur : le client', who.id, 'n\'a pas été trouvé')

    def find_parent(self, who: Customer, where: Customer) -> Customer:
        """
        Fonction récursive pour trouver le client qui a invité un certain client
        :param who: le client à trouver
        :param where: où chercher le client
        :return: Customer: le parent contenant le client
        """

        # runs over all the invitations first, no need to go deeper if it is here...
        for invitation in where.invitations:
            # return parent (where) when the customer is found in the invitations
            if invitation.id == who.id:
                return where

        # now, go deeper...
        for invitation in where.invitations:
            temp = self.find_parent(who, invitation)
            if temp is not None: return temp

    def get_average_age(self) -> float:
        """
        Calcule la moyenne d'âge des clients présents dans l'arbre
        :return: la moyenne d'âge
        """
        self.nb_of_customers = 0
        self.sum_of_ages = 0

        def recursive_lookup(customer: Customer) -> None:
            """
            Recursive function that count customers and adds ages
            :param customer:
            :return: None
            """
            self.nb_of_customers += 1
            self.sum_of_ages += customer.get_age()

            # recursive call
            for invitation in customer.invitations:
                recursive_lookup(invitation)

        # launch recursion
        recursive_lookup(self.root)

        return self.sum_of_ages / self.nb_of_customers

    def get_average_invitations(self) -> float:
        """
        Calcule le nombre d'invitations moyen par client
        :return: la moyenne des invitations
        """
        self.nb_of_customers = 0
        self.sum_of_invitations = 0

        def recursive_lookup(customer: Customer) -> None:
            """
            Recursive function that count customers and invitations
            :param customer:
            :return:
            """
            self.nb_of_customers += 1
            self.sum_of_invitations += customer.invitations.__len__()

            # recursive call
            for invitation in customer.invitations:
                recursive_lookup(invitation)

        # launch recursion
        recursive_lookup(self.root)

        return self.sum_of_invitations / self.nb_of_customers

    def get_row(self, n_row: int) -> list:
        """
        Retourne une liste contenant les clients se trouvant à une certaine profondeur
        :param n_row: numéro de la profondeur
        :return: liste de clients
        """
        self.size = 1
        customer_list: list = []

        def find_customers_at_level(customer: Customer) -> None:
            """
            Recursive function that runs over the invitations and builds string
            :param customer:
            :param string:
            :return:
            """
            self.size += 1  # increase level count

            # invitations of customer
            for invited in customer.invitations:  # 2nd level at first pass
                if self.size == n_row:
                    customer_list.append(invited)

                # invitations of customer invited
                if invited.invitations and self.size < n_row:  # no need to go deeper if already at the level !
                    find_customers_at_level(invited)

            self.size -= 1  # decrease level count

        if n_row == self.size:
            customer_list.append(self.root)  # 1st level
            return customer_list

        find_customers_at_level(self.root)

        return customer_list

    def linear_sort_by_job(self, job_contains: str) -> list:
        """
        Retourne une liste triée contenant les clients dont leur job contient un certain string au début de la liste.
        Par exemple, tous les "IT" au début de la liste et ensuite les autres.
        :param job_contains: le contenu à chercher dans le job des clients
        :return: liste de clients
        """
        found: list = []
        others: list = []

        def recursive_lookup(customer: Customer) -> None:
            """
            Recursive function
            Separate matching - case sensitive - string found in job title from other
            :param customer:
            :return:
            """

            # checks if string is present and separate results in two lists
            if job_contains in customer.job_title:
                found.append(customer)
            else:
                others.append(customer)

            # recursive call
            for invitation in customer.invitations:
                recursive_lookup(invitation)

        # launch recursion
        recursive_lookup(self.root)

        # join the two lists
        return found + others

    def linear_sort_by_class_age(self, classes: list) -> list:
        """
        Retourne une matrice contenant n-classes. Chaque ligne de cette liste contient les clients se trouvant
        dans une classe d'âge donnée
        :param classes: liste de classes d'âge - [10, 15, 20, 25]
                                                Ceci veut dire que vous avez 3 classes d'âge (ou 3 listes) :
                                                [10, 15[, [15, 20[, [20, 25[

        :return: matrice contenant les clients se trouvant dans une classe d'âge
        """

        def recursive_lookup(customer: Customer) -> None:
            """
            Recursive function that fills the matrix
            :param customer:
            :return: None
            """

            # runs over the classes -> considering that the upper limit belongs to following range i.e 10-14, 15-20...
            for i in range(0, len(classes) - 1):

                if classes[i] <= customer.get_age() < classes[i + 1]:
                    # adds the customer to the right matrix
                    matrix[i].append(customer)
                    break  # breaks the loop once the condition is met

            # recursive call
            for invitation in customer.invitations:
                recursive_lookup(invitation)

        # prepare the matrix
        matrix: list = []

        # adds n list to the matrix [[],[]..]
        for i in range(0, len(classes)):
            matrix.append([])

        # launch recursion
        recursive_lookup(self.root)

        return matrix

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
        string: str = ''
        self.size = 0

        def print_levels(customer: Customer, string: str) -> str:
            """
            Recursive function that runs over the invitations and builds string
            :param customer:
            :param string:
            :return:
            """
            self.size += 1  # increase level count

            # invitations of customer
            for invited in customer.invitations:
                string += ('|' * int(self.size) + '__' + invited.__str__() + '\n')

                # invitations of customer invited
                if invited.invitations:
                    string = print_levels(invited, string)

            self.size -= 1  # decrease level count
            return string

        # starting with root
        string += (self.root.__str__() + '\n')

        # launch recursion
        if self.root.invitations:
            string = print_levels(self.root, string)

        # return print_levels(self.root, string)
        return string
