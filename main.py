from outils.file_loader import FileLoader as Loader
from outils.file_parser import FileParser as Parser
from outils.file_writer import FileWriter as Writer
from metier.customers import CustomerTree as Tree
from domaine.customer import Customer
import datetime

if __name__ == "__main__":

    loader = Loader()
    customers_file = loader.load('data\\costumers_data.csv')
    relations_file = loader.load('data\\costumers_relations.csv')

    parser = Parser()
    tree = Tree()
    tree.build_tree(parser.parse_costumers(customers_file), parser.parse_relations(relations_file))

    # test get_average_age
    # print('Moyenne d\'âge : ', tree.get_average_age())

    # test get_average_invitations
    # print('Nb moyen d\'invitations par client : ', tree.get_average_invitations())

    # test linear_sort_by_class_age
    # classes: list = [10, 15, 20, 25]
    # matrix: list = tree.linear_sort_by_class_age(classes)
    # for i in range(0, len(classes) - 1):
    #     print('Classe de', classes[i], 'à', classes[i + 1] - 1, 'ans')
    #
    #     for customer in matrix[i]:
    #         print(customer.__str__(), ':', customer.get_age(), 'ans')

    # test linear_sort_by_job
    # results: list = tree.linear_sort_by_job('IT')
    # for i in range(1, 2000):
    #     print(results[i], '(' + results[i].job_title + ')')

    # test get_row (invitation level)
    # results: list = tree.get_row(3)
    # for result in results:
    #     print(result)

    # # testing get (comparing IDs)
    # for i in range (99998, 100002):
    #     lookup_customer: Customer = Customer(id=i)
    #     customer_found = tree.get(lookup_customer)
    #     print('client trouvé', customer_found)

    # # testing add
    # lookup_customer: Customer = Customer(id=92320)
    # customer_from_list = tree.get(lookup_customer)
    # new_customer: Customer = Customer(id=100001, first_name='Frank', last_name='Théodoloz',
    #                                   email='frank.theodoloz@etu.hesge.ch', date_birth=datetime.datetime(1980, 12, 3),
    #                                   job_title='Développeur')
    #
    # tree.add(new_customer, customer_from_list)

    # # testing remove
    # ids: list = [3, 4, 7, 18, 75, 385, 4474, 21988, 88794]
    # for id in ids:
    #     lookup_customer: Customer = Customer(id=id)
    #     tree.remove(lookup_customer)

    # test output
    writer = Writer()
    writer.write_to_file(tree.__str__(), 'output.txt')
