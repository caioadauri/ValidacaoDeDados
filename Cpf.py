class Cpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_ehValido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF Inválido!!")

    def __str__(self):
        return self.formart_cpf()

    def cpf_ehValido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False

    def formart_cpf(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]
        return (
            "{}.{}.{}-{}".format(
                fatia_um,
                fatia_dois,
                fatia_tres,
                fatia_quatro
            )
        )