class FileWriter:

    def write_to_file(self, string: str, filename: str) -> None:
        """
        Permet d'écrire un string dans un fichier
        :param string: Le string à enregistrer
        :param filename: Le chemin et nom de fichier où le strind oit être stocké
        """
        f = open(filename, "w+")
        f.write(string)
        f.close()
