import csv
from operator import itemgetter
class automobile:
    def __init__(self, id, marca, modello, anno, num_posti):
        self.id = id
        self.marca = marca
        self.modello = modello
        self.anno = int(anno)
        self.num_posti = int(num_posti)
        self.noleggiata = False

    def __str__(self):
        return f"{self.id}, {self.marca}, {self.modello}, {self.anno}, {self.num_posti}"

class Autonoleggio:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.lista_auto = []


    def carica_file_automobili(self, file_path):
        """Carica le auto dal file"""
        try:
            input_file = open(file_path,'r')
            reader = csv.reader(input_file)
            for line in reader:
                id, marca, modello, anno, num_posti = line
                auto = automobile(id, marca, modello, anno, num_posti)
                self.lista_auto.append(auto)
        except FileNotFoundError:
            raise FileNotFoundError('File not found')


    def aggiungi_automobile(self, marca, modello, anno, num_posti):
        """Aggiunge un'automobile nell'autonoleggio: aggiunge solo nel sistema e non aggiorna il file"""
        ultimo_id = self.lista_auto[-1].id
        num_progressivo = int(ultimo_id[1:])+1
        id = f'A{num_progressivo}'
        automobile(id, marca, modello, anno, num_posti)
        auto = automobile(id, marca, modello, anno, num_posti)
        self.lista_auto.append(auto)

        return auto

    def automobili_ordinate_per_marca(self):
        """Ordina le automobili per marca in ordine alfabetico"""

        return sorted(self.lista_auto, key=lambda a: a.marca.lower())



    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        pass

    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        pass
