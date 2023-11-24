
int leiaInteiro();
void escrevaInteiro(int pi);

int add(int s, int t){
	return s + t;
}

int sub(int u, int v){
	return u - v;
}

int mul(int x, int w){
	return x * w;
}

int div(int y, int z){
	return y / z;
}

int main(){
	int a = 0;
	int b = 0;
	int c = 0;
	int d = 0;
	int res = 0;
	int i;

	i = 0;

    do {
        a = leiaInteiro();
        b = leiaInteiro();
        c = leiaInteiro();
        d = leiaInteiro();
        res = add(add(mul(a,b),div(a,b)), sub(d,c));
        escrevaInteiro(res);
        i = i + 1;
	} while (i < 5);

    return(0);
}
