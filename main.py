from cpf_cnpj import CpfCnpj
from validate_docbr import CNPJ

#cpf_um = Cpf("15316264754")
#print(cpf_um)

exemplo_cnpj = "35379838000112"
exemplo_cpf = "32007832062"
# cnpj = CNPJ()
# print(cnpj.validate(exemplo_cnpj))

documento = CpfCnpj(exemplo_cnpj, 'cnpj')
documento2 = CpfCnpj(exemplo_cpf, "cpf")
print(documento)
print(documento2)

