from domaine.customer import Customer
from datetime import datetime


class FileParser:

    def parse_costumers(self, file_content: str) -> list:
        """
        Converti le contenu d'un fichier en une liste de clients
        :param file_content: contenu d'un fichier
        :return: liste de clients
        """

        file_lines = file_content.splitlines()
        cust_list = [0]  # represents the highest customer id which is also the size (-1) of the list

        for line in file_lines[1:]:  # skips the header line
            element = line.split(',')  # sample : 18,Chad,Russel,Chad_Russel8852@joiniaa.com,5/26/1983,Banker

            curr_index = int(element[0])  # represents the Customer id

            if curr_index > cust_list[0]:  # when the element is new e.g. 18 > 8

                # cust_list[0] = 8 and curr_index = 18 : 18-8 = 10 to add, works even with missing ids
                for i in range(0, curr_index - int(cust_list[0])):
                    cust_list.append([])  # increases the size of the list

                cust_list[0] = curr_index

            # adds the Customer in the list at the index corresponding to his id
            cust_list[curr_index] = Customer(int(element[0]), element[1], element[2], element[3],
                                             datetime.strptime(element[4], '%m/%d/%Y').date, element[5])

        # test : should display 7 Bree and age
        # print('id: ', cust_list[7].id, 'name: ', cust_list[7].first_name, 'age :', cust_list[7].get_age())

        return cust_list

    def parse_relations(self, file_content: str) -> list:
        """
        Converti le contenu d'un fichier en une liste de relations
        :param file_content: contenu d'un fichier
        :return: liste de relations
        """
        file_lines = file_content.splitlines()

        rel_list = [0]  # represents the highest customer id which is also the size (-1) of the list

        for line in file_lines[1:]:  # skips the header line
            element = line.split(',')  # sample : 1,2 1,3 1,4 1,7

            curr_index = int(element[0])  # represents the Customer id (who is inviting)

            # print("index:", rel_list[0], "curr_index:", curr_index, "element:", element[1])  # DEBUG
            if curr_index > rel_list[0]:  # when the element is new e.g. 18 > 8

                # rel_list[0] = 8 and curr_index = 18 : 18-8 = 10 to add, works even with missing ids (652)
                for i in range(0, curr_index - int(rel_list[0])):
                    rel_list.append([])  # increases the size of the list

                rel_list[0] = curr_index

            # adds the invited Customers ids to a list at the index corresponding to the inviting Customer id
            rel_list[curr_index].append(int(element[1]))

        # for relations in rel_list:   # DEBUG
        #     print(relations)

        return rel_list
