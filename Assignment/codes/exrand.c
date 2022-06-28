

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
//Uniform random numbers
uniform("uni.dat", 1000000);

//Gaussian random numbers
gaussian("gau.dat", 1000000);

//Required random numbers
required("req.dat", 1000000);

//Mean of uniform distribution
printf("Mean of uniform distribution = %lf\n",mean("uni.dat"));
printf("Variance of uniform distribution = %lf\n", variance("uni.dat"));
printf("E[x^2] = %lf\n", mean2("uni.dat"));

//Mean and Variances of Gaussian distribtion
printf("Mean of Gaussiab distribution = %lf\n",mean("gau.dat"));
printf("Variance of Gaussian distribution = %lf\n", variance("gau.dat"));
printf("E[x^2] = %lf\n", mean2("gau.dat"));


//Mean and Variances of Required distribution
printf("Mean of the required distribution = %lf\n",mean("req.dat"));
printf("Variance of the required distribution = %lf\n", variance("req.dat"));
printf("E[x^2] = %lf\n", mean2("req.dat"));
//printf("min = %lf\n", min("req.dat"));
//printf("max = %lf\n", max("req.dat"));

return 0;
}
