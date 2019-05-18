#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include <sys/time.h>


#define N 9
#define BLANK 0
#define SPACE " "
#define LINE "|"
#define NEW_ROW "\n-------------------------------------\n"
#define true 1
#define false 0

short SUDOKU[N][N] = {{0,6,0,0,2,0,0,4,0}, {5,0,0,3,0,0,0,0,0}, {0,8,0,0,1,0,0,0,0}, {6,0,0,0,0,7,0,0,0}, {0,3,7,0,0,0,2,8,0}, {0,2,0,8,0,0,0,3,0}, {0,0,0,0,0,0,0,0,0}, {7,0,0,4,0,0,0,0,1}, {0,0,0,0,6,0,0,2,0}};

int counter = 0;

typedef struct position{
    short x;
    short y;
}position;


void printSudoku(short sudoku[9][9]){
    printf(NEW_ROW);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            printf(SPACE);
            if(sudoku[i][j] == BLANK) printf(SPACE);
            else printf("%d", sudoku[i][j]);
            printf(SPACE);
            printf(LINE);
        }
        printf(NEW_ROW);
    }
}

void fprintSudoku(short sudoku[9][9], FILE* fp){
    fprintf(fp, NEW_ROW);
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            fprintf(fp, SPACE);
            if(sudoku[i][j] == BLANK) fprintf(fp, SPACE);
            else fprintf(fp, "%d", sudoku[i][j]);
            fprintf(fp, SPACE);
            fprintf(fp, LINE);
        }
        fprintf(fp, NEW_ROW);
    }
}

short used_in_row(short grid[N][N], int row, int num)
{
	for (int col = 0; col < N; col++)
		if (grid[row][col] == num)
		{
			return true;
		}
	return false;
}

// Returns a shortean which indicates whether any assigned entry
// in the specified column matches the given number. 
short used_in_col(short grid[N][N], int col, int num)
{
	for (int row = 0; row < N; row++)
		if (grid[row][col] == num)
		{
			return true;
		}
	return false;
}

// Returns a shortean which indicates whether any assigned entry
// within the specified 3x3 box matches the given number. 
short used_in_box(short grid[N][N], int box_start_row, int box_start_col, int num)
{
	for (int row = 0; row < 3; row++)
		for (int col = 0; col < 3; col++)
			if (grid[row + box_start_row][col + box_start_col] == num) 
			{
				return true;
			}
	return false;
}

// Returns a shortean which indicates whether it will be legal to assign
// num to the given row,col location.
short is_safe(short grid[N][N], int row, int col, int num)
{
	// Check if 'num' is not already placed in current row,
	// current column and current 3x3 box 
	return !used_in_row(grid, row, num) &&
		!used_in_col(grid, col, num) &&
		!used_in_box(grid, row - row % 3, col - col % 3, num);
}

position get_next_empty_pos(short sudoku[N][N]){
    position res;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < N; j++){
            if(sudoku[i][j] == BLANK){
                res.x = i;
                res.y = j;
                return res;
            }
        }
    }
    res.x = -1;
    res.y = -1;
    return res;
}

void solutions_no(short sudoku[N][N], FILE* fp){
    position pos = get_next_empty_pos(sudoku);
    if(pos.x == -1){
        fprintSudoku(sudoku, fp);
        counter++;
        return;
    }

    for(short num = 1; num <= 9; num++){
        if(is_safe(sudoku, pos.x, pos.y, num)){
            sudoku[pos.x][pos.y] = num;
            solutions_no(sudoku, fp);
            sudoku[pos.x][pos.y] = BLANK;
        }
    }

}

int main(){
    srand(time(NULL));
    printSudoku(SUDOKU);
    struct timeval start, end;
    FILE* fp = fopen("RESULTS.txt", "w");
    printf("START\n");
    gettimeofday(&start, NULL);
    solutions_no(SUDOKU, fp);
    gettimeofday(&end, NULL);
    printf("END\n");
    fclose(fp);
    printf("Solutions: %d, time consumed: %fs", counter, (double)(end.tv_usec-start.tv_usec) / 1e6);
    return 0;
}