from klasse_quarkus import Quarkus_log_liste

def druck_eine_liste_aus(liste):
    for element in liste:
        print(element)
        print()

def finde_responseid(zeile):
    rueckgabe_string = ""
    if "RESPONSEID" in zeile:
        index = zeile.index("RESPONSEID")
        index_klammer = zeile[index:].index("]")
        rueckgabe_string = zeile[index + len("RESPONSEID") + 1 : index + index_klammer]
    return rueckgabe_string

def erstelle_liste_aller_responseid(log):
    rueckgabe_liste = []
    for line in log:
        responseid = finde_responseid(line)
        if responseid != "":
          
          rueckgabe_liste.append(responseid)
    rueckgabe_liste = list(set(rueckgabe_liste))
    rueckgabe_liste.sort()
    return rueckgabe_liste

def find_alle_zeilen_einer_responseid(responseid, liste):
    index = 0
    rueckgabe_liste = []
    for zeile in qlog_importe_liste:
        if responseid in zeile:
            rueckgabe_liste.append(zeile)
            break
        index += 1
    index += 1
    for line in qlog_importe_liste[index:]:
        if "RESPONSEID" not in qlog_importe_liste[index] or responseid in qlog_importe_liste[index]:
            rueckgabe_liste.append(line)
        if finde_responseid(line) != responseid and finde_responseid(line) != "":
            break
        index += 1
    return rueckgabe_liste
 
def alle_zusammenhaengenden_zeilen_zusammen(liste_alle_responseids):
    rueckgabe_liste = []
    for responseid in liste_alle_responseids:
        zeilen_passend_zur_id = find_alle_zeilen_einer_responseid(responseid, liste_alle_responseids)
        rueckgabe_liste.append(zeilen_passend_zur_id)
    return rueckgabe_liste

def drucke_doppelte_liste(liste):
    for element_aussen_liste in liste:
        responseid = finde_responseid_in_liste(element_aussen_liste)
        gvf = finde_gvf_in_liste(element_aussen_liste)
        print("---Import:-", "ResponseID:", responseid, "Geschaeftsvorfall:" , gvf, "--------------------------------------------")
        for element_innen in element_aussen_liste:
            print(element_innen)
        print()     

def finde_responseid_in_liste(liste):
    rueckgabe_string = ""
    for zeile in liste:
        if rueckgabe_string == "":
            rueckgabe_string = finde_responseid(zeile)       
    return rueckgabe_string

def finde_gvf_in_liste(liste):
    for zeile in liste:
        if "Bewilligung wurde erfolgreich als Auftrag angelegt" in zeile:
            return "Bewilligung wurde erfolgreich als Auftrag angelegt"
        elif "ABSAGE_DURCH_KOSTENTRAEGER" in zeile:
            return "Absage durch Kostentraeger"
        elif "ANTWORT_AUF_ANTRAG_AUF_VERLAENGERUNG_AUFENTHALT" in zeile:
            return "Antwort auf Antrag auf Verlaengerung des Aufenthalts"
        elif "ERGAENZUNG_VOR_BEGINN" in zeile:
            return "Ergaenzungen vor Rehe-Beginn"
        elif "ANTWORT_ZUM_ANTRAG_DER_VERLAENGERUNG_DER_KOSTENZUSAGE" in zeile:
            return "Antwort auf Antrag der Verlaengerung der Kostenzusage"
        elif "ANTWORT_AUF_ANTRAG_AUF_VERLAENGERUNG_AUFENTHALT" in zeile:
            return "Antwort auf Antrag auf Verlaengerung des Aufenthalts"
        else:
            return "Kein GVF gefunden :("
            
def liefere_fehlerliste(liste):
    rueckgabe_liste = []
    for element_aussen_liste in liste:
        bool_error_in_liste = False
        for element_innen in element_aussen_liste:
            if "ERROR" in element_innen and bool_error_in_liste == False:
                rueckgabe_liste.append(element_aussen_liste)
                bool_error_in_liste = True
    return rueckgabe_liste

if __name__ == '__main__':
    qlog_liste = Quarkus_log_liste().get_quarkus_log_liste()
    qlog_importe_liste = Quarkus_log_liste().get_quarkus_importe()
    liste_responseid = erstelle_liste_aller_responseid(qlog_importe_liste)
    liste_aus_listen_alles_zusammenpassenden_zeilen = alle_zusammenhaengenden_zeilen_zusammen(liste_responseid)
    liste_aus_listen_alles_zusammenpassenden_zeilen.sort()
    error_liste = liefere_fehlerliste(liste_aus_listen_alles_zusammenpassenden_zeilen)
    drucke_doppelte_liste(liste_aus_listen_alles_zusammenpassenden_zeilen)
    
