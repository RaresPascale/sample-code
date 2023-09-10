
def taxCalculator(pret, tva):
    pretNet = pret - pret * tva / 100
    print(pretNet)

if __name__ == '__main__':
    taxCalculator(200,19)


