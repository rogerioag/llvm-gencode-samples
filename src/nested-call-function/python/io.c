#include <stdio.h>

void escrevaInteiro(int ni) {
  printf("%d\n", ni);
}

void escrevaFlutuante(float nf) {
  printf("%f\n", nf);
}

int leiaInteiro() {
  int num;
  scanf("%d", &num);
  return num;
}

float leiaFlutuante() {
  float num;
  scanf("%f", &num);
  return num;
}
