#include<iostream>
#include <fstream>
#include<math.h>

using namespace std;


float du1dt(float u1);
float du2dt(float u2);
float du3dt(float u3);
float dv1dt(float omega ,float gamma, float k, float m,float v1, float u1, float u2);
float dv2dt(float gamma, float k, float m, float v2 , float u1, float u2, float u3);
float dv3dt(float gamma, float k, float m,float v3, float u2, float u3);
float leapfrog(float dt, float t_0, float t_final, string name);

int main()
{
	float m = 1000;
	float gamma= 0.0;
	float k = 2000;
	float omega= 1.0*sqrt(k/m);
	float dt=0.1;

	float u1=1;
	float u2=2;
	float u3=3;
	float v1=0;
	float v2=0;
	float v3=0;

	du1dt(u1);
	du2dt(u2);
	du3dt(u3);
	dv1dt(omega ,gamma, k,m,v1,u1,u2);
	dv2dt(gamma,k,m,v2,u1,u2,u3);
	dv3dt(gamma,k,m,v3,u2,u3);

	return 0; 
}


float du1dt(float u1)
{
	return u1;
}

float du2dt(float u2)
{
	return u1;
}

float du3dt(float u3)
{
	return u3;
}
float dv1dt(float omega ,float gamma, float k, float m,float v1, float u1, float u2 )
{
	return (-gamma*v1 - 2*k*u1 + k*u2 + sin(omega*t))/m;
}

float dv2dt(float gamma, float k, float m, float v2 , float u1, float u2, float u3)
{
 	return (-gamma*v2 +k*u1 - 2*k*u2 + k*u3)/m;
}

float dv3dt(float gamma, float k, float m,float v3, float u2, float u3)
{
	return (-gamma*v3 + k*u2 - k*u3)/m;
}

void leapfrog(float dt, float t_0, float t_final, string name)
{
	float u1=1;
	float u2=2;
	float u3=3;
	float v1=0;
	float v2=0;
	float v3=0;
	//float u1new, u2new, u3new;
	//float v1new, v2new, v3new;

	ofstream outfile;
	outfile.open(name);

	for(int i= t_0; i<= t_final ; i++)
	{
		u1= 1;
		u2= 2;
		u3= 3;
		//v1= v1new;
		//v2= v2new;
		//v3= v3new;
		outfile<< u1 << " " <<u2 << " " << u3 << " " << v1 << " " << v2 << " " << v3 << endl; 
		u1 = u1 + 0.5*dt*du1dt(omega,gamma,k,m,v1, u1,u2);
		u2 = u2 + 0.5*dt*du2dt(gamma,k,m,v2,u1,u2,u3);
		u3 = u3 + 0.5*dt*du3dt(gamma,k,m,v3,u2,u3);

		v1 = v1 + dt*dv1dt(omega,gamma,k,m,v1, u1,u2);
		v2 = v2 + dt*dv2dt(gamma,k,m,v2,u1,u2,u3);
		v3 = v3 + dt*dv3dt(gamma,k,m,v3,u2,u3);
		t_0+= dt; 

	}


	outfile.close();
}