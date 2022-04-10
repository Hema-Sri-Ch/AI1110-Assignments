/* Name : Hema Sri Cheekatla
CS21BTECH11013
2018 Paper, problem 4a
Solve the system of linear equations to find the set of integral values of x,
for which the following inequation holds,

	10x-2 <= 13x+10 < 10x+24, where x belongs to integers
line 1 = 10x-y = 2
line 2 = 13x-y = -10
line 3 = 10x-y = -24 */

# include <stdio.h>
// a struct to store two values (touple, coordinates/coefficients )
struct coord{
	float x;
	float y;
};

// making touple
struct coord make_coord(float a, float b){
	struct coord n;
	n.x = a;
	n.y = b;
	return n;
}

// solving equations by using the coefficient matrix and the constants r and s
struct coord solve(struct coord m, struct coord n, float r, float s){
	struct coord p;
	p.x = (r*(n.y) - s*(m.y))/((m.x)*(n.y) - (n.x)*(m.y));
	p.y = (r*(n.x) - s*(m.x))/((n.x)*(m.y) - (m.x)*(n.y));
	return p;
}
// Printing the pair
void print_coord(struct coord p){
	printf("( %.2f, %.2f)\n", p.x, p.y);
}
int main(){
	struct coord a1, a2, a3;
	float b1, b2, b3;
	a1 = make_coord(10, -1); // coefficients of line 1
	a2 = make_coord(13, -1); // coefficients of line 2
	a3 = make_coord(10, -1); // coefficients of line 3
	b1 = 2;
	b2 = -10;
	b3 = -24;
// p1 and p2 intersection points
	struct coord p1, p2;
// solving line 1 and line 2
	p1 = solve(a1,a2,b1,b2);
// solving line 2 and line 3
	p2 = solve(a2,a3,b2,b3);
	printf("The point of intersection of line 1 and line 2 :");
	print_coord(p1);
	printf("The point of intersection of line 3 and line 2 :");
	print_coord(p2);
// set of required integral x values
	printf("The set of x coordinates satisfying the required condition are: \n");
	int i;
	for (i=(int)p1.x; i<p2.x; i++) printf("%d, ",i);
	printf("\n");
	return 0;
}
