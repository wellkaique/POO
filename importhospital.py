from atividadehospital import Hospital, Medico, Enfermeira, Ala,planosaude

#Criando Hospital

Hospital = Hospital(cnpj="123456789101112")

#Criando Alas
ala1 = Ala(identificador=1)
ala2 = Ala(identificador=2)
ala3 = Ala(identificador=3)

Hospital.adicionar_ala(ala1)
Hospital.adicionar_ala(ala2)
Hospital.adicionar_ala(ala3)

#Criando enfermeiras

enfermeira1 = Enfermeira(nome_enfermeira = "Ana", CRE="CRE123")
enfermeira2 = Enfermeira(nome_enfermeira = "Vitoria", CRE= "CRE 456")
enfermeira3 = Enfermeira(nome_enfermeira = "Giovana", CRE= "CRE 789")

#Associando enfermeiras às alas
enfermeira1.set_ala(ala1)
enfermeira2.set_ala(ala2)
enfermeira3.set_ala(ala3)


#Criando planos de saude

plano_a = PlanoSaude(nome="Plano A", telefone= "111111")
plano_b = PlanoSaude(nome="Plano B", telefone= "2222-2222"
plano_c = PlanoSaude(nome="Plano C", telefone= "3333-3333")

Hospital.adicionar_planosaude(plano_a)
Hospital.adicionar_planosaude(plano_b)
Hospital.adicionar_plano_saude