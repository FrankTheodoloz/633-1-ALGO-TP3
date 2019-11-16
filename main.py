from outils.file_loader import FileLoader as Loader
from outils.file_parser import FileParser as Parser
from outils.file_writer import FileWriter as Writer
from metier.customers import CustomerTree as Tree

if __name__ == "__main__":
    loader = Loader()
    customers_file = loader.load('data\\costumers_data.csv')
    relations_file = loader.load('data\\costumers_relations.csv')

    parser = Parser()
    tree = Tree()
    tree.build_tree(parser.parse_costumers(customers_file), parser.parse_relations(relations_file))

    # writer = Writer()
    # writer.write_to_file(tree.__str__(), 'output.txt')
    # print('Moyenne d\'âge : ', tree.get_average_age(), 'somme:', tree.sum_of_ages, 'nombre:', tree.nb_of_customers)
    # print('Nb moyen d\'invitations par client : ', tree.get_average_invitations())

    # test linear_sort_by_class_age
    classes: list = [10, 15, 20, 25]
    matrix: list = tree.linear_sort_by_class_age(classes)
    for i in range(0, len(classes) - 1):
        print('classe de', classes[i], 'à', classes[i + 1])

        for customer in matrix[i]:
            print(customer.__str__(), ':', customer.get_age())  # __str__  does not work as expected

