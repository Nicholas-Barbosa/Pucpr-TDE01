tentativas: int = 1;
while 10 < 100:
    somaInput: int = int(input("1000 + 800: "));
    subtracaoInput: int = int(input("2998 - 242: "));
    multInput: int = int(input("35 * 45: "));
    divisaoInput: float = float(input("550/6: "));
    if somaInput == 1800 and subtracaoInput == 2756 and multInput == 1575 and divisaoInput == 91.6:
        print("Tentativas: %s " %tentativas);
        break;
    else:
        print("Errou! Jogo reiniciado!");
        tentativas  = tentativas+1;

#Nicholas Barbosa, Gustavo Fiori Luís Choinski