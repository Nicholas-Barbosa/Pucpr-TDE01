import random


def populaNumerosRandomicos():
     randomicos =  random.sample(range(0, 157), 10)
     randomicos.sort(reverse= True);
     return randomicos;


tentativas: int = 1;
arrayComNumerosRandomicos = populaNumerosRandomicos();

while 10 < 100:
    somaInput: int = int(input("Soma, %s + %s: " % (arrayComNumerosRandomicos[0], arrayComNumerosRandomicos[9])));
    subtracaoInput: int = int(
        input("Subtracao, %s - %s: " % (arrayComNumerosRandomicos[1], arrayComNumerosRandomicos[8])));
    multInput: int = int(
        input("Multiplicação, %s * %s: " % (arrayComNumerosRandomicos[3], arrayComNumerosRandomicos[6])));
    divisaoInput: float(input("Divisão, %s / %s: " % (arrayComNumerosRandomicos[5], arrayComNumerosRandomicos[2])));
    if somaInput == (arrayComNumerosRandomicos[0] + arrayComNumerosRandomicos[
        9]) and subtracaoInput == (arrayComNumerosRandomicos[1] - arrayComNumerosRandomicos[
        8]) and multInput == (arrayComNumerosRandomicos[3] * arrayComNumerosRandomicos[
        6]):
        print("Tentativas: %s " % tentativas);
        break;
    else:
        print("Errou! Jogo reiniciado!");
        tentativas = tentativas + 1;
        arrayComNumerosRandomicos = populaNumerosRandomicos();

#Nicholas Barbosa, Gustavo Fiori Luís Choinski