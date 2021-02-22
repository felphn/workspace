#include <stdio.h>
#include <stdlib.h>
// A basic calculator build without using the math.h lib

void printLines() {
    printf("=============================\n");
}


float calcExp(float n, int reps) {
    int i;
    float expRes = n;
    if (reps == 0) {
        return 1;
    } else {
        for (i = 0; i < reps-1; i++) {
            expRes = expRes * n;
        }
        return expRes;
    }
}


float calcFact(float n) {
    if (n == 1) {
        return n;
    } else {
        return n * calcFact(n - 1);
    }
}


float calcSen(float n, int reps) {
    int i;
    float radn = (n*3.14) / 180;
    float senRes = 0;
    for (i = 0; i < reps-1; i++) {
        senRes = senRes + ((calcExp(-1, i) * calcExp(radn, 2*i + 1)) / calcFact(2*i + 1));
    }
    return senRes;
}


float calcCos(float n, int reps) {
    int i;
    float radn = (n*3.14) / 180;
    float cosRes = 1;
    for (i = 1; i < reps; i++) {
        cosRes = cosRes + ((calcExp(-1, i) * calcExp(radn, 2*i)) / calcFact(2*i));
    }
    return cosRes;
}


int main() {
    int usrOption;
    int reps = 1;
    int IDNum = 0;
    float n, firstNum, secondNum, A[reps];
    float sumRes = 0;
    int runtimeLoop = 1;

    printLines();
    printf("\tCalculadora Basica\n");
    while (runtimeLoop == 1) {
        printLines();
        printf("Escolha uma funcao a seguir:\n\n");
        printf("[1]- Calcular Soma\n[2]- Calcular Subtracao\n[3]- Calcular Multiplicacao\n");
        printf("[4]- Calcular Divisao\n[5]- Calcular Divisao de Resto\n[6]- Calcular Exponencial\n");
        printf("[7]- Calcular Fatorial\n[8]- Calcular Seno\n[9]- Calcular Cosseno\n[0]- Encerrar o programa\n");
        printLines();
        printf("> ");
        scanf("%d", &usrOption);

        switch (usrOption) {
            case 1:
            printLines();
            printf("Quantos valores deseja somar?\n> ");
            scanf("%d", &reps);
            if (reps <= 0 || reps == 1) {
                printf("Erro! Digite o numero de valores que deseja somar!\n");
            } else {
                printLines();
                printf("Entre com os numeros que deseja somar\n");
                while (IDNum < reps) {
                    printf("> ");
                    scanf("%f", &A[IDNum]);
                    IDNum++;
                }
                for (IDNum = 0; IDNum < reps; IDNum++) {
                    sumRes = sumRes + A[IDNum];
                    A[IDNum] = 0;
                }
                printf("Resultado: %.4f\n\n\n", sumRes);
                reps = 1;
                IDNum = 0;
                sumRes = 0;
            }
            break;
            
            case 2:
            printLines();
            printf("Quantos valores deseja subtrair?\n> ");
            scanf("%d", &reps);
            if (reps <= 0 || reps == 1) {
                printf("Erro! Digite o numero de valores que deseja subtrair!\n");
            } else {
                printLines();
                printf("Entre com os numeros que deseja subtrair\n");
                while (IDNum < reps) {
                    printf("> ");
                    scanf("%f", &A[IDNum]);
                    IDNum++;
                }
                for (IDNum = 0; IDNum < reps; IDNum++) {
                    sumRes = sumRes - A[IDNum];
                    A[IDNum] = 0;
                }
                printf("Resultado: %.4f\n\n\n", sumRes);
                reps = 1;
                IDNum = 0;
                sumRes = 0;
            }
            break;

            case 3:
            printLines();
            printf("Quantos valores deseja multiplicar?\n> ");
            scanf("%d", &reps);
            if (reps <= 0 || reps == 1) {
                printf("Erro! Digite o numero de valores que deseja multiplicar!\n");
            } else {
                printLines();
                printf("Entre com os numeros que deseja multiplicar\n");
                while (IDNum < reps) {
                    printf("> ");
                    scanf("%f", &A[IDNum]);
                    IDNum++;
                }
                sumRes = 1;
                for (IDNum = 0; IDNum < reps; IDNum++) {
                    sumRes = sumRes * A[IDNum];
                    A[IDNum] = 0;
                }
                printf("Resultado: %.4f\n\n\n", sumRes);
                reps = 1;
                IDNum = 0;
                sumRes = 0;
            }
            break;

            case 4:
            printLines();
            printf("Entre com o numerador da divisao\n> ");
            scanf("%f", &firstNum);
            printLines();
            printf("Entre com o denominador da divisao\n> ");
            scanf("%f", &secondNum);
            if (secondNum == 0) {
                printf("Digite um denominador diferente de 0!\n\n\n");
            } else {
                printf("Resultado: %.4f\n\n\n", firstNum / secondNum);
            }
            break;

            case 5:
            printLines();
            printf("Entre com o numerador da divisao de resto\n> ");
            scanf("%d", &IDNum);
            printf("Resultado: %d\n\n\n", IDNum % 2);
            break;

            case 6:
            printLines();
            printf("Digite a base do exponencial que deseja obter:\n> ");
            scanf("%f", &n);
            printLines();
            printf("Digite o expoente do exponencial que deseja obter:\n> ");
            scanf("%d", &reps);
            if (n >= 1) {
                printLines();
                printf("Resultado: %.2f\n\n\n", calcExp(n, reps));
            } else {
                printf("Digite um valor inteiro positivo!\n\n\n");
            }
            break;

            case 7:
            printLines();
            printf("Digite o fatorial que deseja obter:\n> ");
            scanf("%f", &n);
            if (n >= 1) {
                printLines();
                printf("Resultado: %.2f\n\n\n", calcFact(n));
            } else {
                printf("Digite um valor inteiro positivo!\n\n\n");
            }
            break;

            case 8:
            printLines();
            printf("Digite o valor do angulo que deseja obter o seno:\n> ");
            scanf("%f", &n);
            printLines();
            printf("Digite o numero de repeticoes do somatorio:\n> ");
            scanf("%d", &reps);
            printf("Resultado: %.4f\n\n\n", calcSen(n, reps));
            break;

            case 9:
            printLines();
            printf("Digite o valor do angulo que deseja obter o cosseno:\n> ");
            scanf("%f", &n);
            printLines();
            printf("Digite o numero de repeticoes do somatorio:\n> ");
            scanf("%d", &reps);
            printf("Resultado: %.4f\n\n\n", calcCos(n, reps));
            break;

            case 0:
            printLines();
            printf("Programa encerrado.\n");
            runtimeLoop = 0;
            break;
        }
    }
    system("PAUSE");
    return 0;
}
