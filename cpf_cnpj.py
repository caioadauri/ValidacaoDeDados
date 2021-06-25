from validate_docbr import CPF, CNPJ

class CpfCnpj:

    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if self.tipo_documento == "cpf":
            if self.cpf_ehValido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF Inválido!!")
        elif self.tipo_documento == "cnpj":
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ Inválido")
        else:
            raise ValueError("Documento Inválido")

    def cpf_ehValido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos inválida")

    def formart_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

    def formart_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.formart_cpf()
        elif self.tipo_documento == "cnpj":
            return self.formart_cnpj()

    def cnpj_e_valido(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos invalido")