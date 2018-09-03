#include <iostream>
#include <conio.h>
#include <random>

void NumericalGradient(float& X, float& Y)
{
	const float h = 0.0001;
	const float stepSize = 0.1;

	float derivativeOfX = ((X + h) * Y - X * Y) / h;
	float derivativeOfY = ((Y + h) * X - X * Y) / h;

	X += derivativeOfX * stepSize;
	Y += derivativeOfY * stepSize;
}


int main()
{
	float X = -2.0f;
	float Y = +3.0f;

	for (int i = 0; ; ++i)
	{
		std::cout << "#" << i << "\n";
		std::cout << "( X, Y ) = ( " << X << ", " << Y << " ) \n";
		std::cout << "\t X * Y = " << X * Y << "\n";

		if (X * Y > 0.0f)
		{
			break;
		}
		else
		{
			NumericalGradient(X, Y);
		}
	}

	std::cout << "\n\t program ended, press any key to exit \n";
	_getch();
	return 0;
}