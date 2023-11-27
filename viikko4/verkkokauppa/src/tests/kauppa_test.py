import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.varasto_mock = Mock()
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock() 
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
    
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock  

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        #kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_tehdaan_osto_ja_varmistetaan_maksutietojen_oikeellisuus(self):
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock  

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        #kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikein
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_method_tilisiirto_is_called_with_correct_arguments(self):
        self.viitegeneraattori_mock.uusi.return_value = 55
        #self.varasto_mock  

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "omena", 2)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        #kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("martti", "67891")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikein
        self.pankki_mock.tilisiirto.assert_called_with("martti", 55, "67891", "33333-44455", 2)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_method_tilisiirto_is_called_with_correct_arguments_ver2(self):
        self.viitegeneraattori_mock.uusi.return_value = 55

        # tehdään toteutus saldo-metodille, molempia tuotteita on varastossa 10 kpl
        def varasto_saldo(tuote_id):
            if tuote_id == 1 or tuote_id == 2:
                return 10

        # tehdään toteutus hae_tuote-metodille,tuote_id 1 on omena ja tuote_id 2 on banaani
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "omena", 2)
            elif tuote_id == 2:
                return Tuote(2, "banaani", 3)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("martti", "67891")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikein
        self.pankki_mock.tilisiirto.assert_called_with("martti", 55, "67891", "33333-44455", 5)

    def test_method_tilisiirto_is_called_with_correct_arguments_ver3(self):
        self.viitegeneraattori_mock.uusi.return_value = 55

        # tehdään toteutus saldo-metodille, molempia tuotteita on varastossa 10 kpl
        def varasto_saldo(tuote_id):
            if tuote_id == 1 or tuote_id == 2:
                return 10

        # tehdään toteutus hae_tuote-metodille,tuote_id 1 on omena ja tuote_id 2 on banaani
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "omena", 2)
            elif tuote_id == 2:
                return Tuote(2, "banaani", 3)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # tehdään ostokset, ostetaan kaksi omenaa
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("martti", "67891")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikein
        self.pankki_mock.tilisiirto.assert_called_with("martti", 55, "67891", "33333-44455", 4)

    def test_method_tilisiirto_is_called_with_correct_arguments_ver4(self):
        self.viitegeneraattori_mock.uusi.return_value = 55

        # tehdään toteutus saldo-metodille, omenia on varastossa 10 kpl ja banaaneja 0 kpl
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 0

        # tehdään toteutus hae_tuote-metodille,tuote_id 1 on omena ja tuote_id 2 on banaani
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "omena", 2)
            elif tuote_id == 2:
                return Tuote(2, "banaani", 3)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # tehdään ostokset, ostetaan omena ja banaani (jota ei varastossa)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("martti", "67891")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikein
        self.pankki_mock.tilisiirto.assert_called_with("martti", 55, "67891", "33333-44455", 2)

    def test_every_tilisiirto_has_own_viitenumero(self):
        # Create two buyings with different customers
        self.viitegeneraattori_mock.uusi.return_value = 55
        self.varasto_mock
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "omena", 2)
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("martti", "67891")
        
        self.pankki_mock.tilisiirto.assert_called_with("martti", 55, "67891", "33333-44455", 2)
        # second buying:
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "omena", 2)
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "67891")

        # Create two separate tilisiirto calls 
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "67891", "33333-44455", 2)
        # Check that the viitenumero is different in both calls (42 and 55)
        self.assertNotEqual(self.pankki_mock.tilisiirto.call_args_list[0][0][1], self.pankki_mock.tilisiirto.call_args_list[1][0][1])





        
     




            

''' 
Aloitetaan asiointi, koriin lisätään kaksi samaa tuotetta, jota on varastossa tarpeeksi ja suoritetaan ostos, varmista että kutsutaan pankin metodia tilisiirto oikealla asiakkaalla, tilinumerolla ja summalla

Aloitetaan asiointi, koriin lisätään tuote, jota on varastossa tarpeeksi ja tuote joka on loppu ja suoritetaan ostos, varmista että kutsutaan pankin metodia tilisiirto oikealla asiakkaalla, tilinumerolla ja summalla '''