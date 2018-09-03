#include <iostream>
#include <conio.h>
#include <random>

void RandomSearch(float& X, float& Y)
{
	static std::random_device dev;
	static std::mt19937 gen(dev());
	static std::uniform_real<float> dist;

	X += dist(gen);
	Y += dist(gen);
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
			RandomSearch(X, Y);
		}
	}

	std::cout << "\n\t program ended, press any key to exit \n";
	_getch();
	return 0;
}