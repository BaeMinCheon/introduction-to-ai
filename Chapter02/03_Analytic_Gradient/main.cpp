#include <iostream>
#include <conio.h>
#include <random>

void AnalyticGradient(float& X, float& Y)
{
	const float stepSize = 0.1;

	float derivativeOfX = Y;
	float derivativeOfY = X;

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
			AnalyticGradient(X, Y);
		}
	}

	std::cout << "\n\t program ended, press any key to exit \n";
	_getch();
	return 0;
}