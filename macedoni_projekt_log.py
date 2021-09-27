# importing libraries
import time
import mouse
import random
import sys
import keyboard
import re
import os

INPUT_YES = 'y'
INPUT_NO = 'n'

def cls():
    os.system('cls')

if __name__=="__main__":

    random.seed(42) # nastavi generator randomiziranih stevil.
    se_opisujem_korake = True

    # nov = 'y'
    stevilo_korakov = 0
    pravokotniki = []
    tipi_klika = []
    zamiki_koraka = []
    dodatki_zamikom = []
    tudi_teksti = []
    teksti = []

    stevilo_korakov_SPECIAL = 0
    pravokotniki_SPECIAL = []
    tipi_klika_SPECIAL = []
    zamiki_koraka_SPECIAL = []
    dodatki_zamikom_SPECIAL = []
    tudi_teksti_SPECIAL = []
    teksti_SPECIAL = []

    special_MIN = 0
    special_MAX = 0

    with open("sekvence_korakov.txt", 'r') as seznamSekvenc:
        seznam_sekvenc = seznamSekvenc.readlines()
    # print(seznam_sekvenc) preglej seznam sekvenc.

    nov = None
    continueLoop = True

    if seznam_sekvenc == []:
        print("\nTrenutno nimate nobenih shranjenih programov. Najprej morate enega ustvariti.")
        nov = 'y'
        continueLoop = False

    while continueLoop:
        nov = input("\nŽelite napisati nove korake (y/n)? ")

        cls()

        if nov not in [INPUT_YES, INPUT_NO]:
            print('Vnos ni prepoznan!')
        else:
            continueLoop = False

    if nov == "y":
        input("\nPripravite si okno za opisovanje prvega koraka. klikni ENTER sem, ko je pripravljeno:")


        while ( se_opisujem_korake ):

            ####### PRAVOKOTNIK:

            # x, y = mouse.get_position() # Pridobi pozicijo miske na zacetku.
            print("\nProsim, z levim gumbom na miški POČASI potegni čez območje klika:")
            mouse.record(button='left', target_types=('down'))
            x_down, y_down = mouse.get_position()

            mouse.record(button='left', target_types=('up'))
            x_up, y_up = mouse.get_position()


            rect_low_x = min(x_down, x_up)
            rect_high_x = max(x_down, x_up)
            rect_low_y = min(y_down, y_up)
            rect_high_y = max(y_down, y_up)
            pravokotniki.append((rect_low_x, rect_high_x, rect_low_y, rect_high_y))

            print("\nOdčitan Pravokotnik:")
            print("["+str(rect_low_x).rjust(5, ' ')+","+str(rect_low_y).rjust(5, ' ')+"] -------------- ["+
                  str(rect_high_x).rjust(5, ' ')+","+str(rect_low_y).rjust(5, ' ')+"]")
            print("      |                            | ")
            print("["+str(rect_low_x).rjust(5, ' ')+","+str(rect_high_y).rjust(5, ' ')+"] -------------- ["+
                  str(rect_high_x).rjust(5, ' ')+","+str(rect_high_y).rjust(5, ' ')+"]")

            print("\nProsim, izberi številko za vrsto klika. Možnosti so:")
            print(" 1  Levi")
            print(" 2  Desni")
            print(" 3  Srednji")
            print(" 4  Dvojni levi")
            print(" 5  Dvojni desni")
            click_type_choice = int(input("Moja izbira vrste klika ( stevilka 1 do 5 ): "))
            if click_type_choice not in [1, 2, 3, 4, 5]:
                click_type_choice = 1
                print("Ta izbira ni dovoljena. Izbira je spremenjena na 1 (Levi).")
            tipi_klika.append(click_type_choice)

            step_time = float(input("\nMinimalni čas do naslednjega koraka v ciklu v sekundah (lahko je decimalka): "))
            if (step_time < 0):
                print("Negativna vrednost za čas ni dovoljena! Nadomeščeno z 0 sekund.")
                step_time = 0
            zamiki_koraka.append(step_time)
            add_time = float(input("\nMaksimalni čas, ki se PRIŠTEJE minimalnemu  v sekundah (lahko je decimalka): "))
            if (add_time < 0):
                print("Negativna vrednost za čas ni dovoljena! Nadomeščeno z 0 sekund.")
                add_time = 0
            dodatki_zamikom.append(add_time)

            tudi_tekst = input("\nZelite po kliku dodat tudi kakšen tekst (y/n)? ")
            if tudi_tekst != 'y':
                tudi_tekst = 'n'
            tudi_teksti.append(tudi_tekst)
            rand_teksts = []
            if (tudi_tekst == "y"):
                print()
                while True:
                    tekst = input("Vnesite nov željen tekst, ki naj se izpiše po kliku (za izhod pustite prazno): ")
                    if (tekst!=""):
                        rand_teksts.append(tekst.replace(' ', '{').lower())
                    else:
                        break
                if rand_teksts == []:
                    tudi_teksti[-1] = 'n'  # there is no text!
            teksti.append(rand_teksts)

            stevilo_korakov += 1
            is_over = input("\nPRIPRAVITE SI OKNO za opisovanje naslednjega koraka. So to vsi koraki v ciklu? (y/n) : ")
            if (is_over=="y"):
                break
            print("\n------ NOV  KORAK  ----------")

        stevilo_ciklov = int(input("\nKoliko ciklov želiš: "))
        if (stevilo_ciklov < 1):
            print("Nedovoljeno število ciklov manjše od 1. Število je bilo popravljeno na 1!")
            stevilo_ciklov = 1

        #############################################################################################################
        # POSEBNI CIKLI:
        #############################################################################################################

        zelim_posebne_cikle = input("\nAli želiš posebno zaporedje korakov? (y/n) ")
        if zelim_posebne_cikle != 'y':
            zelim_posebne_cikle = 'n'

        if zelim_posebne_cikle == "y":

            input("\nSprejeto. Pripravite si pogled za POSEBNO zaporedje in kliknite ENTER semle: ")
            while True:

                # PRAVOKOTNIK:

                # x, y = mouse.get_position() # Pridobi pozicijo miske na zacetku.
                print("\nProsim, z levim gumbom na miški POČASI potegni čez območje klika:")
                mouse.record(button='left', target_types=('down'))
                x_down, y_down = mouse.get_position()

                mouse.record(button='left', target_types=('up'))
                x_up, y_up = mouse.get_position()

                rect_low_x = min(x_down, x_up)
                rect_high_x = max(x_down, x_up)
                rect_low_y = min(y_down, y_up)
                rect_high_y = max(y_down, y_up)
                pravokotniki_SPECIAL.append((rect_low_x, rect_high_x, rect_low_y, rect_high_y))

                print("\nOdčitan Pravokotnik:")
                print("[" + str(rect_low_x).rjust(5, ' ') + "," + str(rect_low_y).rjust(5, ' ') + "] -------------- [" +
                      str(rect_high_x).rjust(5, ' ') + "," + str(rect_low_y).rjust(5, ' ') + "]")
                print("      |                            | ")
                print("[" + str(rect_low_x).rjust(5, ' ') + "," + str(rect_high_y).rjust(5, ' ') + "] -------------- [" +
                      str(rect_high_x).rjust(5, ' ') + "," + str(rect_high_y).rjust(5, ' ') + "]")

                print("\nProsim, izberi številko za vrsto klika. Možnosti so:")
                print(" 1  Levi")
                print(" 2  Desni")
                print(" 3  Srednji")
                print(" 4  Dvojni levi")
                print(" 5  Dvojni desni")
                click_type_choice = int(input("Moja izbira vrste klika ( stevilka 1 do 5 ): "))
                if click_type_choice not in [1, 2, 3, 4, 5]:
                    click_type_choice = 1
                    print("Ta izbira ni dovoljena. Izbira je spremenjena na 1 (Levi).")
                tipi_klika_SPECIAL.append(click_type_choice)

                step_time = float(input("\nMinimalni čas do naslednjega koraka v ciklu v sekundah (lahko je decimalka): "))
                if (step_time < 0):
                    print("Negativna vrednost za čas ni dovoljena! Nadomeščeno z 0 sekund.")
                    step_time = 0
                zamiki_koraka_SPECIAL.append(step_time)
                add_time = float(input("\nMaksimalni čas, ki se PRIŠTEJE minimalnemu  v sekundah (lahko je decimalka): "))
                if (add_time < 0):
                    print("Negativna vrednost za čas ni dovoljena! Nadomeščeno z 0 sekund.")
                    add_time = 0
                dodatki_zamikom_SPECIAL.append(add_time)

                tudi_tekst = input("\nZelite po kliku dodat tudi kakšen tekst (y/n)? ")
                if tudi_tekst != 'y':
                    tudi_tekst = 'n'
                tudi_teksti_SPECIAL.append(tudi_tekst)

                rand_teksts = []
                if (tudi_tekst == "y"):
                    rand_teksts = []
                    print()
                    while True:
                        tekst = input("Vnesite nov željen tekst, ki naj se izpiše po kliku (za izhod pustite prazno): ")
                        if (tekst != ""):
                            rand_teksts.append(tekst.replace(' ', '{').lower())
                        else:
                            break
                    if rand_teksts == []:
                        tudi_teksti_SPECIAL[-1] = 'n'  # there is no text!
                teksti_SPECIAL.append(rand_teksts)

                stevilo_korakov_SPECIAL += 1
                is_over = input("\nPRIPRAVITE SI OKNO za opisovanje naslednjega koraka. So to vsi koraki v POSEBNEM ciklu? (y/n) : ")
                if (is_over == "y"):
                    special_MIN = int(input("\nŽeleno MINIMALNO  število zaporednih normalnih ciklov do posebnega? "))
                    special_MAX = int(input(  "Želeno MAKSIMALNO število zaporednih normalnih ciklov do posebnega? "))
                    if ((not(special_MIN <= special_MAX)) or special_MIN < 2):
                        print("\nPosodobljeno: Minimum: 50,  maximum: 100.")
                        special_MIN = 50
                        special_MAX = 100

                    break
                print("\n------ NOV  KORAK  ----------")

        shrani = input("\nOpisovanje sekvence korakov je končano. Želite shraniti to sekvenco (y/n)? ")
        if shrani == "y":
            ime = input("\nPodajte ime sekvence (dovoljena imena so iz črk in številk): ")
            # Treba preverit, da je sekvenca dovoljena.
            while (not(re.match("^[A-Za-z0-9ŠšČčĆćŽžĐđ]*$", ime))):
                ime = input("Nedovoljeno ime! Dovoljena imena so iz črk in številk. Poskusite ponovno: ")

            sekvenca_ze_obstaja = (False, len(seznam_sekvenc))
            for i, sekvenca in enumerate(seznam_sekvenc):
                if ((ime+' ') == sekvenca[:(len(ime)+1)]):
                    sekvenca_ze_obstaja = (True, i)
                    break

            # format:
            # imeSekvence nov stevilo_korakov stevilo_ciklov
            # zaVsakKorak:                    prav1 prav2 prav3 prav4 prav1 prav2 ...   (4*st_korakov)
            #                                 tip_klika1 tip_klika2 tip_klika3 ...
            #                                 zamik_koraka1 zamik_koraka2 ...
            #                                 dodatki_zamikom1 dodatki_zamikom2 ...
            #                                 tudi_teksti1 tudi_teksti2 ...
            #                                 teksti1 teksti2 ...
            # pri cemer je vsak teksti formata:      °tekst1`tekst2`tekst3°

            # stevilo_korakov_SPECIAL
            # zaVsakPosebenKorak:             prav1 prav2 prav3 prav4 prav1 prav2 ...   (4*st_korakov)
            #                                 tip_klika1 tip_klika2 tip_klika3 ...
            #                                 zamik_koraka1 zamik_koraka2 ...
            #                                 dodatki_zamikom1 dodatki_zamikom2 ...
            #                                 tudi_teksti1 tudi_teksti2 ...
            #                                 teksti1 teksti2 ...
            # pri cemer je vsak teksti formata:      °tekst1`tekst2`tekst3°
            #
            #  special_MIN = 0
            #  special_MAX = 0
            nova_sekvenca = ime+' '+zelim_posebne_cikle+' '+str(stevilo_korakov)+' '+str(stevilo_ciklov)
            for k in range(stevilo_korakov):
                nova_sekvenca += (' '+str(pravokotniki[k][0])+' '+str(pravokotniki[k][1])+' ' +
                                  str(pravokotniki[k][2])+' '+str(pravokotniki[k][3]))
                nova_sekvenca += (' '+str(tipi_klika[k])+' '+str(zamiki_koraka[k])+' '+str(dodatki_zamikom[k]))
                nova_sekvenca += (' '+tudi_teksti[k])

                rand_teksts = teksti[k]
                if rand_teksts == []:
                    encoded_texts = '°°'
                else:
                    encoded_texts = '°'
                    for tekst in rand_teksts:
                        encoded_texts += (tekst+'`')
                    encoded_texts = encoded_texts[:-1] + '°'
                nova_sekvenca += (' '+encoded_texts)

            if zelim_posebne_cikle == 'y':
                nova_sekvenca += (' '+str(stevilo_korakov_SPECIAL))
                for k in range(stevilo_korakov_SPECIAL):
                    nova_sekvenca += (' '+str(pravokotniki_SPECIAL[k][0])+' '+str(pravokotniki_SPECIAL[k][1])+' ' +
                                      str(pravokotniki_SPECIAL[k][2])+' '+str(pravokotniki_SPECIAL[k][3]))
                    nova_sekvenca += (' '+str(tipi_klika_SPECIAL[k])+' '+str(zamiki_koraka_SPECIAL[k])+' '+str(dodatki_zamikom_SPECIAL[k]))
                    nova_sekvenca += (' '+tudi_teksti_SPECIAL[k])

                    rand_teksts_SPECIAL = teksti_SPECIAL[k]
                    if rand_teksts_SPECIAL == []:
                        encoded_texts_SPECIAL = '°°'
                    else:
                        encoded_texts_SPECIAL = '°'
                        for tekst_SPECIAL in rand_teksts_SPECIAL:
                            encoded_texts_SPECIAL += (tekst_SPECIAL+'`')
                        encoded_texts_SPECIAL = encoded_texts_SPECIAL[:-1] + '°'
                    nova_sekvenca += (' '+encoded_texts_SPECIAL)
                nova_sekvenca += (' '+str(special_MIN)+' '+str(special_MAX))
            # print(nova_sekvenca)

            if sekvenca_ze_obstaja[0]:
                seznam_sekvenc[sekvenca_ze_obstaja[1]] = nova_sekvenca
            else:
                seznam_sekvenc.append(nova_sekvenca)
            # shrani nove sekvence v sekvence_korakov.txt:
            vse_sekvence = ''
            for sekvenca_i in seznam_sekvenc:
                vse_sekvence += (sekvenca_i.replace('\n', '') + '\n')
            with open("sekvence_korakov.txt", 'w') as seznamSekvenc:
                seznamSekvenc.write(vse_sekvence[:-1])

    else:  # pognali bomo obstojec program!
        print("Programi na voljo:")
        for s, sekvenca_i in enumerate(seznam_sekvenc):
            print(str(s+1) + ': ' + str(sekvenca_i.split(sep=' ')[0]))
        program_izbira = int(input('Vnesite ŠTEVILKO želenega programa semle: '))-1
        if program_izbira not in list(range(len(seznam_sekvenc))):
            program_izbira = 0
            print("Ta izbira ni dovoljena. Izbira je spremenjena na 1: "+str(seznam_sekvenc[0].split(sep=' ')[0]))
        sek = seznam_sekvenc[program_izbira].replace('\n', '').split(sep=' ')
        # print(sek)
        zelim_posebne_cikle = sek[1]
        stevilo_korakov, stevilo_ciklov = int(sek[2]), int(sek[3])
        ind = 4
        for k in range(stevilo_korakov):
            pravokotniki.append((int(sek[ind]), int(sek[ind+1]), int(sek[ind+2]), int(sek[ind+3])))
            tipi_klika.append(int(sek[ind+4]))
            zamiki_koraka.append(float(sek[ind+5]))
            dodatki_zamikom.append(float(sek[ind+6]))
            tudi_teksti.append(sek[ind+7])

            rand_teksts_orig = sek[ind+8]
            rand_teksts = rand_teksts_orig.replace('°', '').split(sep='`')
            teksti.append(rand_teksts)
            ind += 9

        if zelim_posebne_cikle == 'y':
            stevilo_korakov_SPECIAL = int(sek[ind])
            ind += 1
            for k in range(stevilo_korakov_SPECIAL):
                pravokotniki_SPECIAL.append((int(sek[ind]), int(sek[ind + 1]), int(sek[ind + 2]), int(sek[ind + 3])))
                tipi_klika_SPECIAL.append(int(sek[ind + 4]))
                zamiki_koraka_SPECIAL.append(float(sek[ind + 5]))
                dodatki_zamikom_SPECIAL.append(float(sek[ind + 6]))
                tudi_teksti_SPECIAL.append(sek[ind + 7])

                rand_teksts_orig_special = sek[ind + 8]
                rand_teksts_special = rand_teksts_orig_special.replace('°', '').split(sep='`')
                teksti_SPECIAL.append(rand_teksts_special)
                ind += 9
            special_MIN = int(sek[ind])
            special_MAX = int(sek[ind+1])



    input("\nSprejeto. Pripravite si pogled in kliknite ENTER semle: ")
    print("\nProgram teče. Če ga želite prekiniti, kliknite in DRŽITE 'c'. Za pavzo DRŽITE 'p'.")

    print("\nImaš 20 - 25 sekund da minimiziraš oziroma umakneš to okno.")
    val_time = 20 + random.random()*5
    time.sleep(val_time)





    # Vsi podatki zabelezeni. ZDAJ SLEDI DEJANSKO IZVAJANJE PROGRAMA.  #########################################
    stevilo_zaporednih_normalnih = -1
    poseben_cikel = int(special_MIN + random.random()*(special_MAX-special_MIN))

    for cikel in range(stevilo_ciklov):
        stevilo_zaporednih_normalnih += 1
        ######################################################################################################
        # POSEBEN CIKEL:
        ######################################################################################################

        if (zelim_posebne_cikle=="y" and stevilo_zaporednih_normalnih == poseben_cikel):
            print("POSEBEN CIKEL:", poseben_cikel)
            poseben_cikel = int(special_MIN + random.random()*(special_MAX-special_MIN))
            stevilo_zaporednih_normalnih = 0

            for korak in range(stevilo_korakov_SPECIAL):
                # nakljucna pozicija klika:
                rect_low_x, rect_high_x, rect_low_y, rect_high_y = pravokotniki_SPECIAL[korak]
                rand_x = int(rect_low_x + random.random() * (rect_high_x - rect_low_x))
                rand_y = int(rect_low_y + random.random() * (rect_high_y - rect_low_y))
                # premakni misko na to nakljucno mesto:
                trajanje = 0.3 + random.random() * 0.2
                mouse.move(x=rand_x, y=rand_y, absolute=True, duration=trajanje)

                # klikni s pravilnim tipom klika:
                tip_klika = tipi_klika_SPECIAL[korak]
                if tip_klika == 1:
                    mouse.click(button='left')
                elif tip_klika == 2:
                    mouse.click(button='right')
                elif tip_klika == 3:
                    mouse.click(button='middle')
                elif tip_klika == 4:
                    mouse.double_click(button='left')
                elif tip_klika == 5:
                    mouse.double_click(button='right')

                # vnesi tekst:
                if tudi_teksti_SPECIAL[korak] == "y":
                    rand_teksts = teksti_SPECIAL[korak]
                    rand_choice = int(random.random()*len(rand_teksts))
                    tekst = rand_teksts[rand_choice].replace('{', ' ').replace('°', '').replace('`', '')
                    for crka in tekst:
                        time.sleep(0.2 + random.random() * 0.2)
                        keyboard.send(crka)
                        time.sleep(0.1 + random.random() * 0.2)
                    keyboard.send("ENTER")
                    time.sleep(1)

                # pocakaj nakljucno kolicino casa.
                cas_cakanja = zamiki_koraka_SPECIAL[korak] + random.random() * dodatki_zamikom_SPECIAL[korak]
                time.sleep(cas_cakanja)

        ######################################################################################################
        # NORMALEN CIKEL:
        ######################################################################################################

        # OPCIJSKO: printaj stevilko trenutnega cikla:
        zamik = len(str(stevilo_ciklov))
        print("Cikel: " + str(cikel+1).rjust(zamik, ' ') + "/" + str(stevilo_ciklov).rjust(zamik, ' '))

        for korak in range(stevilo_korakov):
            # nakljucna pozicija klika:
            rect_low_x, rect_high_x, rect_low_y, rect_high_y = pravokotniki[korak]
            rand_x = int(rect_low_x + random.random()*(rect_high_x-rect_low_x))
            rand_y = int(rect_low_y + random.random()*(rect_high_y-rect_low_y))
            # premakni misko na to nakljucno mesto:
            trajanje = 0.3 + random.random()*0.2
            mouse.move(x=rand_x, y=rand_y, absolute=True, duration=trajanje)

            # klikni s pravilnim tipom klika:
            tip_klika = tipi_klika[korak]
            if tip_klika == 1:
                mouse.click(button='left')
            elif tip_klika == 2:
                mouse.click(button='right')
            elif tip_klika == 3:
                mouse.click(button='middle')
            elif tip_klika == 4:
                mouse.double_click(button='left')
            elif tip_klika == 5:
                mouse.double_click(button='right')

            # vnesi tekst:
            if (tudi_teksti[korak] == "y"):
                rand_teksts = teksti[korak]
                rand_choice = int(random.random() * len(rand_teksts))
                tekst = rand_teksts[rand_choice].replace('{', ' ').replace('°', '').replace('`', '')
                for crka in tekst:
                    time.sleep(0.2 + random.random() * 0.2)
                    keyboard.send(crka)
                    time.sleep(0.1 + random.random() * 0.2)
                keyboard.send("ENTER")
                time.sleep(1)

            # pocakaj nakljucno kolicino casa.
            cas_cakanja = zamiki_koraka[korak] + random.random()*dodatki_zamikom[korak]
            time.sleep(cas_cakanja)

        # prekini izvajanje programa, ce uporabnik ta hip drzi ustrezno tipko:
        if keyboard.is_pressed('c'):
            print("\nPritisnili ste 'c'. Zato se program prekinja.")
            sys.exit(0)
        if keyboard.is_pressed('p'):
            input("\nPritisnili ste 'p'. Zato je program zaspal. Zbudite ga s tipko 'ENTER'.")

    print("Končano.")
