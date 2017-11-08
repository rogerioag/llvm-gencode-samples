int leiaInteiro(void);
float leiaFlutuante(void);

void escrevaInteiro(int ni);
void escrevaFlutuante(float nf);

int main(){

  int a = leiaInteiro();
  int b = leiaInteiro();
  escrevaInteiro(a + b);

  float c = leiaFlutuante();
  float d = leiaFlutuante();
  escrevaFlutuante(c + d);

  return 0;
}
