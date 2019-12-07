#include <stdio.h>
#include <math.h>

int main(int argc, char *argv[]) {
	
	int t = 0;
	scanf("%d",&t);
	
	for(int i=0;i<t;i++){
		int m = 0;
		scanf("%d",&m);
		int ms[m];
		for (int j=0; j<m; j++){
			scanf("%d",&ms[j]);
		}
		int n = 0;
		scanf("%d",&n);
		int ns[n];
		for (int j=0; j<n; j++){
			scanf("%d",&ns[j]);
		}
		
		int count = 0;
		for (int j=0; j<m; j++){
			for (int k=0; k<n; k++){
				double inter_x = (ms[j]+ns[k]) * 0.5;
				if (inter_x - round(inter_x) == 0){
					count ++;
				}
			}
		}
		printf("%d\n", count);
	}
	
	return 0;
}