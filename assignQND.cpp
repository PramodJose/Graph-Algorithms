#include <iostream.h>
#include <fstream.h>

#define INFILE "graph.dat"

class VertexNode
{
	unsigned short int vNum, dfsNum, lowestParentNum;
	char* vName;

	union
	{
		unsigned short int color;
		bool visited;
	}status;

	VertexNode **adjVertVec;
	unsigned short int adjacentVertices
	static const unsigned int WHITE, GRAY, BLACK;
};

const unsigned int VertexNode::WHITE = 0, VertexNode::GRAY = 1, VertexNode::BLACK = 2;

ifstream fin;
ofstream fout;

void tSort()
{

}

int main(int argc, char* argv[])
{
	if (argc != 2)
	{
		printf("Usage:-\nprog.out <out-file-name>\n");
		return 1;
	}
	
	fin.open(INFILE, ios::in);
	fout.open(argv[1], ios::out);


	fin.close();
	fout.close();
	return 0;
}