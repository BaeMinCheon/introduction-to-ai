#include <iostream>
#include <conio.h>
#include <random>

void BackPropagation(float& X, float& Y, float& Z)
{
	const float stepSize = 0.1;

	float derivativeOfQ = Z;
	float derivativeOfZ = X + Y;

	float derivativeOfX = 1 * derivativeOfQ;
	float derivativeOfY = 1 * derivativeOfQ;

	X += derivativeOfX * stepSize;
	Y += derivativeOfY * stepSize;
	Z += derivativeOfZ * stepSize;
}


int main()
{
	float X = -2.0f;
	float Y = +5.0f;
	float Z = -4.0f;

	for (int i = 0; ; ++i)
	{
		std::cout << "#" << i << "\n";
		std::cout << "( X, Y, Z ) = ( " << X << ", " << Y << ", " << Z << " ) \n";
		std::cout << "\t ( X + Y ) * Z = " << (X + Y) * Z << "\n";

		if ((X + Y)*Z > 0.0f)
		{
			break;
		}
		else
		{
			BackPropagation(X, Y, Z);
		}
	}

	std::cout << "\n\t program ended, press any key to exit \n";
	_getch();
	return 0;
}