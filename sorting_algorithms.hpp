#include <vector>

void insertion_sort(std::vector<int> & array)
{
	int size = array.size();
	int i = 1;
    int key;

	while (i != size)
	{
		int j = i;
        key = array[i];
		while (j > 0 && array[j-1] > key) 
		{
            array[j] = array[j-1];
			j--;
		}
        array[j] = key;
		i++;
	}
}

void selection_sort(std::vector<int> & array)
{
	int size = array.size();

	for (int i = 0; i < size - 1; i++)
	{
		int min_index = i;

		for (int j = i+1; j < size; j++)
		{
			if (array[j] < array[min_index])
				min_index = j;
		}
		
		if (min_index != i)
            std::swap(array[i], array[min_index]);
	}
}

void bubble_sort(std::vector<int> & array)
{
    int n = array.size();
    bool swapped = false;

    do {
        swapped = false;

        for (int i = 0; i <= n - 2; i++) {
            if (array[i] > array[i+1])
            {
                std::swap(array[i], array[i+1]);
                swapped = true;
            }
        }
    } while (swapped); 
}

void shell_sort(std::vector<int> &array)
{
    int size = array.size();

    for (int gap = size/2; gap > 0; gap/=2)
    {
        int j, key;
        for (int i = gap; i < size; i++)
        {
            key = array[i];
            for (j = i; j >= gap && array[j-gap] > key; j-=gap)
               array[j] = array[j-gap];
        }
        array[j] = key;
    }
}


