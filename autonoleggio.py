import csv
from operator import itemgetter
from sys import exception


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
        self.noleggi = []

    def __str__(self):
        return f"{self.nome}, {self.responsabile}"

    def imposta_responsabile(self,responsabile):
        self.responsabile = responsabile


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
        auto_in_forma_list = []
        for auto in self.lista_auto:
            info_auto = [auto.id,auto.marca,auto.modello,auto.anno,auto.num_posti]
            auto_in_forma_list.append(info_auto)
        auto_in_forma_list.sort(key=itemgetter(1))

        return auto_in_forma_list



    def nuovo_noleggio(self, data, id_automobile, cognome_cliente):
        """Crea un nuovo noleggio"""
        trovato = False
        while not trovato:
            for auto in self.lista_auto:

                if auto.id.lower() == id_automobile.strip().lower() and not auto.noleggiata:
                    trovato = True
                    auto.noleggiata = True

                    if len(self.noleggi) == 0:
                        codice_noleggio = 'N1'
                    else:
                        codice_noleggio = 'N'+ str(self.noleggi[-1][1:]+1)

                    noleggio = {'id_noleggio': codice_noleggio,'id_auto': id_automobile, 'data': data,'cognome': cognome_cliente}
                    self.noleggi.append(noleggio)
                    return noleggio

        if not trovato:
            raise exception()




    def termina_noleggio(self, id_noleggio):
        """Termina un noleggio in atto"""
        trovato = False
        while not trovato:
            for noleggio in self.noleggi:
                if noleggio[id_noleggio].lower() == id_noleggio.strip().lower():
                    trovato = True
                    self.noleggi.remove(noleggio)

                    for auto in self.lista_auto:
                        if auto.id.lower() == noleggio['id_auto'].lower():
                            auto.noleggiata = False

        if not trovato:
            raise  exception()




